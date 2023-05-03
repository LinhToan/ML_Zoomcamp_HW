import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
<<<<<<< HEAD
from problem6 import solutionA, solutionB, solutionC
df = pd.read_csv(r'../data.csv')

class Test6(unittest.TestCase):
    def test_6A(self):
        self.assertEqual(solutionA(df), 6)

    def test_6B(self):
        self.assertEqual(solutionB(df), 4)

    def test_6C(self):
        self.assertEqual(solutionC(df), 6)
=======
from problem6 import solution1, solution2, solution3, solution4
df = pd.read_csv(r'../data.csv')
class Test6(unittest.TestCase):
    
    def test_6(self):
        self.assertEqual(solution1(df), 6)
    
    def test_6b(self):
        self.assertEqual(solution2(df), 4)

    def test_6c(self):
        self.assertEqual(solution3(df), 0)
    
    def test_6d(self):
        self.assertEqual(solution4(df), 6)
>>>>>>> main

if __name__ == '__main__':
    unittest.main()