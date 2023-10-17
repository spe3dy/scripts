#vergleiche Arbeiten vs Jobcenter

M = 325 # Miete
S = 100 # Strom
G = 88 # Gas
I = 50 # Internet
C = 25 # iPad
F = 50 # Fahrkarte
H = 10 # Handy

Ausgaben = (M+S+G+I+C+F+H) # Fixkosten
Jobcenter = 890 # Buergergeld
ArbeitWCV = 1728.31 #Netto Gehalt WCV
Spesen = 200 # Auswaerts Essen

print(f"Ausgaben abzueglich Fixkosten ({Ausgaben} Euro): \nWCV {ArbeitWCV - Ausgaben - Spesen} Euro,\nJobcenter {Jobcenter - Ausgaben} Euro.\n Differenz {ArbeitWCV - Jobcenter}")
