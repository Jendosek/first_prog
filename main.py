import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.example.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features = "html.parser")
    for script in soup.find_all(["style", "script"]):
        script.extract() #вирізає хтмл код
    text = ' '.join(soup.stripped_strings) #відрізає зайве
    words = len(text.split())
    print(words)
else:
    print(f"немає підклчення {response.status_code}")