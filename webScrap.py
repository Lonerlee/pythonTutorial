from bs4 import BeautifulSoup

with open("youtube.com", "r") as f:
  doc = BeautifulSoup(f, "html.parser")

tag = doc.title
print(tag)