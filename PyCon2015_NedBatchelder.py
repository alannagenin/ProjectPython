#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:09:00 2020

@author: alanna
"""
#Ned Batchelder - Facts and Myths about Python names and values
#video : https://www.youtube.com/watch?v=_AEJHKGk9ns
#slides : https://nedbatchelder.com/text/names1/names1.html#17

#Names refer to values
x = 23
print(x)

#Many names can refer to one value
x = 23
y = x

#Names are reassigned independently
x = 23
y = x
x = 12

#Values live until no references
x = "hello"
x = "world"

#Assignment never copies data --> 2 assignments to the same data
nums = [1, 2, 3]
other = nums

#Changes are visible through all names
nums = [1, 2, 3]
other = nums
nums.append(4)
print(other)# [1, 2, 3, 4] !!!

#Immutable values can't alias (values that cannot be changed)
#Immutable types: ints, floats, strings, tuples
x = "hello"
y = x
x = x + " there"

#"Change" is unclear
x = 2
y = 3
x = x + 1
nums.append(7)
nums = nums + [7]

#Assignment variants
x += y
x = x + y           # conceptually
#x = x.__iadd__(y)   # actually!

# pseudo-code!
class List:
    def __iadd__(self, other):
        self.extend(other)
        return self
    
# These are the same:
nums += [4, 5]#rebinding
nums.extend([4, 5]); nums = nums

#References can be more than just names
#List elements are references
nums = [1, 2, 3]
x = nums[1]

#Lots of things are references
#my_obj.attr = 23
#my_dict[key] = 24
#my_list[index] = 25
#my_obj.attr[key][index].attr = "etc, etc"

#Lots of things are assignments
#All of these assign to X
#X = ...
#for X in ...
#class X(...):
#def X(...):
#def fn(X):
#import X
#from ... import X
#except ... as X:
#with ... as X:

#For loops
for x in sequence:
    something(x)

#what is really done
x = sequence[0]
something(x)
x = sequence[1]
something(x)

#For loops
nums = [1, 2, 3]
for x in nums:          # x = nums[0] ...
    x = x * 10
print(nums)             # [1, 2, 3]   :(

#Function arguments are assignments
def func(x):    # x = num
    print(x)
    return

#does the same thing 
num = 17
func(num)       # x = num
print(num)

def append_twice(a_list, val):
    a_list.append(val)
    a_list.append(val)
    return
 
nums = [1, 2, 3]
append_twice(nums, 7)
print(nums)         # [1, 2, 3, 7, 7]


def append_twice_bad(a_list, val):
    a_list = a_list + [val, val]
    return
 
nums = [1, 2, 3]
append_twice_bad(nums, 7)
print(nums)         # [1, 2, 3]

def append_twice_good(a_list, val):
    a_list = a_list + [val, val]
    return a_list
 
nums = [1, 2, 3]
nums = append_twice_good(nums, 7)
print(nums)         # [1, 2, 3, 7, 7]


#Three append_twice functions
def append_twice(a_list, val):
    """Mutates argument."""
    a_list.append(val)
    a_list.append(val)
    
def append_twice_bad(a_list, val):
    """Useless!"""
    a_list = a_list + [val, val]
    
def append_twice_good(a_list, val):
    """Returns new list."""
    a_list = a_list + [val, val]
    return a_list

#Dynamic typing
x = 12
x = "hello"
x = [1, 2, 3]
x[1] = "two"

#Making a 2D list:
board = [[0] * 8] * 8                # bad
board = [[0] * 8 for _ in range(8)]  # good
print(board)