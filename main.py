import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.example.com/")
try:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    print(title)
except:
    print(f"Немає підключення {response.status_code}!")