# the main kind of loop in python is the for loop.

# it looks like this:

for i in range(10):
    print(i)

# this will print the numbers 0 to 9, because it stops before 10.

# you can also use a for loop to iterate over a list or string.

from lists import fruits 

#this imports the fruits list from the lists.py file

for fruit in fruits:
    print(fruit)

# this will print each fruit in the list.

word = "hello"

vowels = "aeiou"
vowels_count = 0

for letter in word:
    if letter in vowels:
        vowels_count += 1

## print(f"There are {vowels_count} vowels in the word '{word}'.")

# this will count the number of vowels in a word. This uses an if statement. They are self-explanatory.