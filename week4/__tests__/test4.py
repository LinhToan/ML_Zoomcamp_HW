import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem4 import solution

class Test4(unittest.TestCase):
    def test_4(self):
        df = pd.read_csv(r'../AER_credit_card_data.csv')
        columns = ["reports", "age", "income", "share", "expenditure", "dependents", "months", "majorcards", "active", "owner", "selfemp"]
        self.assertEqual(solution(df, columns), 'A threshold of 0.4 yields the highest F1 score with 0.983')

if __name__ == '__main__':
    unittest.main()