#functions are reusable pieces of code that can be called multiple times

def greet_player(name):
    print(f"Hello, {name}! Welcome to the game.")

#this function takes a player's name as an argument and prints a greeting message.

greet_player("Wesley")

greet_player("Logan")

greet_player("Gage")

# see how we can call the same function with different names?

#you can also return values from functions.

def calculate_damage(attack, defense):
    damage = attack - defense
    if damage < 0:
        damage = 0
    return damage

# this function calculates the damage dealt based on attack and defense values.

player_attack = 50
enemy_defense = 20

damage_dealt = calculate_damage(player_attack, enemy_defense)

## print(f"Player dealt {damage_dealt} damage to the enemy.")

# most of the time, functions are used to perform the same action over and over again, but with different inputs.
# this makes your code cleaner and easier to read.

# sometimes, functions are defined in separate files and imported into your main program.

# from functions import *

# the asterisk (*) imports all functions from the functions.py file.
# this file is called functions.py, so this doesn't do anything, but if there was a function in lists.py, you could import it. You can also import variables and lists from other files too:

from lists import fruits

# functions can be combined with loops and conditionals to create more complex behavior.

word_list = ["glimmer", "vault", "serene", "fracture", "mirth", "quartz", "bristle", "ember", "swoop", "drizzle", "tundra", "cradle", "wisp", "knoll", "plume", "thresh", "gravel", "latch", "spool", "rift"]

def count_vowels(list):
    vowels = "aeiou"
    count = 0
    for word in list:
        for letter in word:
            if letter in vowels:
                count += 1
    return count

## print(f"There are {count_vowels(word_list)} vowels in the word list.")

# I can also do it with the fruits list:

## print(f"There are {count_vowels(fruits)} vowels in the fruits list.")