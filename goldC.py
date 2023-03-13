import requests
import os

def getGoldAPI():
  token = os.environ['GOLD_TOKEN']

  headers = {
    'x-access-token': token,
  }

  response = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)

  if response.status_code != 200:
    print(response.status_code)
    print('Status - ERROR')
    sys.exit()

  print('Status - working')
  getDataJson = response.json()
  print('The price of ' + getDataJson['metal'] + ' is: ' + str(getDataJson['price']) + ' ' + getDataJson['currency'])
  print('Name of the exchange is ' + getDataJson['exchange'])
  
getGoldAPI()
