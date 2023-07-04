import sys
import unittest
import requests
sys.path.insert(0, '../')
from problem4 import solution

class Test4(unittest.TestCase):
    def test_4(self):
        model_file = '../model1.bin'
        dv_file = '../dv.bin'
        url = "http://localhost:9696/problem4"
        client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
        response = requests.post(url, json=client).json()
        self.assertEqual(solution(model_file, dv_file, client), 0.162)

if __name__ == '__main__':
    unittest.main()