import requests
from bs4 import BeautifulSoup

URL = 'https://sonnenaufgang.online/sun/essen'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
sunrise_data = soup.find('span', {'data-name': 'sunrise'})
sunrise_data = sunrise_data.text
print(sunrise_data)