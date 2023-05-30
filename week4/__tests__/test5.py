import sys
import unittest
import pandas as pd
from sklearn.model_selection import KFold
sys.path.insert(0, '../')
from problem5 import solution

class Test5(unittest.TestCase):
    def test_5(self):
        df = pd.read_csv(r'../AER_credit_card_data.csv')
        columns = ["reports", "age", "income", "share", "expenditure", "dependents", "months", "majorcards", "active", "owner", "selfemp"]
        kfold_split = KFold(n_splits=5, shuffle=True, random_state=1)
        self.assertEqual(solution(df, columns, kfold_split), 'The mean and std of the AUC across different folds are 0.996 +- 0.003')

if __name__ == '__main__':
    unittest.main()