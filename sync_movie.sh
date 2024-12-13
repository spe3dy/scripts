#!/bin/bash

# Quell- und Zielordner
SOURCE_DIR="/mnt/user/Obi-Cloud/Movies"
DEST_DIR="/mnt/user/isos/Film-Sync-Obi"

# Log-Datei
LOG_FILE="/mnt/user/isos/Film-Sync-Obi/transfer_log.txt"
COPIED_FILES_LIST="/mnt/user/isos/Film-Sync-Obi/copied_files.txt"

# Zeitstempel für Startzeit
START_TIME=$(date +%s)

# Header in die Log-Datei schreiben, falls sie noch nicht existiert
if [ ! -f "$LOG_FILE" ]; then
  echo "Transfer gestartet am: $(date)" > "$LOG_FILE"
  echo "--------------------------------------" >> "$LOG_FILE"
fi

# Live-Log-Anzeige
echo "Live-Log: Transfer gestartet am: $(date)"

# Sicherstellen, dass die Datei für die kopierten Dateien existiert
if [ ! -f "$COPIED_FILES_LIST" ]; then
  touch "$COPIED_FILES_LIST"
fi

# Findet Dateien, die in den letzten 2880 Minuten (48 Stunden) geändert wurden
find "$SOURCE_DIR" -type f -mmin -14400 | while read -r file; do
    # Überprüfen, ob der Dateiname schon in der Liste der kopierten Dateien vorhanden ist
    if grep -Fxq "$(basename "$file")" "$COPIED_FILES_LIST"; then
        # Wenn die Datei bereits kopiert wurde, überspringen
        echo "$(date) - Datei $(basename "$file") wurde bereits kopiert. Überspringe." | tee -a "$LOG_FILE"
    else
        # Datei in das Zielverzeichnis kopieren
        cp "$file" "$DEST_DIR"

        # Den Dateinamen in die Liste der kopierten Dateien eintragen
        echo "$(basename "$file")" >> "$COPIED_FILES_LIST"

        # In die Log-Datei schreiben
        echo "$(date) - Kopiert: $file" | tee -a "$LOG_FILE"
        echo "Datei $(basename "$file") kopiert."  # Live-Log Anzeige
    fi
done

# Zeitstempel für Endzeit
END_TIME=$(date +%s)

# Berechnung der Dauer
DURATION=$((END_TIME - START_TIME))

# Dauer in die Log-Datei schreiben
echo "Transfer abgeschlossen. Dauer: $((DURATION / 60)) Minuten und $((DURATION % 60)) Sekunden." | tee -a "$LOG_FILE"

# Ende der Log-Datei
echo "--------------------------------------" | tee -a "$LOG_FILE"

# Log-Datei per E-Mail senden
#EMAIL="admin@home.speedyland.de"
#SUBJECT="Transfer Log: $(date)"
#cat "$LOG_FILE" | mail -s "$SUBJECT" "$EMAIL"

# echo "Log-Datei wurde an $EMAIL gesendet."

