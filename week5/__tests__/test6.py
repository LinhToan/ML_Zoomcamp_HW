import requests

host = "creddit-approval-env.eba-pq3umzri.us-east-1.elasticbeanstalk.com "
url = f"http://{host}/problem6"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
response = requests.post(url, json=client).json()

print(response)
# returns a probability of 0.928