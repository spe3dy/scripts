import requests
from bs4 import BeautifulSoup

URL = 'https://s.to/neue-episoden'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
pagestitle = soup.find('span', {'class=': 'col-md-12'})
print(pagestitle)
