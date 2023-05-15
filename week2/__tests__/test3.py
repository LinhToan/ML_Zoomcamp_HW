import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem3 import solution

class Test3(unittest.TestCase):
    def test_3(self):
        df = pd.read_csv(r'../housing.csv')
        self.assertEqual(solution(df), 0.330)

if __name__ == '__main__':
    unittest.main()