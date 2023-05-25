#1
import requests
from bs4 import BeautifulSoup

response = requests.get("https://uk.wikipedia.org/wiki/")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    for i in soup.find_all('h2'):
        i.extract()
    text = ' '.join(soup.stripped_strings)
    words = text.split()
    print(words)
else:
    print(f"немає підклчення {response.status_code}")