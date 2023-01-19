import requests, re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

x = requests.get("https://api.dane.gov.pl/1.4/resources/43547,wykaz-publikacji-naukowych-i-specjalistycznych-cnbop-pib-dane-za-2022-r?lang=pl")
works = x.json()

print('Title:')
print(works['data']['attributes']['title'])

print('Time of verification:')
print(works['data']['attributes']['verified'])

print('Description:')
print(cleanhtml(works['data']['attributes']['description']))

print('Language:')
print(works['meta']['params']['lang'])
