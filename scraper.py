from bs4 import BeautifulSoup
import requests

## print('Erster Webscraper')

# https://s.to

# URL = 'https://home.speedyland.de/comcave/whatismyip' 

URL = 'https://s.to'                   # Basis URL die Abgerufen werden soll 
perepherie = '/serie/stream/peripherie' # URL Erweiterung
andor = '/serie/stream/andor'
House_of_Dragon = '/serie/stream/house-of-the-dragon'
Rick_and_Morty ='/serie/stream/rick-and-morty'

sP = (URL + perepherie)
sA = (URL + andor)
sHoD = (URL + House_of_Dragon)
sRaM = ( URL + Rick_and_Morty)

print(sP, sA, sHoD, sRaM) 