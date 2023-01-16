import requests

x = requests.get("https://api.dane.gov.pl/1.4/resources/44218,raport-z-miesiecznej-dziaalnosci-poz-maj-2022?lang=pl")
works = x.json()

print(works['data']['attributes']['description'])