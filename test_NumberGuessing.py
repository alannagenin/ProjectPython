from NumberGuessing import process
from unittest import TestCase


class GameTestCase(TestCase):
    def test_perfect_win(self):
        solution = 10
        state = {
            "max": solution + 1,
            "min": solution - 1,
            "remaining": 5,
            "solution": 10,
        }
        self.assertEqual("win", process(solution, state))

    def test_lose(self):
        solution = 10
        state = {
            "max": solution + 1,
            "min": solution - 1,
            "remaining": 1,
            "solution": solution,
        }
        user_input = state["min"]
        self.assertEqual("lose", process(state, user_input))

    def test_lose_retry_smaller(self):
        solution = 10
        state = {
            "max": solution + 1,
            "min": solution - 1,
            "remaining": 2,
            "solution": solution,
        }
        user_input = state["min"]
        self.assertEqual("smaller", process(state, user_input))
