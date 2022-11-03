import requests
from bs4 import BeautifulSoup

URL = 'https://sonnenaufgang.online/sun/essen_(germany)' # Hier wird die URL angegeben

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser') # Hier wird BS gesagt, dass es die textdatei als html parsen soll
sunrise_data = soup.find('span', {'data-name', 'sunrise'}) # Hier wird der Filter gesetzt
sunrise_data = sunrise_data.text
sunrise_data = sunrise_data[:-3] # Loescht die letzten 3 Zeichen
#print (sunrise_data)
print(f'Die Sonne geht aktuell um {sunrise_data} Uhr auf')