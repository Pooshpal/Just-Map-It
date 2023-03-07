import requests

url = 'http://localhost:5000/api'
payload = {'key': 'value'}
headers = {'content-type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print('Error:', response.text)
