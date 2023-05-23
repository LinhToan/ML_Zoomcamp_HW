import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem5 import solution

class Test5(unittest.TestCase):
    def test_5(self):
        df = pd.read_csv(r'../housing.csv')
        self.assertEqual(solution(df), 'The feature with the smallest difference is total_rooms with a difference of 0.0')

if __name__ == '__main__':
    unittest.main()