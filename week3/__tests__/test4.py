import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem4 import solution

class Test4(unittest.TestCase):
    def test_4(self):
        df = pd.read_csv(r'../housing.csv')
        self.assertEqual(solution(df), 0.84)

if __name__ == '__main__':
    unittest.main()