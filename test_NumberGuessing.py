from NumberGuessing import process
from unittest import TestCase


class GameTestCase(TestCase):
    def test_win(self):            
        solution = 6
        state = {
                 'max': 5,
                 'remaining': 2,
                 'solution': solution
                 }
        self.assertFalse(process(6, state))
    
    def test_perfect_win(self):
        solution = 10
        state = {
            "max": 5,
            "remaining": 5,
            "solution": solution,
        }
        self.assertFalse(process(solution, state))
        
    def test_lose(self):
        solution = 10
        state = {
            "max": 5,
            "remaining": 5,
            "solution": solution,
        }
        self.assertTrue(process(solution + 1, state))

#    def test_winning(self):
#        solution = 10
#        status = {
#            "max": 5,
#            "remaining": 5,
#            "solution": solution,
#        }
#
#        for number, expected in [[3,4,5], [True, True, False]]:
#            result = process(number, status)
#        
#        self.assertEqual(result, expected, f'Error for {number}: {result} != {expected}')
#    
#    def test_lose(self):
#        solution = 10
#        state = {
#            "max": 5,
#            "remaining": 5,
#            "solution": solution,
#        }
#        user_input = state["solution"] - 1
#        self.assertFalse(process(state, user_input))
#
#    def test_lose_retry_smaller(self):
#        solution = 10
#        state = {
#            "max": solution + 1,
#            "min": solution - 1,
#            "remaining": 2,
#            "solution": solution,
#        }
#        user_input = state["min"]
#        self.assertEqual("smaller", process(state, user_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    import unittest
    unittest.main()