#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:45:51 2020

@author: alanna
"""

from Hangman import play
from unittest import TestCase


class GameTestCase(TestCase):
    def test_play(self):
        word = 'alanna'
        state = {
                "max": len(word) + 3,
                "remaining": len(word) + 3,
                "guesses": "",
                "failed": 0,
                "solution": word
                }
        self.assertEqual('alanna', play('alanna', state["solution"]))