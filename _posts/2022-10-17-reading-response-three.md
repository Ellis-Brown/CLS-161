---
layout: post
title:  "Reading Response Three"
date:   "2022-10-17"
categories: jekyll update
---
# Reading and reflection blog posts

For this week's post, I will be discussing [_Technology is Taking Over English Departments_](https://newrepublic.com/article/117428/limits-digital-humanities-adam-kirsch) by Adam Kirsh. This article gives an analysis of other media discussing Digital Humanities, and the possible paradigm shift of digital humanities work and research. The article brings up a lot of very interesting points about the role, driving factors, and future of work that is considered digital humanities. I found the following two paragraphs very interesting, which brought up a lot of interesting points, and honestly leaves you with more questions than answers:

> If computers cannot think better than human beings, digital humanists are left with the argument that at least they can think faster—the John Henry argument. In the essay “Developing Things: Notes toward an Epistemology of Building in the Humanities,” Ramsay and Geoffrey Rockwell observe, “Reading Foucault and applying his theoretical framework can takes months or years of application. A web-based text analysis tool could apply its theoretical position in seconds.” Never mind that understanding that theoretical position will take more than seconds. Here are nicely encapsulated the two fundamental errors that theorizing about the revolutionary nature of digital humanities often commits. First, there is the idea that thinking humanistically is a matter of taking a framework of ideas and “applying” it to a text or a work of art. The second is the idea that applying ideas in this way leads to an external self-subsistent result, be it a theory or another book or a piece of driftwood with pictures on it.
> 
> Both of these errors derive from a false analogy between the humanities and the sciences. Humanistic thinking does not proceed by experiments that yield results; it is a matter of mental experiences, provoked by works of art and history, that expand the range of one’s understanding and sympathy. It makes no sense to accelerate the work of thinking by delegating it to a computer when it is precisely the experience of thought that constitutes the substance of a humanistic education. The humanities cannot take place in seconds. This is why the best humanistic scholarship is creative, more akin to poetry and fiction than to chemistry or physics: it draws not just on a body of knowledge, though knowledge is indispensable, but on a scholar’s imagination and sense of reality. Of course this work cannot be done in isolation, any more than a poem can be written in a private language. But just as writing a poem with a computer is no easier than writing one with a pen, so no computer can take on the human part of humanistic work, which is to feel and to think one’s way into different times, places, and minds.

The author is clearly contemplating the role and purpose of digital / computational tools in the world of humanities research. Consider these sentences from paragraph one: "'Reading Foucault and applying his theoretical framework can takes months or years of application. A web-based text analysis tool could apply its theoretical position in seconds.'" This is something that the author disagrees with, showing how the application of a digital tool to some framework is not truly bringing about any self discovery or understanding, it is just making an artifcat. I agree with the author, there is a lot of value in understanding, reading, and learning things that cannot be intrinsically captured or replaced by computers. Computers are incredibly effective at pattern matching, and can assist in productivity and accessiblity of work and information to many, but they cannot fundementally replace the self development of an individual. Therefore, within the humanities which is often focused on **humans** understanding **humans**, the computational tools can never truly replace the role of humams in the studies of humanities. Even in a future where computers are capable of original ideas with their own emotions and thoughts, we ourselves have an inherent desire to learn and understand the world. Therefore, I would argue the value of digital processing in humanities research is always going to be an aid for the researcher, never a replacement. I believe that the day that humanities researchers are replaced by computers is the day that people do not have a desire to learn anymore, and I think this day will never come. 

Secondly, the results driven mindset related to the possibilites of a future in digital humanities is very interesting to me. Computers are shaping our lives, allowing us to work in *some ways* more productively, such as the grammarly web tool assisting with spelling and sentence flow, or online communication tools for team work and collaboration, but the end user of all of these tools are humans. Many people would agree that lots of work should be automated, and it helps advance the quality of life for many. I think the concept of using computational tools to reduce the work and effort spent understanding the nuances of an artifcat takes may away the fundemental reason for doing so, in some fields of research, however. If computers were meant to be a filter between the world and the information consumed, then people would only read book summaries, movie summaries, and would often not produce their own work or apply their own voice or thoughts to the things they produce. While computers can greatly increase our productivty, productivity can only be defined by results. Not all digital humanities or humanities research is meant to be results driven, as said by the author. 

Therefore, I agree with the author with their claim that the results driven nature of current technology tools is not a perfect fit for the field of humanities. As a computer science major and someone who resisted learning about most humanities related things, I very much appreciate a seperation between some computer aided things and the human activities. Computers should strongly aid people, and make things more accessible, but should not take away from what people want to do. Research and findings aided by pattern searching and trend analysis is an amazing use of digital tools in humanities research, but only let you find what you are interested enough to look for.

---

The following is just a fun experiment.

Below this line, I will use an example of an AI trying to write it's own thoughts. Github Copilot is a code-assistant AI that processes a file, and attempts to predict what you will write next, from context and prompts. I will give it the prompt "In the future, I think AI will be able to ...", and lets see what it does. It was not designed to write in english, so I have also added a code example below the text.

The prompt for the code is to parse through a book, and find all occurances of nouns.

--- 
### Essay example using Github Copilot
In the future, I think AI will be able to write essays for me, but I will still have to write the essay myself. I think that the future of humanities research will be a combination of human and computer work. Computers will be able to do the tedious work, and humans will be able to do the creative work. The role of computers in today's life are to make things more accessible, and I think that will be the same in the future. 

### Code example using Github Copilot

After giving the prompt,it choose to do this in python. I typed only 2 things:
- I typed "im" to imply that the first line would be an import. It choose all the imports to include
- I typed "d" once it got stuck infintely importing. It knew to define a function
- I typed "def open" to encourage it to write a function to open the book
- I typed "def main" to have it generate the main.

On first run, I realized I needed to type `nltk.download()` to get the dependencies, rather than just installing with `pip`, but then the script was able to run.

The script worked. Try it yourself, or view my juypyter notebook here:
```python
## Define a function to parse through a book, and find all occurances of nouns.    

import nltk
from nltk.corpus import brown
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import RSLPStemmer
from nltk.stem import WordNetLemmatizer

def parse_book(book):
    # Tokenize the book
    tokens = word_tokenize(book)
    # Remove punctuation
    words = [word for word in tokens if word.isalpha()]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    # Stemming
    porter = PorterStemmer()
    words = [porter.stem(word) for word in words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    # POS Tagging
    tagged = nltk.pos_tag(words)
    # Find all nouns
    nouns = [word for word,pos in tagged if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
    return nouns
def open_book(book):
    # Open the book
    with open(book, 'r') as file:
        text = file.read().replace('\n', '')
    return text

def main():
    # Open the book
    book = open_book('book.txt')
    # Parse the book
    nouns = parse_book(book)
    # Print the nouns
    print(nouns)
```