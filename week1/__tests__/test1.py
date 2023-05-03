import sys
import unittest
import numpy as np
sys.path.insert(0, '../')
from problem1 import solution

class Test1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(), '1.24.1')

if __name__ == '__main__':
    unittest.main()