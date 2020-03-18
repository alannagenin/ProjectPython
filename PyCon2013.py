#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:37:34 2020

@author: alanna
"""

#tools to use : iter, partial
import collections
import doctest
from collections import namedtuple
import urllib
import threading

#help :
#code : https://github.com/JeffPaine/beautiful_idiomatic_python
#slides : https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1?slide=33
#video : https://www.youtube.com/watch?v=anrOzOapJ2E

# ------------ Transforming Code into Beautiful, Idiomatic Python ------------ 

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

#print(sorted(colors, cmp=compare_length))

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
print("\nSecond version to count :\n", d, sep='')

#More modern but doesn't work
d = collections.defaultdict(int)
for color in colors:
    d[color] += 1
print("\nThird version to count :\n", d, sep='')   

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
 
#---------------------------- Improving clarity ----------------------------
#Clarify function calls with keyword arguments   
#twitter_search('@obama', False, 20, True)
#twitter_search('@obama', retweets=False, numtweets=20, popular=True)
    
#Clarify multiple return values with named tuples
doctest.testmod()
# (0, 4)

doctest.testmod()
# TestResults(failed=0, attempted=4)

#name the tuple
TestResults = namedtuple('TestResults', ['failed', 'attempted'])

#unpacking sequences
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# A common approach / habit from other languages
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

#better : more readable and faster, easy change
fname, lname, age, email = p


#Updating multiple state variables
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t

#better
def fibonacci2(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y #simultaneous update

print("\nFibonacci")
fibonacci2(6)

#Simultaneous state updates and temporary variables
#tmp_x = x + dx * t
#tmp_y = y + dy * t
#The "influence" function here is just an example function
#tmp_dx = influence(m, x, y, dx, dy, partial='x')
#tmp_dy = influence(m, x, y, dx, dy, partial='y')
#x = tmp_x
#y = tmp_y
#dx = tmp_dx
#dy = tmp_dy

#better
#x, y, dx, dy = (x + dx * t,
#                y + dy * t,
#                influence(m, x, y, dx, dy, partial='x'),
#                influence(m, x, y, dx, dy, partial='y'))

#---------------------------- Concatenating strings ----------------------------


names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
    s += ', ' + name
print("\nNames :",s)

print("Names :", ', '.join(names))

#---------------------------- Updating sequences ----------------------------

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

del names[0]
names.pop(0)
names.insert(0, 'mark')
print("\nNames :",names)

#better
names = collections.deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])
# More efficient with collections.deque
del names[0]
names.popleft()
names.appendleft('mark')
print("Names :",names)



#------------------------- Decorators and Context Managers -------------------------
#Using decorators to factor-out administrative logic
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

#Better
#@cache
#def web_lookup2(url):
#    return urllib.urlopen(url).read()
    
#caching decorator
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

#------------------------- Factor-out temporary contexts -------------------------

#Saving the old, restoring the new
#old_context = getcontext().copy()
#getcontext().prec = 50
#print(Decimal(355) / Decimal(113))
#setcontext(old_context)
#
#Better and reusable
#with localcontext(Context(prec=50)):
#    print(Decimal(355) / Decimal(113))
    
#----------------------------------- Files -----------------------------------

#How to open and close files
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()

#Better
with open('data.txt') as f:
    data = f.read()
print("\nData :\n", data, sep='')

#----------------------------------- Locks -----------------------------------

# Make a lock
lock = threading.Lock()

print("\nOld-way to use a lock :")
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()

#Better
print("\nNew-way to use a lock :")
with lock:
    print('Critical section 1')
    print('Critical section 2')
    
    
#----------------------------------- List Comprehensions -----------------------------------    

result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print("\nSum of 1 to 10 squared :", sum(result))

#Better
#print([sum(i**2) for i in range(10)])
print("Sum of 1 to 10 squared :",sum([i**2 for i in range(10)]))
#without brackets
print("Sum of 1 to 10 squared :",sum(i**2 for i in range(10)))