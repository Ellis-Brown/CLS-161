---
layout: page
title: Data mining an internet archive
description: This lesson uses Python to mine data from the Boston Public Library internet archive. 
---

# Programming Historian Lesson 1

Lesson completed: [Data Mining the Internet Archive Collection](https://programminghistorian.org/en/lessons/data-mining-the-internet-archive)

## Reflection on learning:

I have broken my reflection into two parts, the first general, and the second focusing more on the tech stack.

### General Takeaways

Working with data collected over the years is not easy, data collection and processing is inconsistent, data cleaning is hard, and some metrics may not be recorded or lost. Firstly, the internet archive search generated 9769 items to be processed. Of these, 1 URL was not valid and could not be found on the server, which either implies a broken record, or that `_marc.xml` file we were interested in was not collected. For a complete investigation of this topic, one could reason that some archives were lost over the years, and 1/9769 missing was not relevant, but a more complete investigation into why this was is recommended. Secondly, the location data using the suggested schema could be scraped from 6947 out of 9769 data points. This is __far too low__, as its quite realistic to assume that the missing data could have been sourced from the same location, and the correlation between the location and mismatched or missing scheme data for location is high. This could greatly affect the integrity of the results. To account for this, either one must manually check all missing archives of 2822, which would be a tedious process, or look into patterns in the collected `_marc.xml` files. 

Cleaning the data turned out to be a large challenge as well. As this was not the focus of this module, I did not invest the needed time to perfect and fix the issue, but something clear came up within the data collection: Locations were not named consistently. We had "Boston", "Mass", "MA", "Boston, Mass" as all different locations recorded for archive records, but may or may not have referred to the real location. As a result, one goal would be to raise or lower the specificity to that of the same level, such as the state, or city level. However, it is not possible to make "Mass" more specific, as the location in Mass is unclear. This points to the conclusion that __data collected over time may be missing context, and a perfect record of what happens is not always obtainable__. The data also contained extra characters, trailing and leading spaces, which I removed using regular expressions. Overall, however, the cleaning of the data for statistical assessment was inadequate, due to the schemas missing for 2822 documents in the pattern we expected, and the inconsistency with the data we collected.

If I were to be adding more time spent on this project, I would make sure the data collected and gathered was all accounted for, errors in finding files were investigated, and all data processed was __manually__ checked at least once for consistency. While an extremely boring task, the __vast ways that similar data is presented needs to be accounted for, in order to prevent introducing bias from the perspective of the programmer due to a lack of understanding the dataset__. If I had chosen to bring everything to the state level, that introduces my bias that the location within the state is less of interest, and affects my conclusions and claims as well. Ultimately, it comes down to the person doing research to make the important decisions related to their claims and analysis. Anyone (even an AI) can build a web crawler on an archive, with enough time. The true challenge is making good use of that collected data.

### Technical takeaways

During this lesson, I had to work with a few libraries I was unfamiliar with. I worked with
`internetarchive`, `wordcloud`, and `pymarc` for the first time. The most interesting was internetarchive, which introduced the idea of searching an online archive for information, and allowed the script to locate the URL names of files, which could then be downloaded directly using the library or another tool. Also involved was a recommended timeout about slowing down requests to the web server. I am surprised that this timeout is implemented at the application layer of the program, rather than as part of the networking protocol, but I understand that a failure in the networking protocol from packet congestion would lead to a failure at the application level, so I guess it makes sense. I was curious about experimenting with the times for the timeout (0.001s vs 0.05s vs 0.5s vs 1s [recommend]),
but I did not get the chance to do this, because I introduced a caching system to prevent redownloads. Also, download is slow and depends on the network and the computer doing so, which impose multiple limitations at different points in time. However, these limitations are technical, but the main problems occur from the way in which this data collection is done.

---

 The code can be found below
```python
'''
> Overview
    The following will look through The Antislavery Collection at the Boston
    Public Library online archive. In order to understand more about the pieces
    of work in this collection, we will be collecting the publication locations,
    and creating a word cloud to give a visual picture of the data.

> Architecture
    The project searches the online internet archive for the relevant collection
    then downloads metadata files related to each publication in the form of
    "marc_xml" files.  These xml files are parsed to find their publication 
    location. The data is then cleaned and presented in a world map.

> Installation & Requirements
    This script is intended to be run with Python 3.9.14+

    The following python packages are required
    Install with: pip3 install <package>

        internetarchive
        pymarc
        time
        os
        matplotlib
        wordcloud
        re

> Cleanup
    This script will create multiple files on your local computer.
    To clean them up, navigate to the folder that holds this script, and run
    
        rm ./downloads/* && rmdir downloads;
    
    this will remove all downloaded files, which you do not want to keep
    forever. However, in between runs of the script, the list of files 
    downloaded is held in a set to prevent duplicate downloads, so do not
    delete the files until you are finished with analysis.


> Last modified
    9/28/2022

> Author
    Ellis Brown

> References
    This digital humanities project was built following inspiration from this
    tutorial, which outlines the premis of using the online archive to 
    capture publication data.
    https://programminghistorian.org/en/lessons/data-mining-the-internet-archive

> Notes
    The time it took for this to run on my local computer (M1 Macbook Pro)
    on a network with about 200 Mbps was about 10 minutes. This also required me
    to have 300MB storage available, so be careful before running this locally.
    To account for this, I have added a MAX DOCUMENTS to parse flag, which
    can be turned from -1 (indiciates ALL) to some sample, such as 50
'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#                               Imports
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import internetarchive as ia # search the internet archive for books & content
import pymarc # library for working with bibliographic data encoded in MARC21.
import time   # handles pauses
import os     # allows us to list and view files and directories
import matplotlib.pyplot as plt # For plotting the word cloud
from wordcloud import WordCloud # For generating the word cloud
import re as regex # Used to clean characters


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#                            Global Variables
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
DOWNLOAD_FOLDER = "./downloads/"
locations       = [] 
ALL             = -1           # -1 indicates all documents.
DOWNLOAD_PAUSE  = 0.5          # time in seconds so we do not spam the server
COLLECTION      = 'bplscas'
ERROR_LOG       = open("error_log.txt", "a")
MAX_DOCUMENTS   = ALL           #  n | ALL , where n is a positive integer
                      



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#                           download_results
#
#          Searches the internet archive for a specified COLLECTION.
#           Downloads the _marc.xml file associated with each result
#                          in that collection
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def download_results():
    print(" ** Searching archive **")
    time_start_search = time.time()
    search = ia.search_items('collection:' + COLLECTION) 
    current_files = set(os.listdir(DOWNLOAD_FOLDER))
    count = 0
    print("** Search complete. Time elapsed: "
          + str(time.time() - time_start_search) + "s **")
    print(" ** Beginning downloads **")
    time_start_downloads = time.time()
    for result in search:
        # process a portion of the search, rather than all documents
        if MAX_DOCUMENTS != ALL and count > MAX_DOCUMENTS:
            print(" ** Download of " + str(count) + " items complete. Time elapsed: " 
                   + str(time.time() - time_start_downloads) + "s **")
            return
        did_download = False
        try:
            id = result['identifier']

            item = ia.get_item(id)
            filename = id + "_marc.xml" # Do not download all data
                                        # We only need the marc metadata
            if filename not in current_files:
                current_files.add(filename)
                marc_xml = item.get_file(filename)
                print("Downloading " + filename + " . . . ")
                
                marc_xml.download(destdir=DOWNLOAD_FOLDER)
                print("Done!")
            else:
                print(f"{filename} already downloaded")
                did_download = True

        except Exception as e:
            ERROR_LOG.write("Error downloading " + id + ": " + str(e) + "\n")
        
        # We do not want to overload the Internet Archive with requests
        # Therefore, add a small timeout delay between downloads
        if not did_download:
            time.sleep(DOWNLOAD_PAUSE)

        count += 1

    print(" ** Download of " + str(count) + " items complete. Time elapsed: " 
          + str(time.time() - time_start_downloads) + "s **")




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#                              get_place_of_pub
#
#           Determine the place of publication for specified record
#          If the publication location cannot be found, skip the record
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def get_place_of_pub(record):
    if record:
        if '260' in record:
            if 'a' in record['260']:
                locations.append(record['260']['a'])
                return
    



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#                               clean_data
#
#           Takes as parameter a list of location names, and cleans
#                 the data for processing by the word cloud
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def clean_data(locations):
    print(" ** Cleaning data for " + str(len(locations)) + " locations **")
    only_chars = regex.compile('[^a-z A-Z]')
    remove_spaces = regex.compile(' ')
    # An important decision needs to be made here.
    # Some places have more or less specific locations.
    # In order for the cloud to be more accurate, the levels of
    # specificity should be the same.
    for i in range(len(locations)):
        word = locations[i].strip()
        if "," in word:
            word = word[:word.index(",")]
        word = only_chars.sub("", word)
        word = remove_spaces.sub("", word)
        locations[i] = word
    print(" ** Data successfully cleaned **")
    
        
        

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#                           generate_wordcloud
#
#             Takes in a list of words, speperated by spaces
#                      and generates a word cloud
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def generate_wordcloud(text):
    print(" ** Generating word cloud **")
    wordcloud = WordCloud(collocations = False,
                          background_color = 'white').generate(text)
    # Display the generated Word Cloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    print(" ** Opening wordcloud in new window **")
    plt.show()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
#                                  main
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
def main():
    # Create a directory to store the downloaded files
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    
    # Download the results to a local folder
    download_results()
    
    # Open the files we downloaded, and parse them
    print(" ** Gathering location data from downloaded files **")
    for filename in os.listdir(DOWNLOAD_FOLDER):
        if filename.endswith(".xml"):
            pymarc.map_xml(get_place_of_pub, DOWNLOAD_FOLDER + filename) 

    # Clean the data we got back. Remove extraneous characters
    clean_data(locations)

    # Generate a word cloud of the data we received
    generate_wordcloud(" ".join(locations))



# Run the code 
if __name__ == "__main__":
    main()

```
