import requests
import os

token = os.environ['GOLD_TOKEN']

headers = {
    'x-access-token': token,
}

response = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)

if response.status_code == 200:
    print('ok')
else:
    print(response.status_code)