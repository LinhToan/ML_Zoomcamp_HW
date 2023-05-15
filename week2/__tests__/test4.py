import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem4 import solution

class Test4(unittest.TestCase):
    def test_4(self):
        df = pd.read_csv(r'../housing.csv')
        r_list = [0, 0.000001, 0.0001, 0.001, 0.01, 0.1, 1, 5, 10]
        self.assertEqual(solution(df, r_list), 'The smallest RMSE is 0.33 with r = 0')

if __name__ == '__main__':
    unittest.main()