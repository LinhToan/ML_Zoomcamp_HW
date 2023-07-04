# To run this test, use `pipenv shell` and 
# then `gunicorn --bind 0.0.0.0:9696 problem4:app`, then finally run test4.py
import requests

url = "http://localhost:9696/problem4"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
response = requests.post(url, json=client).json()

print(response)
# returns a probability of 0.928