from bs4 import BeautifulSoup
import requests

https = "https://"

urlDefault = "www.google.com"
decide = "Y"

class Decision:
  def myfunc(self):
    decide = "Y"
    i = 0
    while i < 1:
      decide = input("Type Y if you want to use your own page or N if you want to use default one [" + urlDefault + "]? - ")
      if decide == "Y" or decide == "y":
        return input("Type in any URL and it will provide you with a page title - https://")
        i += 1
      elif decide == "N" or decide == "n":
        return "www.google.com"
        i += 1
      else :
        print("Error. Try to type single letter Y or N.")


d1 = Decision()

urlDefault = d1.myfunc()

page = requests.get(https + urlDefault)
zupka = BeautifulSoup(page.text, 'html.parser')

pageTitle = []
for title in zupka.find_all('title'):
    pageTitle.append(title.text.strip())

print(pageTitle)
