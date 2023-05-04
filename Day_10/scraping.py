import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/project/duckduckgo-search/"

web_page = requests.get(url)

soup = BeautifulSoup(web_page.content, "html.parser")

header = soup.find("h1").get_text()

print(header)
