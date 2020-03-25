#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:31:50 2020

@author: alanna genin
"""

import csv
from random import choice #randint
from collections import Counter

#open the file with the words
with open("english-common-words.csv") as csvfile:
    words = csv.reader(csvfile, delimiter=",")
    words = [",".join(word) for word in words] # put words in a list
    words = [word for word in words if len(word) > 2] # select only words > 2 letters

# choose randomly a word
def choose_word(words):
    # word = words[randint(0, len(words))]
    word = choice(words)
    return word.upper()

word = choose_word(words)
#print(word)

# print as many _ as letters in the word
def start(word):
    """
    >>> start('hello_world')
    None
    """
    underscore = ''
    for i in range(len(word)):
        underscore += '_ '
    return(underscore)

# tries
state = {
    "max": len(word) + 3,
    "remaining": len(word) + 3,
    "guesses": "",
    "failed": 0,
    "solution": word,
}

#def error(character):
#    if not character.isalpha():
#        print("Enter only a letter")
#    elif len(character) > 1:
#        print("Enter only a single letter")
#    elif character in state["guesses"]:
#        print('You have already guessed that letter') 
#    return False


def output(guessed, solution):
    """
    >>> output('des', 'descartes')
    des_____s

    #No quotes because you print and don't return
    """
    for letter in solution:
        if letter in guessed:
            print(letter, end="", sep=" ")
        else:
            print(" _ ", end="", sep=" ")
    print()


def play(character, word):
    #error(character)
    state["remaining"] -= 1
    state["guesses"] += character
    
    #print the propositions
    output(state["guesses"], state["solution"])
    
    #if all the letters are in the word return False
    if Counter(state["guesses"]) == Counter(word):
        print("\nYou win! \nMy word was ", state["solution"],".",sep="")
        return False
    
    #stop if no more tries remaining
    if state["remaining"] <= 0:
        print("\nYou lose, you used your ", state["max"]," tries. \nMy word was ",
            state["solution"],".",sep="")
        return False
    
    #if the character is not found return True
    if character not in word:
        print("Wrong. You have", state["remaining"], "more guesses.")
        state["failed"] += 1
        return True

    #if the character is found return True
    elif character in word:
        if word.count(character) > 1:
            state["guesses"] = word.count(character)*character
    return True


    



# ----------------------------------- Loop ------------------------------------
if __name__ == "__main__":
    print("This game is a hangman, try to guess my word.")

    print("\n-------------- Your propositions -------------- ")
    print("\nYou have", state["remaining"], "tries to guess : ", start(word), sep=" ")

    while True:
        char = str(input("Proposition : "))
        res = play(char.upper(), state["solution"])
        if res:
            print("\nYou have ", state["remaining"], " tries remaining.", end="", sep="")
        else:
            # stop the game if false (no more tries or word found)
            break
