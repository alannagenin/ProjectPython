#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:25:34 2020

@author: alanna genin
"""

from random import randint

print("The aim of the game is too find a integer between two numbers that you choose. I will give you clues to find my number.")
print("\n----------------- Min and max ----------------- ", end='')


#-------------------------------- Min and max --------------------------------   

lower_boundary, upper_boundary = int(input("Min : ")), int(input("Max : "))

state = {"max": 5,
         "remaining": 5 ,
         "solution": randint(lower_boundary, upper_boundary)}

if upper_boundary - lower_boundary >= 1000:
    state["max"] = state["remaining"] = randint(12, 15)
elif upper_boundary - lower_boundary >= 500:
    state["max"] = state["remaining"] = 10
elif upper_boundary - lower_boundary >= 100:
    state["max"] = state["remaining"] = randint(6,7)

#-------------------------------- Process --------------------------------   

def process(number, state):
    #decrease the number of tries
    state["remaining"] -= 1 
    
    #stop the game if there's no more moves left
    if state["remaining"] == 0 and number != state["solution"]:
        print("\nYou loose, you used your ", state["max"], " tries. \nMy number was ", state["solution"], ".", sep='')
        return False
    
    #stop if number found
    if number == state["solution"]:
        if state["max"] - state["remaining"] == 1 :
            print("You win in ", state["max"] - state["remaining"], " try.", sep='')
        else:
            print("You win in ", state["max"] - state["remaining"], " tries.", sep='')
        return False
     
    #too big
    if number > state["solution"]:
        print("Too big")
        return True
    
    #too small
    if number < state["solution"]:
        print("Too small")
        return True
    

#-------------------------------- Loop --------------------------------    

print("\n-------------- Your propositions -------------- ")
print("\nYou have", state["remaining"], "tries to guess my number.", sep=" ")
while True:
    number = int(input("Proposition : "))
    while number < lower_boundary or number > upper_boundary:
        number = int(input("Error, choose another number : "))
        print(end='')
    res = process(number, state)
           
    if res:
        print("\nYou have ", state["remaining"], " tries remaining.", end='', sep='')
    else :
        #stop the game if false (no more tries or number found)
        break