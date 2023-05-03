import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem6 import solutionA, solutionB, solutionC
df = pd.read_csv(r'../data.csv')

class Test6(unittest.TestCase):
    def test_6A(self):
        self.assertEqual(solutionA(df), 6)

    def test_6B(self):
        self.assertEqual(solutionB(df), 4)

    def test_6C(self):
        self.assertEqual(solutionC(df), 6)

if __name__ == '__main__':
    unittest.main()
