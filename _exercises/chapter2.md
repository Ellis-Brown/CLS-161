---
layout: page
title: Exercises Chapter 2
description: Select exercises from Python Crash Course
---


# Weekly Python: Week 1

## 2.1 Simple message: Store a message in a variable, then print the message


```python
message = "Changing my message!"
print(message)
```

    Changing my message!


## 2.2 Simple Message: Store a message in a variable, and print that message. Then change the value of your variable to a new message, and print the new message.


```python
message = "Default"
print(message)
message = "Changed"
print(message)
```

    Default
    Changed


## 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”



```python
friend = "Silvia"
print(f"Hello {friend}, would you like to learn some Python today?")
```

    Hello Silvia, would you like to learn some Python today?


## 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.



```python
name = "Micah Saxton"
print(name.lower())
print(name.upper())
print(name.title())
```

    micah saxton
    MICAH SAXTON
    Micah Saxton



## 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:


```python
quote = 'Obama once said "Change will not come if we wait for some other person or some other time. We are the ones we\'ve been waiting for. We are the change that we seek."'
print(quote)
```

    Obama once said "Change will not come if we wait for some other person or some other time. We are the ones we've been waiting for. We are the change that we seek."


## 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.



```python
famous_person = "Obama"
message = f'{famous_person} once said "Change will not come if we wait for some other person or some other time. We are the ones we\'ve been waiting for. We are the change that we seek."'
print(message)
```

    Obama once said "Change will not come if we wait for some other person or some other time. We are the ones we've been waiting for. We are the change that we seek."


## 2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.


```python
name = "  \t \nAnkur Dahal  "
print(f"|{name}|")
print(f"|{name.strip()}|")
```

    |  	 
    Ankur Dahal  |
    |Ankur Dahal|


## 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results. You should create four lines that look like this:


```python
print(4 + 2 + 2)
print(3 - (-5))
print(4 * 2)
print(int(16 / 2)) # This is resulting a float type, but I cast it into an integer using the (int) function
# It is recommended to use the // operator for integer division, though.

```

    8
    8
    8
    8


## 2-9. Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.



```python
favorite_number = 4348
print(f"My favorite number is {favorite_number}.")
```

    My favorite number is 4348.


## 2-10. Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.

This is done in 2-8