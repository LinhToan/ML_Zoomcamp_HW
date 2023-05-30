import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem6 import solution

class Test6(unittest.TestCase):
    def test_6(self):
        df = pd.read_csv(r'../AER_credit_card_data.csv')
        columns = ["reports", "age", "income", "share", "expenditure", "dependents", "months", "majorcards", "active", "owner", "selfemp"]
        c_list = [0.01, 0.1, 1, 10]
        self.assertEqual(solution(df, c_list, columns), 'C=1 gives us a mean and std of 0.996 +- 0.003')

if __name__ == '__main__':
    unittest.main()