import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem5 import solution

class Test5(unittest.TestCase):
    def test_5(self):
        df = pd.read_csv(r'../housing.csv')
        seeds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(solution(df, seeds), 0.005)

if __name__ == '__main__':
    unittest.main()