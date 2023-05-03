import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem2 import solution

class Test2(unittest.TestCase):
    def test_2(self):
        df = pd.read_csv(r'../data.csv')
        self.assertEqual(solution(df), 11914)

if __name__ == '__main__':
    unittest.main()

