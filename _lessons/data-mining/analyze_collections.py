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

