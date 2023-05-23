import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem6 import solution

class Test6(unittest.TestCase):
    def test_6(self):
        df = pd.read_csv(r'../housing.csv')
        self.assertEqual(solution(df), 'The smallest "a" value is 0 and gives us a RMSE of 0.517')

if __name__ == '__main__':
    unittest.main()