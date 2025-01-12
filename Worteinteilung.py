import requests

# Schritt 1: Grundwortschatz laden
def load_grundwortschatz(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip().lower() for line in f if line.strip()]
        return words
    except Exception as e:
        print(f"Fehler beim Laden der Grundwortschatz-Datei: {e}")
        return []


# Teil 4: Check Grundwort
def check_grundwort(word, grundwortschatz_path="grundwortschatz2.txt"):
    grundwortschatz = load_grundwortschatz(grundwortschatz_path)
    
    if word.lower() in grundwortschatz:
        return True
    else:
        return False
    
# Teil 5
def wiktionary(word):
    url = f"https://de.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": word,
        "prop": "info"
    }
    response = requests.get(url, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    if "-1" in pages:
        return False  # Seite existiert nicht
    return True  # Seite existiert"""



# Teil 6
def textcheck(text):
    
    for i in text:
        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122) or i in "äöüß ÄÖÜ":
            pass
        else:
            text = text.replace(i, "")

    liste = text.split(" ")
    Grundliste = []
    Andereliste = []
    Sonstige = []

    for i in liste:
        if check_grundwort(i, grundwortschatz_path="grundwortschatz2.txt") == True:
            Grundliste.append(i)
        else:
            Andereliste.append(i)
    
    for i in Andereliste:
        if wiktionary(i) == True:
            pass
        else:
            Sonstige.append(i)
            Andereliste.remove(i)



    print("Grundwörter", Grundliste)
    print("Andere Wörter", Andereliste)
    print("Sonstige Wörter", Sonstige)
    """for i in liste:
        print("Wort")
        print(i)"""

    

if __name__ == "__main__":

    Satz = "Fertigungsanlagen können verkauft (verschrottet) werden. Eine verschrottete Fertigungsanlage steht bereits zu Beginn der Periode nicht mehr zur Verfügung. Anlagen, die bereits vollständig abgeschrieben sind, werden nicht automatisch verkauft. Um eine bestimmte Anlage zu verkaufen, setzen Sie einen Haken im Entscheidungsbereich Desinvestition. Die entsprechenden Fertigungsanlagen werden dann zu einem anlagenspezifischen Prozentsatz des Restbuchwertes verkauft. Bei Anlagen des Typs A beträgt der Erlös 20% (Typ B 25%, Typ C 30%) des Restbuchwerts.  Sollten Sie Maschinen verschrotten, so erhalten Sie einen Resterlös, welcher als Einzahlung im Finanzbericht Ihrem Unternehmen zufließt. Jedoch führt der Wertverlust in Höhe der Differenz von Restbuchwert minus Resterlös zu einer „außerordentlichen Abschreibung“ im Bereich Fertigungsanlagen in der Kostenartenrechnung. Sie können nicht alle Maschinen verkaufen, d. h. mindestens eine Anlage muss in Ihrem Bestand verbleiben."

    textcheck(Satz)
