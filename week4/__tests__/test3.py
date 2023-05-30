import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem3 import solution

class Test3(unittest.TestCase):
    def test_3(self):
        df = pd.read_csv(r'../AER_credit_card_data.csv')
        columns = ["reports", "age", "income", "share", "expenditure", "dependents", "months", "majorcards", "active", "owner", "selfemp"]
        self.assertEqual(solution(df, columns), 0.3)

if __name__ == '__main__':
    unittest.main()