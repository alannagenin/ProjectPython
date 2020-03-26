#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:45:51 2020

@author: alanna genin
"""

from Hangman import play
from unittest import TestCase

#testing
class GameTestCase(TestCase):
    def test_play_win(self):
        word = 'alanna'
        state = {
                "max": len(word) + 5,
                "remaining": len(word) + 5,
                "guesses": "",
                "goodguesses": "",
                "failed": 0,
                "solution": word
                }
        self.assertTrue(play('a', state["solution"]))
        
    def test_play_win_last_try(self):
        word = 'alanna'
        state = {
                "max": len(word) + 5,
                "remaining": 1,
                "guesses": "",
                "goodguesses": "",
                "failed": 0,
                "solution": word
                }
        self.assertTrue(play('a', state["solution"]))
        
    def test_play_win_last_letter(self):
        word = 'alanna'
        state = {
                "max": len(word) + 5,
                "remaining": 1,
                "guesses": "lane",
                "goodguesses": "lnn",
                "failed": 0,
                "solution": word
                }
        self.assertTrue(play('a', state["solution"]))
        
    def test_play_fail(self):
        word = 'alanna'
        state = {
                "max": len(word) + 5,
                "remaining": len(word) + 5,
                "guesses": "lann",
                "goodguesses": "lann",
                "failed": 0,
                "solution": word
                }
        self.assertTrue(play('e', state["solution"]))
        
    def test_play_remaining(self):
        word = 'alanna'
        state = {
                "max": len(word) + 5,
                "remaining": 0,
                "guesses": "lann",
                "goodguesses": "lann",
                "failed": 0,
                "solution": word
                }
        self.assertTrue(play('e', state["solution"]))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    import unittest
    unittest.main()
