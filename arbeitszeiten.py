from flask import Flask, request, render_template_string
import pandas as pd
import mysql.connector

app = Flask(__name__)

# MySQL-Verbindungsdetails
DB_CONFIG = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'Arbeitsstunden'
}

# HTML für die Web-Oberfläche
UPLOAD_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV-Upload</title>
</head>
<body>
    <h1>CSV-Datei hochladen</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="csvfile" accept=".csv" required>
        <button type="submit">Hochladen</button>
    </form>
</body>
</html>
"""

# Tabelle erstellen, falls sie noch nicht existiert
def create_table():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Arbeitszeit (
        Ort VARCHAR(255),
        Nummer INT,
        Eintrittsdatum DATE,
        Eintrittszeit TIME,
        Austrittsdatum DATE,
        Austrittszeit TIME,
        Stunden FLOAT,
        hhmmss TIME,
        Notizen TEXT
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/')
def index():
    return render_template_string(UPLOAD_PAGE)

@app.route('/upload', methods=['POST'])
def upload():
    if 'csvfile' not in request.files:
        return "Keine Datei hochgeladen", 400

    file = request.files['csvfile']
    if file.filename == '':
        return "Leere Datei hochgeladen", 400

    try:
        # CSV einlesen
        df = pd.read_csv(file, sep=None, engine='python')

        # Leere Werte durch None ersetzen
        df = df.where(pd.notnull(df), None)

        # Verbindung zur Datenbank herstellen
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Daten Zeile für Zeile einfügen
        for _, row in df.iterrows():
            insert_query = """
            INSERT INTO Arbeitszeit (Ort, Nummer, Eintrittsdatum, Eintrittszeit, Austrittsdatum, Austrittszeit, Stunden, hhmmss, Notizen)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                row['Ort'],
                int(row['Nummer']) if pd.notna(row['Nummer']) else None,
                pd.to_datetime(row['Eintrittsdatum'], errors='coerce').date() if pd.notna(row['Eintrittsdatum']) else None,
                row['Eintrittszeit'],
                pd.to_datetime(row['Austrittsdatum'], errors='coerce').date() if pd.notna(row['Austrittsdatum']) else None,
                row['Austrittszeit'],
                float(str(row['Stunden']).replace(',', '.')) if pd.notna(row['Stunden']) else None,
                row['hhmmss'],
                row['Notizen'] if pd.notna(row['Notizen']) else None
            ))

        connection.commit()
        cursor.close()
        connection.close()

        return "Datei erfolgreich importiert"

    except Exception as e:
        return f"Fehler beim Verarbeiten der Datei: {e}", 500

if __name__ == '__main__':
    # Sicherstellen, dass die Tabelle existiert
    create_table()
    # Flask-App starten
    app.run(debug=True, host='0.0.0.0')
