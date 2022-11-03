import requests
from bs4 import BeautifulSoup

URL = 'https://s.to/neue-episoden' # Hier wird die URL angegeben

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser') # Hier wird BS gesagt, dass es die textdatei als html parsen soll

checknew_data = soup.find('div', {'class', 'newEpisodeList'}) # Hier wird der Filter gesetzt
checknew_data = checknew_data.text
print(checknew_data)