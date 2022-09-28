---
layout: page
title: Exercises Chapter 5
description: Select exercises from Python Crash Course (Chapter 5)
---


# Python Crash Course Chapter 5

## 5-1. Conditional Tests
Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. 


```python
class Ellis:
    def is_programmer(self):
        return True

    def is_awesome(self):
        return True
    def is_a_sophomore(self):
        return False

print("Is ellis a programmer? I think so!")
ellis = Ellis()
print("Am I a programmer?")
print(ellis.is_programmer() == True)
```

    Is ellis a programmer? I think so!
    Am I a programmer?
    True



```python
x = 5
print("Is x not equal to 6?, I think so!")
print(x != 6)
```

    Is x not equal to 6?, I think so!
    True



```python
a = 5
b = 5
print("Is a greater than b?, I think not!")
print(a > b)
```

    Is a greater than b?, I think not!
    False



```python
a = 5
b = 5
print("Is a less than or equal to b? I think so!")
print(a <= b)

```

    Is a less than or equal to b? I think so!
    True



```python
historian = "Isabel Wilkerson"
print("Is historian != 'isabel wilkerson'? I predict True.")
print(historian != "isalbel wilkerson")
```

    Is historian != 'isabel wilkerson'? I predict True.
    True


## 5-2. More Conditional Tests

You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:

- Tests for equality and inequality with strings
- Tests using the `lower()` method
- Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
- Tests using the `and` keyword and the `or` keyword
- Test whether an item is in a list
- Test whether an item is not in a list


```python
# Test for equality and inequality with strings
name = "Ellis"
print("Is name == 'Ellis'?", name == "ELLIS")
```

    Is name == 'Ellis'? False



```python
# Tests using the lower() method
name = "Ellis"
print("Is name.lower() == 'ellis'?", name.lower() == "ellis")

```

    Is name.lower() == 'ellis'? True



```python
# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, 
# and less than or equal to
time = 4
print("Is time == 4?", time == 4)
print("Is time != 4?", time != 4)
print("Is time > 4?", time > 4)
print("Is time < 4?", time < 4)
print("Is time >= 4?", time >= 4)
print("Is time <= 4?", time <= 4)

```

    Is time == 4? True
    Is time != 4? False
    Is time > 4? False
    Is time < 4? False
    Is time >= 4? True
    Is time <= 4? True



```python
# Tests using the and keyword and the or keyword
a = 5
b = "puppy"
print("Is a == 5 and b == 'puppy'?", a == 5 and b == "puppy")
print("Is a == 5 or b == 'puppy'?", a == 5 or b == "puppy")
print("Is a == 5 and b == 'cat'?", a == 5 and b == "cat")
print("Is a == 5 or b == 'cat'?", a == 5 or b == "cat")

```

    Is a == 5 and b == 'puppy'? True
    Is a == 5 or b == 'puppy'? True
    Is a == 5 and b == 'cat'? False
    Is a == 5 or b == 'cat'? True



```python
# Test whether an item is in a list
classes = ["cls161", "cs117", "cs97", "math63"]
print("Am I taking CS98?", "yes" if "cs98" in classes else "no")
```

    Am I taking CS98? no



```python
# Test whether an item is not in a list
# Test whether an item is in a list
classes = ["cls161", "cs117", "cs97", "math63"]
print("Am I taking CS98?", "no" if "cs98" not in classes else "yes")
```

    Am I taking CS98? no


## 5-6. Stages of Life

Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

- If the person is less than 2 years old, print a message that the person is a baby.
- If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
- If the person is at least 4 years old but less than 13, print a message that the person is a kid.
- If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
- If the person is at least 20 years old but less than 65, print a message that the person is an adult.
- If the person is age 65 or older, print a message that the person is an elder.


```python
age = 41
if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >=4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >=20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder")
```

    The person is an adult.


## 5-7. Favorite Fruit

Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

- Make a list of your three favorite fruits and call it favorite_fruits.
- Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!



```python
fav_fruits = ["Black Plums", "Red Plums", "Bananas"]
if "Black Plums" in fav_fruits:
    print("You really like black plums!")
if "Red Plums" in fav_fruits:
    print("You really like red plums!")
if "Bananas" in fav_fruits:
    print("You really like bananas!")
if "Apples" in fav_fruits:
    print("You really like apples!")
if "Oranges" in fav_fruits:
    print("You really like oranges!")
    
```

    You really like black plums!
    You really like red plums!
    You really like bananas!


## 5-8. Hello Admin

Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

- If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
- Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


```python
users = ["ebrown26", "atanne02", "ashah01", "admin", "adahal02"]
for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Welcome to the server, {user}!")
        
```

    Welcome to the server, ebrown26!
    Welcome to the server, atanne02!
    Welcome to the server, ashah01!
    Hello admin, would you like to see a status report?
    Welcome to the server, adahal02!


## 5-9. No Users

Add an if test to hello_admin to make sure the list of users is not empty.

- If the list is empty, print the message We need to find some users!
- Remove all of the usernames from your list, and make sure the correct message is printed.


```python

def greet(users):
    if users:
        for user in users:
            if user == "admin":
                print("Hello admin, would you like to see a status report?")
            else:
                print(f"Welcome to the server, {user}!")
    else:
        print("We need to find some users!")
users = ["ebrown26", "atanne02", "ashah01", "admin", "adahal02"]
greet(users)
print("---------------- empty list ----------------")
users = []
greet(users)
```

    Welcome to the server, ebrown26!
    Welcome to the server, atanne02!
    Welcome to the server, ashah01!
    Hello admin, would you like to see a status report?
    Welcome to the server, adahal02!
    ---------------- empty list ----------------
    We need to find some users!


## 5-10. Checking Usernames

Do the following to create a program that simulates how websites ensure that everyone has a unique username.

- Make a list of five or more usernames called current_users.
- Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
- Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
- Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)


```python
current_users = ["ebrown26", "atanne02", "ashah01", "admin", "adaHal02"] # caps once
new_users = ["ebROWn26", "root", "adahal02", "jdoe01", "jdoe02"] # caps once
for user in new_users:
    if user.lower() in [x.lower() for x in current_users]: # space complexity is HAHAHAH
        print(f"Sorry {user}, that username is taken.")
    else:
        print("Welcome to the team!")
```

    Sorry ebROWn26, that username is taken.
    Welcome to the team!
    Sorry adahal02, that username is taken.
    Welcome to the team!
    Welcome to the team!



```python

```
