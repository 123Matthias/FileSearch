import os
import re

import unicodedata

def list_files(directory, keywords=None, recursive=False):
    """
    Listet alle Dateien in einem Verzeichnis auf, optional gefiltert nach Keywords.
    
    Args:
        directory: Der Pfad zum Verzeichnis
        keywords: String mit Keywords (getrennt durch Leerzeichen oder Komma) oder None
        recursive: Wenn True, werden Unterverzeichnisse durchsucht
        
    Returns:
        Eine Liste mit allen Dateipfaden (gefiltert nach Keywords)
    """
    files = []

    
    
    # Keywords aufbereiten
    keyword_list = []
    if keywords:
        # Ersetze Kommas durch Leerzeichen und splitte
        cleaned = keywords.replace(',', ' ')
        keyword_list = [k.strip().lower() for k in cleaned.split() if k.strip()]
    
    if recursive:
        # Rekursive Suche mit os.walk
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                
                # Wenn keine Keywords, alle Dateien nehmen
                if not keyword_list:
                    files.append(filepath)
                else:
                    # Prüfen ob eines der Keywords im Dateinamen vorkommt
                    file_lower = filename.lower()
                    file_normalized = unicodedata.normalize('NFC', file_lower)  # Dateiname normalisieren
                    print(f"Original: '{filename}' -> klein: '{file_lower}'")

                    for keyword in keyword_list:
                        keyword_normalized = unicodedata.normalize('NFC', keyword)  # Keyword normalisieren
                        print(f"  Vergleiche '{keyword}' mit '{file_lower}'")
                        print(f"  Als Bytes - Keyword: {keyword.encode('utf-8')}")
                        print(f"  Als Bytes - Datei:   {file_lower.encode('utf-8')}")
                        
                        if keyword_normalized in file_normalized:
                            print(f"  → GEFUNDEN!")
                            files.append(filepath)
                            break
                        else:
                            print(f"  → NICHT gefunden")

    else:
        # Nur aktuelles Verzeichnis
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)
            if os.path.isfile(full_path):
                # Wenn keine Keywords, alle Dateien nehmen
                if not keyword_list:
                    files.append(full_path)
                else:
                    # Prüfen ob eines der Keywords im Dateinamen vorkommt
                    item_lower = item.lower()
                    for keyword in keyword_list:  # ← Hier definierst du keyword
                        if keyword in item_lower:
                            print(f"'{keyword}' gefunden in '{item}'")
                            files.append(full_path)
                            break  # Stop nach dem ersten Treffer
                      
    return files

def normalize_text(text):
    """Wandle in NFC-Form um (ü als ein Zeichen)"""
    return unicodedata.normalize('NFC', text)