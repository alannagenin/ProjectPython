#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:04:49 2020

@author: alanna
"""
#Ned Batchelder - Loop Like A Native
#video : https://www.youtube.com/watch?v=EnSu9hHGq5o
#slides : https://nedbatchelder.com/text/iter/iter.html#37


#Iteration
my_list = [i for i in range(1,7)]
i = 0
while i < len(my_list):
    v = my_list[i]
    print(v)
    i += 1
print()

#better but not the best way
for i in range(len(my_list)):
    v = my_list[i]
    print(v)
print()

#better
for v in my_list:
    print(v)
print()    
    
#list --> elements
for e in [1, 2, 3, 4]:
    print(e)
print()

#strings --> characters
for c in "Hello":
    print(c)
print()

#dictionnaries --> key and values    
d = { 'a': 1,  'b': 2,  'c': 3 } 
for k in d:
    print(k)
print()

# Also:
for v in d.values():
    print(v)
print()
    
for k,v in d.items():
    print("Key:", k, "value:", v)
print()
 
#files --> lines
with open("data.txt") as f:
    for line in f:
        print(repr(line))
        
#Stdlib has interesting iterables
#for match in re.finditer(pattern, string):
        
#for root, dirs, files in os.walk('/some/dir'):
    #once for each sub-directory...
    #produce and iterable

#for num in itertools.count():
    #once for each integer... Infinite!

from itertools import chain, repeat, cycle
seq = chain(repeat(17, 3), cycle(range(4)))
#for num in seq: never endsq
    #print(num, sep=", ", end="")
    # 17, 17, 17, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, ...

#Other uses for iterables
iterable = [21, 42, 66]

new_list = list(iterable)
results = [x - 2 for x in iterable]
total = sum(iterable)
smallest = min(iterable)
largest = max(iterable)
combined = " ".join(str(iterable))#for strings
print()

#index
for i, v in enumerate(my_list):
    print(i, v)
    
names = ["Eiffel Tower", "Empire State", "Sears Tower"]
print("\n", list(enumerate(names)), sep='')

print("\nor\n", sep='')
for num, name in enumerate(names):
    print(num, name)
print()
    
#Iteration vs indexing
#Limited:
for i in range(len(my_list)):
    v = my_list[i]    # indexing!
    print(i, v)
print()

#More powerful:
for i, v in enumerate(iterable):
    print(i, v)
print()
#for linenum, line in enumerate(f, start=1):
    #...

#the other bad way
i = 0
for v in iterable:
    print(i, v)
    i += 1
print()  

#loop over two lists?
names = ["Eiffel Tower", "Empire State", "Sears Tower"]
heights = [324, 381, 442]
 
for i in range(len(names)):
    name = names[i]
    height = heights[i]
    print("%s: %s meters" % (name, height))
print()

#using zip
for name, height in zip(names, heights):
    print("%s: %s meters" % (name, height))
print()


names = ["Eiffel Tower", "Empire State", "Sears Tower"]
heights = [324, 381, 442]
print(dict(zip(names, heights)), '\n')
 
#powerful
tall_buildings = {
  "Empire State": 381, "Sears Tower": 442,
  "Burj Khalifa": 828, "Taipei 101": 509,
  }
print(max(tall_buildings.values()))
print(max(tall_buildings.items(), key=lambda b: b[1]))
print(max(tall_buildings, key=tall_buildings.get), '\n')

#Make your own iteration
nums = [88, 73, 92, 72, 40, 38, 25, 20, 90, 72]
for n in nums:
    if n % 2 == 0:
        print(n)
print()

def evens(stream):
    them = []
    for n in stream:
        if n % 2 == 0:
            them.append(n)
    return them
 
for n in evens(nums):
    print(n)
print()

def hello_world():
    yield "Hello"
    yield "world"

#Generators
for x in hello_world():
    print(x)
print()
   
#Evens generator
def evens(stream):
    for n in stream:
        if n % 2 == 0:
            yield n

for n in evens(nums):
    print(n)
print()

#Abstracting your iteration
#f = open("my_config.ini")
#for line in f:
#    line = line.strip()
#    if line.startswith('#'):
#        # A comment line, skip it.
#        continue
#    if not line:
#        # A blank line, skip it.
#        continue
# 
#    # An interesting line.
#    do_something(line)

#Your own generator
#def interesting_lines(f):
#    for line in f:
#        line = line.strip()
#        if line.startswith('#'):
#            continue
#        if not line:
#            continue
#        yield line

#with open("my_config.ini") as f:
#    for line in interesting_lines(f):
#        do_something(line)
 
#with open("my_other.dat") as f2:
#    for line in interesting_lines(f2):
#        do_something_else(line)


#Q:How do I break out of two loops?
#for row in range(height):
#    for col in range(width):
# 
#        value = spreadsheet.get_value(col, row)
#        do_something(value)
# 
#        if this_is_my_value(value):
#            break   # ← ???

#A:Make the double loop single
def range_2d(width, height):
    """Produce a stream of two-D coordinates."""
    for y in range(height):
        for x in range(width):
            yield x, y

#for col, row in range_2d(width, height):
#    value = spreadsheet.get_value(col, row)
#    do_something(value)
# 
#    if this_is_my_value(value):
#        break

#Better: iterate cells
#for cell in spreadsheet.cells():
#    value = cell.get_value()
#    do_something(value)
# 
#    if this_is_my_value(value):
#        break
 
#Low-level iteration           
#Iterable: produces an iterator
#Iterator: produces a stream of values

iterator = iter(iterable)  # iterable.__iter__()
value = next(iterator)     # iterator.next() or .__next__()
value = next(iterator)

#with open("blah.dat") as f:
#    # Read the first line
#    header_line = next(f)
# 
#    # Read the rest
#    for data_line in f:
#        # ...

#Making your object iterable
class ToDoList(object):
    def __init__(self):
        self.tasks = []
 
    def __iter__(self):
        return iter(self.tasks)
#todo = ToDoList()
#...
#for task in todo:
#    # ...


#__iter__ generators
class ToDoList2(object):
    def __init__(self):
        self.tasks = []
 
    def __iter__(self):
        for task in self.tasks:
            if not task.done:
                yield task
 
    def all(self):
        return iter(self.tasks)
 
    def done(self):
        return (t for t in self.tasks if t.done)