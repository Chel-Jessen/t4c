# Setup:
- Ersetzen Sie den OpenAI-Key und die OpenAI-Org in der openai.env Datei mit ihren eigenen Werten.  
Key: https://platform.openai.com/account/api-keys  
Org: https://platform.openai.com/account/org-settings
- Sie können das Projekt in eine .exe Datei umwandeln mit einem dieser Tools  
PyInstaller https://pyinstaller.org/en/stable/  
Auto-Py-To-Exe https://github.com/brentvollebregt/auto-py-to-exe  
Beachten Sie aber, dass Python Dateien nicht für eine .exe Ausführung gedacht sind und deshalb Fehler auftreten können.
Ich empfehle die Ausführung über eine eigene Python Installation
- Für dieses Projekt wurde Python 3.10 verwendet.  
Ältere Python Versionen könnten eventuell nicht funktionieren.
- Installieren Sie alle Dependencies aus der requirements.txt Datei mit  
  pip install -r requirements.txt

# Ausführen:
- main.py starten
- den Pfad zur Input-Datei eingeben (.xslx für URLs zum scrapen und .csv für Lieferantendaten)
- Im Menü die zu generierenden Attribute auswählen (Bis auf Misc ist jeweils nur eine Option pro Attribut möglich)
- Mit 0 die Auswahl beenden und bestätigen
- Die Output-Datei wird im selben Verzeichnis als "output_{timestamp}.xlsx" gespeichert.


# Voreinstellungen:
 Sie können in der options.json Datei unter 'Voreinstellungen' eigene Voreinstellungen speichern.  
 Geben Sie ihrer Voreinstellung einen Namen und legen Sie alle dafür zu erzeugenden Attribute an.  
 Verwenden Sie hier bitte die entsprechende Nummer. Wenn ein Attribut nicht erzeugt werden soll, einfach einen leeren Text "" eingeben.  
 Misc Optionen müssen immer in [ ] mit Kommata getrennt sein.  
 Sie können unbegrenzt viel Voreinstellungen speichern, solange die Namen einzigartig sind und sich alle im 
 "Voreinstellungen" Feld befinden und dem Schema folgen.  
 
# Prompts:
 Sie können in der prompts.py Datei jeden Prompt nach Belieben anpassen.  
 Der Platzhalter %opt wird ersetzt durch die ausgewählte Option und %text durch den Input-Text entweder des HTML Quellcodes oder der CSV Reihe.  
 Jeder Prompt muss %opt und %text enthalten.  
 
# Output Datei
 Die Output-Datei wird als .xlsx Datei gespeichert.  
 Wenn die Input-Datei eine .xlsx Datei war, ist die erste Spalte die jeweilige gescrapte URL.  
 Die oberste Zeile beinhaltet immer die ausgewählte Option.  
 Markierte Felder bedarfen insbesondere einer Nachprüfung:
 - Rot für Zeichenlimit
 - Blau für Französisch
 - Gelb für HTML
 - Pink für Wörterlimit
 - Braun für andere Besonderheiten  

Da eine Zelle jedoch nur eine Farbe haben kann, könnten auch Überschneidungen auftreten.