from logging.config import listen
from bs4 import BeautifulSoup
import requests
file = open("quellen.txt", "r")
for line in file:
    #print(line)
    liste.append(line)
print(liste)
print("ich habe folgende Ergebnisse gefunden {}") ## Nicht getestet, ging nicht auf dem Windows Rechner