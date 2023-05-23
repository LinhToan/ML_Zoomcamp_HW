import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem2 import solution

class Test2(unittest.TestCase):
    def test_2(self):
        df = pd.read_csv(r'../housing.csv')
        self.assertEqual(solution(df), 'The features with the highest correlation are total bedrooms and households with a correlation value of 0.974')

if __name__ == '__main__':
    unittest.main()