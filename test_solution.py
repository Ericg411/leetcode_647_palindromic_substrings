import unittest
from solution import Solution

class TestPalindromicSubstrings(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countSubstrings("abc"), 3)
        
    def test_example_2(self):
        self.assertEqual(self.solution.countSubstrings("aaa"), 6)

    def test_single_char(self):
        self.assertEqual(self.solution.countSubstrings("a"), 1)

    def test_empty_string(self):
        self.assertEqual(self.solution.countSubstrings(""), 0)

    def test_palindromic_string(self):
        self.assertEqual(self.solution.countSubstrings("racecar"), 10)

if __name__ == '__main__':
    unittest.main()
