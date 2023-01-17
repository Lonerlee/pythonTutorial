import requests, re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

x = requests.get("https://api.dane.gov.pl/1.4/datasets/1434,obligacje-skarbowe-1?lang=pl")
works = x.json()

print('Title:')
print(works['data']['attributes']['category']['title'])

print('Description:')
print(cleanhtml(works['data']['attributes']['notes']))

print('License:')
print(works['data']['attributes']['license_name'])
