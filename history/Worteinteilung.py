import requests
import re

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

def erklaeren(word):
    print("Hello World")
    api_url = "https://de.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": word,
        "explaintext": True  # Nur reiner Text (ohne HTML)
    }

    # API-Request
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()

    # Extrahiere die Erklärung
    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        extract = page_data.get("extract", "")
        if extract:
            # Relevante Abschnitte extrahieren
            return extract_meanings_only(extract)

    return f"Keine Erklärung für das Wort '{word}' gefunden."

def extract_meanings_only(text):
    # Extrahiere nur den Bedeutungen-Abschnitt
    match = re.search(r"Bedeutungen:\n(.*?)\n(?:Synonyme:|Beispiele:|Wortbildungen:|\Z)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "Keine Bedeutungen gefunden."

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

    #Satz = "Fertigungsanlagen können verkauft (verschrottet) werden. Eine verschrottete Fertigungsanlage steht bereits zu Beginn der Periode nicht mehr zur Verfügung. Anlagen, die bereits vollständig abgeschrieben sind, werden nicht automatisch verkauft. Um eine bestimmte Anlage zu verkaufen, setzen Sie einen Haken im Entscheidungsbereich Desinvestition. Die entsprechenden Fertigungsanlagen werden dann zu einem anlagenspezifischen Prozentsatz des Restbuchwertes verkauft. Bei Anlagen des Typs A beträgt der Erlös 20% (Typ B 25%, Typ C 30%) des Restbuchwerts.  Sollten Sie Maschinen verschrotten, so erhalten Sie einen Resterlös, welcher als Einzahlung im Finanzbericht Ihrem Unternehmen zufließt. Jedoch führt der Wertverlust in Höhe der Differenz von Restbuchwert minus Resterlös zu einer „außerordentlichen Abschreibung“ im Bereich Fertigungsanlagen in der Kostenartenrechnung. Sie können nicht alle Maschinen verkaufen, d. h. mindestens eine Anlage muss in Ihrem Bestand verbleiben."
    #Satz = "Es hatte ein Mann einen Esel, der schon lange Jahre die Säcke unverdrossen zur Mühle getragen hatte, dessen Kräfte aber nun zu Ende gingen, so dass er zur Arbeit immer untauglicher ward. Da dachte der Herr daran, ihn aus dem Futter zu schaffen, aber der Esel merkte, dass kein guter Wind wehte, lief fort und machte sich auf den Weg nach Bremen; dort, meinte er, könnte er ja Stadtmusikant werden. Als er ein Weilchen fortgegangen war, fand er einen Jagdhund auf dem Wege liegen, der jappte wie einer, der sich müde gelaufen hat. „Nun, was jappst du so, Packan?“ fragte der Esel. „Ach,“ sagte der Hund, „weil ich alt bin und jeden Tag schwächer werde, auch auf der Jagd nicht mehr fort kann, hat mich mein Herr wollen totschlagen, da hab ich Reissaus genommen; aber womit soll ich nun mein Brot verdienen?“ – „Weisst du was?“ sprach der Esel, „ich gehe nach Bremen und werde dort Stadtmusikant, geh mit und lass dich auch bei der Musik annehmen. Ich spiele die Laute und du schlägst die Pauken.“ Der Hund war’s zufrieden, und sie gingen weiter. Es dauerte nicht lange, so sass da eine Katze an dem Weg und macht ein Gesicht wie drei Tage Regenwetter. „Nun, was ist dir in die Quere gekommen, alter Bartputzer?“ sprach der Esel. „Wer kann da lustig sein, wenn’s einem an den Kragen geht,“ antwortete die Katze, „weil ich nun zu Jahren komme, meine Zähne stumpf werden, und ich lieber hinter dem Ofen sitze und spinne, als nach Mäusen herumjagen, hat mich meine Frau ersäufen wollen; ich habe mich zwar noch fortgemacht, aber nun ist guter Rat teuer: wo soll ich hin?“ – „Geh mit uns nach Bremen, du verstehst dich doch auf die Nachtmusik, da kannst du ein Stadtmusikant werden.“ Die Katze hielt das für gut und ging mit. Darauf kamen die drei Landesflüchtigen an einem Hof vorbei, da sass auf dem Tor der Haushahn und schrie aus Leibeskräften. „Du schreist einem durch Mark und Bein,“ sprach der Esel, „was hast du vor?“ – „Da hab‘ ich gut Wetter prophezeit,“ sprach der Hahn, „weil unserer lieben Frauen Tag ist, wo sie dem Christkindlein die Hemdchen gewaschen hat und sie trocknen will; aber weil morgen zum Sonntag Gäste kommen, so hat die Hausfrau doch kein Erbarmen und hat der Köchin gesagt, sie wollte mich morgen in der Suppe essen, und da soll ich mir heut abend den Kopf abschneiden lassen. Nun schrei ich aus vollem Hals, solang ich kann.“ – „Ei was, du Rotkopf,“ sagte der Esel, „zieh lieber mit uns fort, wir gehen nach Bremen, etwas Besseres als den Tod findest du überall; du hast eine gute Stimme, und wenn wir zusammen musizieren, so muss es eine Art haben.“ Der Hahn liess sich den Vorschlag gefallen, und sie gingen alle vier zusammen fort."
    #textcheck(Satz)

    print("Check1")
    print(erklaeren(word="teuer"))
    print("Check2")
