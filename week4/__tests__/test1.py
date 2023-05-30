import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem1 import solution

class Test1(unittest.TestCase):
    def test_1(self):
        df = pd.read_csv(r'../AER_credit_card_data.csv')
        tolerance = 0.5
        self.assertEqual(solution(df, tolerance), 'Out of the choices given, share yields the highest AUC score with 0.989')

if __name__ == '__main__':
    unittest.main()