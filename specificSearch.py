from bs4 import BeautifulSoup
import requests

URL = "https://www.youtube.com/watch?v=0_t6FqNz7z0&list=PLyyl5wAdbtvABUNmAUdna-ir11Vhw0Hvy"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("span", id_="video-title")


for job_element in job_elements:
    title_element = job_element.find("span", class_="title")
    print(title_element.text.strip())
    print()
