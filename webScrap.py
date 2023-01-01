from bs4 import BeautifulSoup
import requests

urlDefault = "https://www.youtube.com/watch?v=EOWP5Y7eErE"
urlDefault = input("Type in any URL and it will provide you with a page title (Make sure to add 'https://') - ")

page = requests.get(urlDefault)
zupka = BeautifulSoup(page.text, 'html.parser')

pageTitle = []
for title in zupka.find_all('title'):
    pageTitle.append(title.text.strip())

print(pageTitle)
