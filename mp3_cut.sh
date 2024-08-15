#!/bin/bash

# Verzeichnis, in dem sich die MP3-Dateien befinden
input_dir="/pfad/zu/deinem/verzeichnis"
output_dir="/pfad/zu/deinem/ausgabe_verzeichnis"

# Erstelle das Ausgabe-Verzeichnis, falls es noch nicht existiert
mkdir -p "$output_dir"

# Dauer eines Abschnitts in Sekunden (1 Stunde = 3600 Sekunden)
duration=3600

# Schneide jede MP3-Datei in stündliche Abschnitte
for file in "$input_dir"/*.mp3; do
  filename=$(basename "$file" .mp3)
  
  # Bestimme die Gesamtdauer der Datei
  total_duration=$(ffprobe -i "$file" -show_entries format=duration -v quiet -of csv="p=0")
  total_duration=${total_duration%.*} # Sekunden ohne Nachkommastellen

  start_time=0
  part_num=1  # Zähler für die Dateinummerierung

  while [ $start_time -lt $total_duration ]; do
    # Generiere einen eindeutigen Dateinamen für jedes Segment
    output_file="$output_dir/${filename}_$(printf "%03d" $part_num).mp3"
    
    # Schneiden und die resultierende Datei speichern
    ffmpeg -i "$file" -ss "$start_time" -t "$duration" -acodec copy "$output_file"
    
    # Startzeit für den nächsten Abschnitt aktualisieren
    start_time=$((start_time + duration))
    part_num=$((part_num + 1))  # Zähler erhöhen
  done
done
