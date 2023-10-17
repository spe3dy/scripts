#vergleiche Arbeiten vs Jobcenter

#Eingang
M = 325 # Miete
FG = 42 # Fahrgeld

#Ausgang
S = 100 # Strom
G = 88 # Gas
I = 50 # Internet
C = 25 # iPad
F = 50 # Fahrkarte
H = 10 # Handy
Sp = 250 # Spesen - Auswaerts Essen

#Zusammenfassung
Einnahmen = (M+FG)
Ausgaben = (M+S+G+I+C+H) # Fixkosten

Jobcenter = 890 # Buergergeld
ArbeitWCV = 1728.31 #Netto Gehalt WCV

print(f"Ausgaben abzueglich Fixkosten ({Ausgaben} Euro): \n WCV {ArbeitWCV - Ausgaben - Sp - F} Euro,\nJobcenter {Jobcenter - Ausgaben + FG -F} Euro.\n Differenz {ArbeitWCV - Jobcenter + FG -F}")
