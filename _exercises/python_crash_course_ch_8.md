---
layout: page
title: Exercises Chapter 8
description: Select exercises from Python Crash Course (Chapter 8)
---
# Python Crash Course Chapter 8

 > 8-1, 8-2, 8-3, 8-5, 8-6, 8-7

Ellis Brown

## 8-1. Message
Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly. 


```python
def display_message():
    print("I am learning about functions in this chapter.")

display_message()
```

    I am learning about functions in this chapter.


## 8-2. Favorite Book
Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.


```python
def favorite_book(title: str) -> None:
    print(f"My favorite book is {title.title()}.")

book_title = "Alice in Wonderland"
favorite_book(book_title)
```

    My favorite book is Alice In Wonderland.


## 8-3. T-Shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


```python
# Here is a fun example of "typed python" which accepts data types : )
def make_shirt(size: int, text: str) -> None:
    print(f"Size: {size}, Text: {text}")

make_shirt(4348, "I love python woohoo!")
make_shirt(text="I love python woohoo!", size=4348)
make_shirt(size=4348, text="I love python woohoo!")

```

    Size: 4348, Text: I love python woohoo!
    Size: 4348, Text: I love python woohoo!
    Size: 4348, Text: I love python woohoo!


## 8-5. Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.


```python
def describe_city(city_name: str, country: str= "Canada") -> None:
    print(f"{city_name} is in {country}.")

describe_city("Toronto")
describe_city("Vancouver")
describe_city("New York", "USA")
```

    Toronto is in Canada.
    Vancouver is in Canada.
    New York is in USA.


## 8-6. City Names
Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.


```python
def city_country(city_name: str, country: str) -> str:
    return f"{city_name}, {country}"

city_country("Bangalore", "India")
city_country("San Francisco", "USA")
city_country("Toronto", "Canada")
```




    'Toronto, Canada'



## 8-7. Album
Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.


```python
def make_album(artist_name: str, album_title: str, num_songs: int = None) -> dict:
    if num_songs:
        return {"artist": artist_name, "album": album_title, "num_songs": num_songs}
    else:
        return {"artist": artist_name, "album": album_title}

print(make_album("GreenDay", "Dookie"))
print(make_album("GreenDay", "Dookie", 14))
print(make_album("GreenDay", "American Idiot", 12))
```

    {'artist': 'GreenDay', 'album': 'Dookie'}
    {'artist': 'GreenDay', 'album': 'Dookie', 'num_songs': 14}
    {'artist': 'GreenDay', 'album': 'American Idiot', 'num_songs': 12}



```python

```
