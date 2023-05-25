import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.example.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features = "html.parser")
    soup_list = soup.find_all("a")
    for link in soup_list:
        href = link.get('href')
        print(href)
else:
    print(f"немає підклчення {response.status_code}")