#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:31:50 2020

@author: alanna genin
"""

import csv
from random import randint

if __name__ == "__main__":
    print("This game is a hangman. Try to guess my word.")

with open("english-common-words.csv") as csvfile:
    words = csv.reader(csvfile, delimiter=",")
    words = [",".join(word) for word in words]  # put words in a list
    words = [word for word in words if len(word) > 2]  # select only words > 2 letters


# choose randomly a word
def choose_word(words):
    word = words[randint(0, len(words))]
    return word.upper()
    # This aleady exits, it's random.choice().


# return as many _ as letters in the word
def start(word):
    """
    >>> start('hello_world')
    None
    """
    # This does not returns
    for _ in word:
        # This iterates on every letter of the word, put the letter in the _ variable
        # if _ == '_': xxxxx
        # the _ variable is tricky be careful.
        # word.count('_')  is a better option.
        print("_", sep=" ", end=" ")


# No this does a print, it returns no

word = choose_word(words)
print(word)

# tries
state = {
    "max": len(word) + 5,
    "remaining": len(word) + 5,
    "guesses": "",
    "failed": 0,
    "solution": word,
}


def play(character, word):
    state["remaining"] -= 1

    if state["remaining"] == 0:
        print(
            "\nYou lose, you used your ",
            state["max"],
            " tries. \nMy number was ",
            state["solution"],
            ".",
            sep="",
        )
        return False

    elif character not in word:
        print("Wrong. You have", state["remaining"], "more guesses.")
        print("_", sep=" ", end=" ")
        state["failed"] += 1
        return True

    elif character in word:
        print(character, sep=" ", end=" ")
        return True


# hint: something
def output(guessed, solution):
    """
    >>> output('des', 'descartes')
    des_____s

    #No quotes because you print and don't return
    """
    for letter in solution:
        if letter in guessed:
            print(letter, end="")
        else:
            print("_", end="")


# you can also do


def output2(guessed, solution):
    """
    >>> output2('n', 'Bonjour')
    '__n____'
    >>> output2('b', 'Bonjour')
    'b______'

    #this will fail, fix the code so that it works

    """

    return "".join(letter if letter in guessed else "_" for letter in solution)


#
# -------------------------------- Loop --------------------------------
if __name__ == "__main__":
    print("\n-------------- Your propositions -------------- ")
    print("\nYou have", state["remaining"], "tries to guess : ", start(word), sep=" ")

    while True:
        char = str(input("Proposition : "))
        res = play(char.upper(), state["solution"])
        if res:
            print(
                "\nYou have ", state["remaining"], " tries remaining.", end="", sep=""
            )
        else:
            # stop the game if false (no more tries or number found)
            break
