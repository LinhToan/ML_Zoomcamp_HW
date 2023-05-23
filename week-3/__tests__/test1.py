import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem1 import solution

class Test1(unittest.TestCase):
    def test_1(self):
        df = pd.read_csv(r'../housing.csv')
        self.assertEqual(solution(df), '<1h_ocean')

if __name__ == '__main__':
    unittest.main()