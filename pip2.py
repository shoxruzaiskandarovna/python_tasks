import requests
from pprint import pprint as print

API_KEY = '28014de4385a212c57801796'
currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
response = requests.get(url)
kurs = response.json()['conversion_rate']
print(f"1 dollar kursi {kurs} so`mga teng")

from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="gray-text")
print(news[2].text)