import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem6 import solution

class Test6(unittest.TestCase):
    def test_6(self):
        df = pd.read_csv(r'../housing.csv')
        seed = 9
        self.assertEqual(solution(df, seed), 0.35)

if __name__ == '__main__':
    unittest.main()