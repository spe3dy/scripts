import requests
from bs4 import BeautifulSoup

URL = 'https://s.to/neue-episoden' # Hier wird die URL angegeben

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser') # Hier wird BeautifullSoup gesagt, dass es die textdatei als html parsen soll

checknew_data = soup.find('div', {'class', 'newEpisodeList', 'german.svg'} ) # Hier wird der Filter gesetzt
checknew_data = checknew_data.text

checknew_data = '\n'.join((line for line in checknew_data.split('\n') if line))
print(checknew_data)