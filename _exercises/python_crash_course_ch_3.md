---
layout: page
title: Exercises Chapter 3
description: Select exercises from Python Crash Course (Chapter 3)
---

# Python Crash Course Chapter 3

## 3-1. Names
Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.


```python
friends = ["Ankur", "Silvia", "Toshi", "Viet"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
```

    Ankur
    Silvia
    Toshi
    Viet


## 3-2. Greetings
Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.


```python
friends = ["Ankur", "Silvia", "Toshi", "Viet"]
print(f"What are you up to {friends[0]}?")
print(f"What are you up to {friends[1]}?")
print(f"What are you up to {friends[2]}?")
print(f"What are you up to {friends[3]}?")
```

    What are you up to Ankur?
    What are you up to Silvia?
    What are you up to Toshi?
    What are you up to Viet?


## 3-3. Your Own List
Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”


```python
vehicles = ["1999 Toyota Camry LE", "2006 Toyota Sienna", "2015 Toyota Prius"] 
# I have owned the first 2 cars. One day I hope to buy a prius
print(f"I enjoy getting around on a {vehicles[0]}.")
print(f"I enjoy getting around on a {vehicles[1]}.")
print(f"I enjoy getting around on a {vehicles[2]}.")
```

    I enjoy getting around on a 1999 Toyota Camry LE.
    I enjoy getting around on a 2006 Toyota Sienna.
    I enjoy getting around on a 2015 Toyota Prius.


## 3-4. Guest List
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.


```python
guests = ["annika tanner".title(), "Sopia Buell", "Nichols Taylor"]
print(f"Hello {guests[0].title()}, would you like to come to a dinner party?")
print(f"Hello {guests[1].title()}, would you like to come to a dinner party?")
print(f"Hello {guests[2].title()}, would you like to come to a dinner party?")
```

    Hello Annika Tanner, would you like to come to a dinner party?
    Hello Sopia Buell, would you like to come to a dinner party?
    Hello Nichols Taylor, would you like to come to a dinner party?


## 3-5. Changing Guest List
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

- Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

- Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

- Print a second set of invitation messages, one for each person who is still in your list.


```python
# code from 3-4
guests = ["annika tanner".title(), "Sopia Buell", "Nichols Taylor"]
for person in guests:
    print(f"Hello {person}, would you like to come to a dinner party?")

# remove one guest
busy = guests.pop(1)
print(f"{busy} is busy. Who should we invite instead?")

# new invitation messages
replacement = "Jesse Buell"
guests.append(replacement)
for person in guests:
    print(f"Hello {person}, would you like to come to a dinner party?")
```

    Hello Annika Tanner, would you like to come to a dinner party?
    Hello Sopia Buell, would you like to come to a dinner party?
    Hello Nichols Taylor, would you like to come to a dinner party?
    Sopia Buell is busy. Who should we invite instead?
    Hello Annika Tanner, would you like to come to a dinner party?
    Hello Nichols Taylor, would you like to come to a dinner party?
    Hello Jesse Buell, would you like to come to a dinner party?


## 3-6. More Guests
You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

- Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
- Use insert() to add one new guest to the beginning of your list.
- Use insert() to add one new guest to the middle of your list.
- Use append() to add one new guest to the end of your list.
- Print a new set of invitation messages, one for each person in your list.


```python
guests = ["annika tanner".title(), "Sopia Buell", "Nichols Taylor"]

# print statement for bigger table
print("I have a bigger table so I can invite more guests!")

# use insert() to add one guest to the beginning of the list
guests.insert(0, "John Doyle")


# use insert() to add one guest to the middle of the list
guests.insert(2, "Chao Duan")

# use append() to add one guest to the end of the list
guests.append("Jessie (i forgot her last name)")

# new invitations
for guest in guests:
    print(f"Hello {guest}, would you like to come to a dinner party?")
```

    I have a bigger table so I can invite more guests!
    Hello John Doyle, would you like to come to a dinner party?
    Hello Annika Tanner, would you like to come to a dinner party?
    Hello Chao Duan, would you like to come to a dinner party?
    Hello Sopia Buell, would you like to come to a dinner party?
    Hello Nichols Taylor, would you like to come to a dinner party?
    Hello Jessie (i forgot her last name), would you like to come to a dinner party?


## 3-7. Shrinking Guest List
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

- Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
- Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
- Print a message to each of the two people still on your list, letting them know they’re still invited.
- Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


```python
print("Sorry, it turns out I can only invite two people to dinner")

while len(guests) > 2:
    print(f"Sorry, {guests.pop()}, I can't invite you to dinner")

for guest in guests:
    print("I'm glad that you can still come, {guest}")

```

    Sorry, it turns out I can only invite two people to dinner
    I'm glad that you can still come, {guest}
    I'm glad that you can still come, {guest}


## 3-8. Seeing the World
Think of at least five places in the world you’d like to visit.

- Store the locations in a list. Make sure the list is not in alphabetical order.
- Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
- Use sorted() to print your list in alphabetical order without modifying the actual list.
- Show that your list is still in its original order by printing it.
- Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
- Show that your list is still in its original order by printing it again.
- Use reverse() to change the order of your list. Print the list to show that its order has changed.
- Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
- Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
- Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.


```python
locations = ["San Francisco", "San Diego", "Los Angeles", "San Jose", "Sacramento"]
```

    ['Iceland', 'South Africa', 'Australia', 'Alaska', 'Japan']
    ['Alaska', 'Australia', 'Iceland', 'Japan', 'South Africa']
    ['Iceland', 'South Africa', 'Australia', 'Alaska', 'Japan']
    ['Japan', 'Alaska', 'Australia', 'South Africa', 'Iceland']
    ['Iceland', 'South Africa', 'Australia', 'Alaska', 'Japan']
    ['Alaska', 'Australia', 'Iceland', 'Japan', 'South Africa']
    ['South Africa', 'Japan', 'Iceland', 'Australia', 'Alaska']

