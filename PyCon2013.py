#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:37:34 2020

@author: alanna
"""

#tools to use : iter, partial

#Looping integers
print("Square : ")
for i in [0, 1, 2, 3, 4, 5, 6]:
   print(i**2)

#better 
print("\nBetter version :")   
for i in range(7):
    print(i**2)

#better but ugly --> doesn't exists anymore
#for i in xrange(7):
#    print(i**2)
    
#Looping over a collection    
print("\nColors :")
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(colors[i])
    
#better and faster
print("\nBetter version for colors :")
for color in colors:
    print(color)

print("\nBackwards :")  
#Looping backwards
#horrific version
for i in range(len(colors)-1, -1, -1):
    print(colors[i])    

#better way
print("\nBetter and faster way backwards :")
for color in reversed(colors):
    print(color)
    
#Looping over a collection and indices
print("\nColors and indices :") 
for i in range(len(colors)):
    print(i, '-->', colors[i])

#fast, beautiful and readable
print("\nMuch better for colors and indices :")
for i, color in enumerate(colors):
    print(i, '-->', colors[i])
       
#looping over two collections
names = ['Raymond', 'Tom', 'Rachel']
colors = ['red', 'green', 'blue', 'yellow']

print("\nLooping over two collections : ")
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])

#far more better
print("\nUsing zip :")
for name, color in zip(names, colors):
    print(name, '-->', color)
    
#doesn't work
#print("\nUsing izip :")
#for name, color in izip(names, colors):
#    print(name, '-->', color)

#Looping in sorted order
print("\nLooping in sorted order : ")
for color in sorted(colors):
    print(color)

#Looping in sorted order and reversed
print("\nLooping in sorted order and reversed : ")
for color in sorted(colors, reverse=True):
    print(color)

#custom sort order --> doesn't work 
print("\nCustom sort order : ")
def compare_length(c1, c2):
    if len(c1) < len(c2) :
        return -1
    if len(c1) > len(c2) :
        return 1
    return 0

print(sorted(colors, cmp=compare_length))

#sort by the length : better and faster
print(sorted(colors, key=len))


#call a function until a sentinel value
#blocks = []
#while True:
#    block = f.read(32)
#    if block == '':
#        break
#    blocks.append(block)
#    
#blocks = []
#for block in inter(partial(f.read, 32), ''):
#    blocks.append(block)

#distinguishing multiple exit points
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
        if not found:
            return -1
        return i

#better version
def find2(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

#---------------------------- dictionnary skills ----------------------------
print("\n--- Dictionnaries ---")
#looping  over dictionnaries skills
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red', 'tom':'purple'}

for k in d:
    print(k)

for k in d.keys():
    if k.startswith('a'):
        del d[k]

print("\nDictionnary after deleting elements starting with 'k' ")
d = {k: d[k] for k in d if not k.startswith('r')}
print(d)


#Looping over dictionary keys and values
# Not very fast, has to re-hash every key and do a lookup on it
print("\nLoop keys and values")
for k in d:
    print(k, '--->', d[k])

print()
# Makes a big huge list
for k, v in d.items():
    print(k, '--->', v)


#better but not available in Python 3 anymore 
#for k, v in d.iteritems():
#    print(k, '--->', v)

#Construct a dictionary from pairs
print("\nConstructing a dictionary from pairs")
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

#d = dict(izip(names, colors)) : older version
d = dict(zip(names, colors))#for Python 3
print(d)
# result : {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#Count with a dictionnary
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
    if color not in d:#it can fail if there's not the key
        d[color] = 0
    d[color] += 1
print("\nCounting to make a new dictionnary :\n", d, sep='')

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1#doesn't fail
print("\nOther version to count :\n", d, sep='')

#More modern but doesn't work
#d = collections.defaultdict(int)
#for color in colors:
#    d[color] += 1
    
#Making groups
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# In this example, we're grouping by name length
d = {}
for name in names:
    key = len(name)#we can change the key for example name[0:] groups by the first letter
    if key not in d:
        d[key] = []
    d[key].append(name)
print("\nGrouping by length :\n", d, sep='')
#6 lines and slow

d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print("\nAlso grouping by length :\n", d, sep='')

#modern way
#d = collections.defaultdict(list)
#for name in names:
#    key = len(name)
#    d[key].append(name)
#4 lines and fast


#popitem atomic
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
print("\nPopitems :")
while d:
    key, value = d.popitem()#emoves item
    print(key, '-->', value)
    
    
#Linking dictionaries together
#defaults = {'color': 'red', 'user': 'guest'}
#parser = argparse.ArgumentParser()
#parser.add_argument('-u', '--user')
#parser.add_argument('-c', '--color')
#namespace = parser.parse_args([])
#command_line_args = {k:v for k, v in vars(namespace).items() if v}

#copies too much data
#d = defaults.copy()
#d.update(os.environ)
#d.update(command_line_args)
 
#faster
#d = ChainMap(command_line_args, os.environ, defaults)