import sys
import unittest
import pandas as pd
sys.path.insert(0, '../')
from problem3 import solution

class Test3(unittest.TestCase):
    def test_3(self):
        df = pd.read_csv(r'../data.csv')
<<<<<<< HEAD
        self.assertEqual('Chevrolet' in solution(df), True)
        self.assertEqual('Ford' in solution(df), True)
        self.assertEqual('Volkswagen' in solution(df), True)
        self.assertEqual('Honda' in solution(df), False)
        self.assertEqual('Toyota' in solution(df), False)
        self.assertEqual('Audi' in solution(df), False)

if __name__ == '__main__':
    unittest.main()
=======
        self.assertEqual(solution(df), df.Make.value_counts().head(3).to_dict())

if __name__ == '__main__':
    unittest.main()
>>>>>>> main
