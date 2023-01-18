import requests, re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

x = requests.get("https://api.dane.gov.pl/1.4/resources/44385,liczba-studentow-z-obywatelstwem-ukrainskim-stan-na-09012023?lang=pl")
works = x.json()

print('Title:')
print(works['data']['attributes']['title'])

print('Description:')
print(cleanhtml(works['data']['attributes']['description']))

print('Language:')
print(works['meta']['params']['lang'])
