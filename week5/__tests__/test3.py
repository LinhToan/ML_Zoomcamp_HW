import sys
import unittest
sys.path.insert(0, '../')
from problem3 import solution

class Test3(unittest.TestCase):
    def test_3(self):
        client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
        model_file = 'model1.bin'
        dv_file = 'dv.bin'
        self.assertEqual(solution(model_file, dv_file, client), 0.162)

if __name__ == '__main__':
    unittest.main()