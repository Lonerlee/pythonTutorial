import requests, re

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

x = requests.get("https://api.dane.gov.pl/1.4/resources/43547,wykaz-publikacji-naukowych-i-specjalistycznych-cnbop-pib-dane-za-2022-r?lang=pl")
works = x.json()

typeIn = input('Type in what you want to know about this data. Commands are - title, time, desc, lang - ')

class getTheData:
  if typeIn == 'title':
    print('Title:')
    print(works['data']['attributes']['title'])
  elif typeIn == 'time':
    print('Time of verification:')
    print(works['data']['attributes']['verified'])
  elif typeIn == 'desc':
    print('Description:')
    print(cleanhtml(works['data']['attributes']['description']))
  elif typeIn == 'lang':
    print('Language:')
    print(works['meta']['params']['lang'])
  else:
    print('Unknown command.')

gtd = getTheData()

gtd