---
layout: page
title: Exercises Chapter 4
description: Select exercises from Python Crash Course (Chapter 4)
---


# Python Crash Course Chapter 4

## 4-1. Pizzas
Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

- Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
- Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!


```python
pizza = ["pineapple", "ham", "pepper"]
# for pizza_topping in pizza:
#     print(pizza_topping)
# Above lines are commented out because they are not needed for the exercise anymore

for p in pizza:
    print(f"I like {p} pizza.")

print("I only kind of like pizza, I'm lactose intolerant")


```

    pineapple
    ham
    pepper
    I like pineapple pizza.
    I like ham pizza.
    I like pepper pizza.
    I only kind of like pizza, I'm lactose intolerant


## 4-2. Animals
Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

- Modify your program to print a statement about each animal, such as A dog would make a great pet.
- Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!


```python
animals = ["cat", "lion", "cheetah"]
for animal in animals:
    print(f"A {animal} may make a good pet... it depends")
    
print("All of these animals are cute, and look kind of like a cat")
```

    A cat may make a good pet... it depends
    A lion may make a good pet... it depends
    A cheetah may make a good pet... it depends
    All of these animals are cute, and look kind of like a cat


## 4-3. Counting to Twenty
Use a for loop to print the numbers from 1 to 20, inclusive.


```python
for n in range(1,21):
    print(n)
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20


## 4-6. Odd Numbers
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.


```python
for n in range(1, 20, 2):
    print(n)
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19


## 4-10. Slices
Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

- Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
- Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
- Print the message The last three items in the list are:. Use a slice to print the last three items in the list.


```python
pizza_toppings = ["pineapple", "ham", "pepper", "mushroom", "onion", "pepperoni"]

print("The first 3 items in the list are: ", pizza_toppings[:3])
print("The items from the middle of the list are: ", pizza_toppings[2:5])
print("The last 3 items in the list are: ", pizza_toppings[-3:])

```

    The first 3 items in the list are:  ['pineapple', 'ham', 'pepper']
    The items from the middle of the list are:  ['pepper', 'mushroom', 'onion']
    The last 3 items in the list are:  ['mushroom', 'onion', 'pepperoni']


## 4-11. My Pizzas, Your Pizzas
Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

- Add a new pizza to the original list.
- Add a different pizza to the list friend_pizzas.
- Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.


```python
pizza = ["pineapple", "ham", "pepper"]
friend_pizza = pizza.copy() # Works in python3, not in python2. I prefer this to slice [:] because it's more explicit
pizza.append("ice cream")
friend_pizza.append("chocolate")

print("My pizza contains:")
for topping in pizza:
    print(f"\t{topping}")

print("My friend's pizza contains:")
for topping in friend_pizza:
    print(f"\t{topping}")
```




    ['pineapple', 'ham', 'pepper']




```python

```
