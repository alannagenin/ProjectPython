#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:31:50 2020

@author: alanna genin
"""

import csv
from random import choice
from collections import Counter


#open the file with the words
with open("english-common-words.csv") as csvfile:
    words = csv.reader(csvfile, delimiter=",")
    words = [",".join(word) for word in words] # put words in a list
    words = [word for word in words if len(word) > 2] # select only words > 2 letters


# choose randomly a word
def choose_word(words):
    word = choice(words)
    return word.upper()


# print as many _ as letters in the word
def start(word):
    """
    >>> start('hello_world')
    _ _ _ _ _ _ _ _ _ _ _  
    """
    underscore = ''
    for i in range(len(word)):
        underscore += '_ '
    return(underscore)


# instantiate the word, guesses and tries
word = choose_word(words)
# print(word)


state = {
    "max": len(word) + 5,
    "remaining": len(word) + 5,
    "guesses": "",
    "goodguesses": "",
    "failed": 0,
    "solution": word
}


#if user makes an error
def error(character):
    if not character.isalpha():
        print("Enter only letters, no numbers.\n")
        return True
     
    elif len(character) > 1:
        print("Enter only a single letter.\n")
        return True
    
    elif character in state["guesses"] or character in state["goodguesses"]:
        print("You have already guessed that letter.\n") 
        #state["goodguesses"] -= (word.count(character))*character
        return True
    
    elif character == " ":
        print("This is a space, not a letter.\n")
        return True
    
    else:
        return False


#print the guesses and _ left
def output(guessed, solution):
    """
    >>> output('E', 'DESCARTES')
    _ E _ _ _ _ _ E _ 
    """
    #No quotes because you print and don't return
    for letter in solution:
        if letter in guessed:
            print(letter, end="", sep=" ")
        else:
            print(" _ ", end="", sep=" ")
    print()


#print the letters guessed
def fail(guessed):
    print("Letters guessed:", end=" ")
    for letter in guessed:
        print(letter, sep=" ", end="-")
    #print()


#main loop
def play(character, word):
    
    #decrease the number of tries left
    state["remaining"] -= 1
    
    #register the guesses
    state["guesses"] += character
    
    #print the propositions
    output(state["guesses"], state["solution"])
       
    #stop if no more tries remaining
    if state["remaining"] <= 0:
        return False
    
    #if the character is not found return True
    if character not in word:
        state["failed"] += 1
        return True
    
    #if the character is found return True : 
    elif character in word:
        state["goodguesses"] += (word.count(character))*character
        if Counter(state["goodguesses"]) == Counter(word):
            return False    
    return True


def print_play(character, word):
    #stop if no more tries remaining
    if state["remaining"] <= 0:
        print("\nYou lose, you used your ", state["max"]," tries, you failed ",
              state["failed"], " times.\nMy word was ", state["solution"],".",sep="")
    
    if state["remaining"] != 0:
        #if the character is not found return True
        if character not in word:
            print("Wrong.", end="\n")
        
        #if the character is found return True : 
        elif character in word:
            #if all the letters are in the word return False
            if Counter(state["goodguesses"]) == Counter(word):
                print("\nYou win! \nMy word was ", state["solution"],".",sep="")



    



# ----------------------------------- Loop ------------------------------------
if __name__ == "__main__":
    print("This game is a hangman, try to guess my word.",
          "The word is randomly chosen in a list of 3000 most common words in English.",
          "To increase the difficulty only words with more than 3 letters are picked.",
          "You will have a number of tries depending on the length of the word.")

    print("\n-------------- Your propositions -------------- ")
    print("\nYou have", state["remaining"], "tries to guess : ", start(word), sep=" ")

    while True:

        #print all the guessed letters
        if state["max"] != state["remaining"]:
            fail(state["guesses"])
        
        #play
        char = str(input("Proposition : "))
        
        #while error return to the begining of the loop
        if error(char):
            continue #ignore la suite d'une boucle             
    
        
        res = play(char.upper(), state["solution"])
        print_play(char.upper(), state["solution"])
        
        #continue or break the loop
        if res:
            print("\nYou have ", state["remaining"], " tries remaining.", end="\n", sep="")
        else:
            # stop the game if false (no more tries or word found)
            break
