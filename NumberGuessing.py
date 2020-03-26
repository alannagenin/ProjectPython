#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:25:34 2020

@author: alanna genin
"""

from random import randint


#-------------------------------- Min and max ---------------------------------   

def boundaries():
    print("\n----------------- Min and max ----------------- ")
    lower_boundary, upper_boundary = int(input("Min : ")), int(input("Max : "))
    return lower_boundary, upper_boundary

def create_status(lower_boundary, upper_boundary):
    state = {"max": 5,
         "remaining": 5 ,
         "solution": randint(lower_boundary, upper_boundary)}
    
    #give more tries
    if upper_boundary - lower_boundary >= 1000:
        state["max"] = state["remaining"] = randint(12, 15)
    elif upper_boundary - lower_boundary >= 500:
        state["max"] = state["remaining"] = randint(7, 12)
    elif upper_boundary - lower_boundary >= 100:
        state["max"] = state["remaining"] = randint(6,7)
    
    return state


#----------------------------------- Number -----------------------------------

def number_input():
    number = int(input("Proposition : "))
    
    #testing is the number in between the two boundaries
    while number < lower_boundary or number > upper_boundary:
        number = int(input("Error, choose another number : "))
        print(end='')
        # if print() then it jumps two lines but I want only one line of separation

    return number
        

#---------------------------------- Process -----------------------------------   

def process(number, state):
    #decrease the number of tries
    state["remaining"] -= 1 
    
    #stop the game if there's no more moves left
    if state["remaining"] == 0 and number != state["solution"]:
        return False
    
    #stop if number found
    if number == state["solution"]:
        return False
     
    #too big
    if number > state["solution"]:
        return True
    
    #too small
    if number < state["solution"]:
        return True


def print_process(number, state):
    #stop the game if there's no more moves left
    if state["remaining"] == 0 and number != state["solution"]:
        print("\nYou lose, you used your ", state["max"], " tries. \nMy number was ", state["solution"], ".", sep='')

    #stop if number found
    if number == state["solution"]:
        if state["max"] - state["remaining"] == 1 :
            print("You win in ", state["max"] - state["remaining"], " try.", sep='')
        else:
            print("You win in ", state["max"] - state["remaining"], " tries.", sep='')

    if state["remaining"] != 0:
        #too big
        if number > state["solution"]:
            print("Too big")
    
        #too small
        if number < state["solution"]:
            print("Too small")
    

#------------------------------------ Loop ------------------------------------    

if __name__ == '__main__' :
    print("The aim of the game is too find a integer between two numbers that you choose.",
          "I will give you clues to find my number.")
    
    #Setting up the game
    lower_boundary, upper_boundary = boundaries()
    state = create_status(lower_boundary, upper_boundary)
    print("\nYou have", state["remaining"], "tries to guess my number.", sep=" ")
    
    print("\n-------------- Your propositions -------------- ")
    while True: 
        #propositions
        number = number_input()
        res = process(number, state)
        print_process(number, state)
        
        #contiunue or stop guessing
        if res:
            print("\nYou have ", state["remaining"], " tries remaining.", end='', sep='')
        else :
            #stop the game if false (no more tries or number found)
            break

