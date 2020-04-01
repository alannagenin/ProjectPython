# Project in Python

The aim of this project is to code in Python 3 several games that we all know such as hangman or guessing a number between two boundaries. To that extent, we will use dictionnaries, tests, and so on.

Games :
- Guessing a number between two boundaries
- Hangman
- Simulating gaussian curves

## Guessing numbers

Steps 
1. User chooses two boundaries (lower and upper)
2. The computer chooses randomly a number between those two boundaries
3. Guess one number
4. Tell if too small or too big
5. Loop again

The file `english-common-words.csv`  shows the 3000 most used words in English. We will use it to randomly choose a word.

## Hangman

Steps 
1. The computer chooses randomly a word
2. Guess one letter
3. Tell if True or False
4. Loop again

## Gaussian

Simulate gaussian samples by asking to the user the number of samples he wants.

## Testing

Finally, we did somes tests to know if our functions are well defined. To that extend, unit tests are performed using the module [unittest](https://docs.python.org/3/library/unittest.html).
 
```python
#importing
from unittest import TestCase

#testing
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    import unittest
    unittest.main()
```

## Nota Bene
Files starting by `PyCon__.py` are codes coming from lectures of Python experts during the PyCon in 2013 or 2015.

