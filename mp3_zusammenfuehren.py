import os
import subprocess

# Liste der Verzeichnisse
directories = [
    "Master of Chess (Live)", "[001]-und der Superpapagei", "[002]-und der Phantomsee", "[003]-und der Karpatenhund",
    "[004]-und die schwarze Katze", "[005]-und der Fluch des Rubins", "[006]-und der sprechende Totenkopf",
    "[007]-und der unheimliche Drache", "[008]-und der gruene Geist", "[009]-und die raetselhaften Bilder",
    "[010]-und die fluesternde Mumie", "[011]-und das Gespensterschloss", "[012]-und der seltsame Wecker",
    "[013]-und der lachende Schatten", "[014]-und das Bergmonster", "[015]-und der rasende Loewe",
    "[016]-und der Zauberspiegel", "[017]-und die gefaehrliche Erbschaft", "[018]-und die Geisterinsel",
    "[019]-und der Teufelsberg", "[020]-und die flammende Spur", "[021]-und der tanzende Teufel",
    "[022]-und der verschwundene Schatz", "[023]-und das Aztekenschwert", "[024]-und die silberne Spinne",
    "[025]-und die singende Schlange", "[026]-und die Silbermine", "[027]-und der magische Kreis",
    "[028]-und der Doppelgaenger", "[029]-Die Originalmusik", "[030]-und das Riff der Haie",
    "[031]-und das Narbengesicht", "[032]-und der Ameisenmensch", "[033]-und die bedrohte Ranch",
    "[034]-und der rote Pirat", "[035]-und der Hoehlenmensch", "[036]-und der Super Wal",
    "[037]-und der heimliche Hehler", "[038]-und der unsichtbare Gegner", "[039]-und die Perlenvoegel",
    "[040]-und der Automarder", "[041]-und das Volk der Winde", "[042]-und der weinende Sarg",
    "[043]-und der hoellische Werwolf", "[044]-und der gestohlene Preis", "[045]-und das Gold der Wikinger",
    "[046]-und der schrullige Millionaer", "[047]-und der giftige Gockel", "[048]-und die gefaehrlichen Faesser",
    "[049]-und die Comic Diebe", "[050]-und der verschwundene Filmstar", "[051]-und der riskante Ritt",
    "[052]-und die Musikpiraten", "[053]-und die Automafia", "[054]-Gefahr im Verzug", "[055]-Gekaufte Spieler",
    "[056]-Angriff der Computer Viren", "[057]-Tatort Zirkus", "[058]-und der verrueckte Maler",
    "[059]-Giftiges Wasser", "[060]-Dopingmixer", "[061]-und die Rache des Tigers", "[062]-Spuk im Hotel",
    "[063]-Fussball Gangster", "[064]-Geisterstadt", "[065]-Diamtengenschmuggel", "[066]-und die Schattenmaenner",
    "[067]-Das Geheimnis der Saerge", "[068]-Der Schatz im Bergsee", "[069]-Spaete Rache", "[070]-Schuesse aus dem Dunkel",
    "[071]-Die verschwundene Seglerin", "[072]-Dreckiger Deal", "[073]-Poltergeist", "[074]-Das brennende Schwert",
    "[075]-Die Spur des Raben", "[076]-Stimmen aus dem Nichts", "[077]-Pistenteufel", "[078]-Das leere Grab",
    "[079]-Im Bann des Voodoo", "[080]-Geheimakte Ufo", "[081]-Verdeckte Fouls", "[082]-Die Karten des Boesen",
    "[083]-Meuterei auf hoher See", "[084]-Musik des Teufels", "[085]-Feuerturm", "[086]-Nacht in Angst",
    "[087]-Wolfsgesicht", "[088]-Vampir im Internet", "[089]-Toedliche Spur", "[090]-Der Feuerteufel",
    "[091]-Labyrinth der Goetter", "[092]-Todesflug", "[093]-Das Geisterschiff", "[094]-Das schwarze Monster",
    "[095]-Botschaft von Geisterhand", "[096]-Der rote Raecher", "[097]-Insektenstachel", "[098]-Tal des Schreckens",
    "[099]-Rufmord", "[100]-Toteninsel", "[101]-Das Hexen Handy", "[102]-Doppelte Taeuschung", "[103]-Das Erbe des Meisterdiebes",
    "[104]-Gift per E-Mail", "[105]-Der Nebelberg", "[106]-Der Mann ohne Kopf", "[107]-und der Schatz der Moenche",
    "[108]-Die sieben Tore", "[109]-GefÃ¤hrliches Quiz", "[110]-Panik im Park", "[111]-Die Hoehle des Grauens",
    "[112]-Schlucht der Daemonen", "[113]-Das Auge des Drachen", "[114]-Die Villa der Toten", "[115]-Auf toedlichem Kurs",
    "[116]-Codename Cobra", "[117]-Der finstere Rivale", "[118]-Das duestere Vermaechtnis", "[119]-Der geheime Schluessel",
    "[120]-Der schwarze Skorpion", "[121]-Spur ins Nichts", "[122]-und der Geisterzug", "[123]-Fussballfieber",
    "[124]-Geister Canyon", "[125]-Feuermond", "[126]-Schrecken aus dem Moor", "[127]-Schwarze Madonna",
    "[128]-Schatten ueber Hollywood", "[129]-SMS aus dem Grab", "[130]-Der Fluch des Drachen", "[131]-Haus des Schreckens",
    "[132]-Spuk im Netz", "[133]-Fels der Daemonen", "[134]-Der tote Moench", "[135]-Fluch des Piraten",
    "[136]-und das versunkene Dorf", "[137]-Pfad der Angst", "[138]-Die geheime Treppe", "[139]-Das Geheimnis der Diva",
    "[140]-Stadt der Vampire", "[141]-Die Fussball Falle", "[142]-Toedliches Eis", "[143]-und die Poker Hoelle",
    "[144]-Zwillinge der Finsternis", "[145]-und die Rache des Samurai", "[146]-Der Biss der Bestie", "[147]-Grusel auf Campbell",
    "[148]-und die feurige Flut", "[149]-Der namenlose Gegner", "[150]-Geisterbucht", "[151]-Schwarze Sonne",
    "[152]-Skateboardfieber", "[153]-und das Fussballphantom", "[154]-Botschaft aus der Unterwelt", "[155]-und der Meister des Todes",
    "[156]-Im Netz des Drachen", "[157]-Im Zeichen der Schlangen", "[158]-und der Feuergeist", "[159]-Nacht der Tiger",
    "[160]-Geheimnisvolle Botschaften", "[161]-Die blutenden Bilder", "[162]-und der schreiende Nebel", "[163]-und der verschollene Pilot",
    "[164]-Fussball Teufel", "[165]-Im Schatten des Giganten", "[166]-und die brennende Stadt", "[167]-und das blaue Biest",
    "[168]-GPS Gangster", "[169]-Die Spur des Spielers", "[170]-Strasse des Grauens", "[171]-und das Phantom aus dem Meer",
    "[172]-und der Eisenmann", "[173]-Daemon der Rache", "[174]-und das Tuch der Toten", "[175]-Schattenwelt",
    "[176]-und der gestohlene Sieg", "[177]-Der Geist des Goldgraebers", "[178]-Der gefiederte Schrecken", "[179] Die Rache des Untoten",
    "[180]-und die fluesternden Puppen", "[181]-Das Kabinett des Zauberers", "[182]-Im Haus des Henkers", "[183]-und der letzte Song",
    "[184]-und der Hexengarten", "[185]-und der Mann ohne Augen", "[186]-Insel des Vergessens", "[187]-und das silberne Amulett",
    "[188]-Signale aus dem Jenseits", "[189]-und der unsichtbare Passagier", "[190]-und die Kammer der Raetsel",
    "[191]-Verbrechen im Nichts", "[192]-Im Bann des Drachen", "[193]-Schrecken aus der Tiefe", "[194]-und die Zeitreisende",
    "[195]-Im Reich der Ungeheuer", "[196]-Geheimnis des Bauchredners", "[197]-Im Auge des Sturms", "[198]-Die Legende der Gaukler",
    "[199]-und der gruene Kobold", "[200]-Feuriges Auge", "[201]-Hoehenangst", "[202]-Das weiÃŸe Grab", "[203]-Tauchgang ins Ungewisse",
    "[204]-Der dunkle Waechter", "[205]-Das raetselhafte Erbe", "[206]-und der Mottenmann", "[207]-Die falschen Detektive",
    "[208]-Kelch des Schicksals", "[209]-Kreaturen der Nacht", "[210]-und die schweigende Grotte", "[211]-und der Jadekoenig",
    "[212]-und der weiÃŸe Leopard", "[213]-Der Fluch der Medusa", "[214]-und der Geisterbunker", "[215]-und die verlorene Zeit",
    "[216]-Die Schwingen des Unheils", "[217]-und der KristallschÃ¤del", "[218]-Im Netz der LÃ¼gen", "[219]-und die Teufelsklippe",
    "[220]-Im Wald der Gefahren", "[221]-Manuskript des Satans", "[222]-und die Gesetzlosen", "[223]-und der Knochenmann",
    "[224]-Die Yacht des Verrats", "und der Superpapagei (Live)", "und der seltsame Wecker (Live)"
]

base_url = "/path/to/directory"

# Funktion um den Verzeichnis-Pfad zu erstellen
def get_directory_path(base_url, dir_name):
    return os.path.join(base_url, dir_name, "CD 01")

# Funktion um die mp3-Dateien zu kombinieren und zu konvertieren
def process_directory(directory):
    os.chdir(directory)
    temp_output = "temp_output.mp3"
    final_output = "korrekte.mp3"
    
    # cat *.mp3 > temp_output.mp3
    cat_command = f"cat *.mp3 > {temp_output}"
    subprocess.run(cat_command, shell=True)
    
    # lame --mp3input temp_output.mp3 korrekte.mp3
    lame_command = f"lame --mp3input {temp_output} {final_output}"
    subprocess.run(lame_command, shell=True)
    
    # Optional: Entfernen der temporären Datei
    os.remove(temp_output)

# Hauptprogramm: Durchlaufen aller Verzeichnisse
for dir_name in directories:
    directory_path = get_directory_path(base_url, dir_name)
    
    if os.path.exists(directory_path):
        process_directory(directory_path)
    else:
        print(f"Directory does not exist: {directory_path}")
