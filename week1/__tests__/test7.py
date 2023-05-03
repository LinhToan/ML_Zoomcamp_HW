import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem7 import solution

class Test7(unittest.TestCase):
<<<<<<< HEAD
=======
    
>>>>>>> main
    def test_7(self):
        df = pd.read_csv(r'../data.csv')
        self.assertEqual(solution(df), 4.595)

if __name__ == '__main__':
    unittest.main()