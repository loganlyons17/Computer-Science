import random as r
import sys
from colorama import Fore, init
init(autoreset=True)

words = []
hint = []
CHECK_list = []
secret_word = ""
guess = ""

def get_word():
    global secret_word
    with open("words.txt") as file:
        lines = file.readlines()
        for line in lines:
            words.append(line.strip())

    secret_word = r.choice(words)
    #print(secret_word)

def get_guess():
    global guess
    guess = ""
    print("-----------------")
    guess = input()
    if guess == "CHECK":
        print("-----------------")
        print(Fore.YELLOW+"".join(CHECK_list))
        get_guess()
        return
    if guess == "Papyrus":
        print("-----------------")
        print(Fore.BLUE+"Nyeh Heh Heh")
        get_guess()
        return
    if guess == "Hornet":
        print("-----------------")
        print(Fore.BLUE+"SHAW")
        get_guess()
        return
    if len(guess) != 5:
        print("-----------------")
        print(Fore.RED + "Invalid Length")
        get_guess()
    if guess not in words:
        print("-----------------")
        print(Fore.RED + "Word Not Recognized")
        get_guess()
    get_hints()

def get_hints():
    hint = []
    if secret_word == guess:
        print(Fore.GREEN + "=======================")
        print(Fore.GREEN + "You Win!")
        print(Fore.GREEN + "=======================")
        sys.exit()
    for index, letter in enumerate(guess):
        if letter == secret_word[int(index)]:
            hint.append(Fore.GREEN+letter)
        elif letter in secret_word:
            hint.append(Fore.YELLOW+letter)
            if letter not in CHECK_list:
                CHECK_list.append(letter)
        else:
            hint.append(Fore.RED+"#")
    
    print("-----------------")
    print("".join(hint))
    get_guess()
  
get_word()
get_guess()