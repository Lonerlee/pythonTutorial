from bs4 import BeautifulSoup
import requests

https = "https://"

urlDefault = "www.google.com"
decide = "Y"

class Decision:
  def __init__(self, decide):
    self.decide = decide

  def myfunc(self):
    

decide = input("Do you want to use your own page or do you want to use default one [" + urlDefault + "]? Type Y or N - ")

urlDefault = input("Type in any URL and it will provide you with a page title - https://")

page = requests.get(https + urlDefault)
zupka = BeautifulSoup(page.text, 'html.parser')

pageTitle = []
for title in zupka.find_all('title'):
    pageTitle.append(title.text.strip())

print(pageTitle)
