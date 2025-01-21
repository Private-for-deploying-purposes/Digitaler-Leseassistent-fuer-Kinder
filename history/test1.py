from transformers import pipeline
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import streamlit as st

# NLTK-Ressourcen herunterladen
nltk.download("punkt")
nltk.download("stopwords")

# NER-Modell initialisieren
ner_pipeline = pipeline("ner", model="dbmdz/bert-base-german-cased", aggregation_strategy="simple")

# Deutsche Stoppwörter laden
german_stopwords = set(stopwords.words("german"))

# Zusätzliche Wörter(Grundwortschatz2), die ignoriert werden sollen
def load_grundwortschatz(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip().lower() for line in f if line.strip()]
        return set(words)
    except Exception as e:
        print(f"Fehler beim Laden der Grundwortschatz-Datei: {e}")
        return []
frequent_words = load_grundwortschatz("grundwortschatz2.txt")
print(frequent_words)

# Funktion: Häufige Wörter filtern
def is_common_word(word):
    return word.lower() in german_stopwords or word.lower() in frequent_words

# Funktion: Wiktionary für Definitionen
def fetch_wiktionary_definition(word):
    api_url = "https://de.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": word,
        "explaintext": True
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    for _, page_data in pages.items():
        extract = page_data.get("extract", "")
        if extract:
            return extract_meanings_only(extract)

    return "Keine Erklärung gefunden."

# Extrahiere nur den Bedeutungen-Abschnitt
def extract_meanings_only(text):
    match = re.search(r"Bedeutungen:\n(.*?)\n(?:Synonyme:|Beispiele:|Wortbildungen:|\Z)", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "Keine Bedeutungen gefunden."

# Schwierige Wörter identifizieren
def find_difficult_words(text):
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.isalpha() and len(word) > 6 and not is_common_word(word)]

    detected_words = set()
    results = ner_pipeline(" ".join(filtered_words))

    for entity in results:
        word = entity.get("word")
        # Entferne Präfixe wie ## und stelle sicher, dass das Wort vollständig bleibt
        if word and not word.startswith("##"):
            full_word = word.strip(".,!?;:()[]{}")
            if full_word.isalpha() and len(full_word) > 6 and not is_common_word(full_word):
                detected_words.add(full_word)

    definitions = {}
    for word in detected_words:
        definitions[word] = fetch_wiktionary_definition(word)

    return definitions

def textcheck(text):
    for i in text:
        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122) or i in "äöüß ÄÖÜ":
            pass
        else:
            text = text.replace(i, "")

    schwierige_worte = [
        wort for wort in text.split(" ") 
        if wort.lower().strip(".,!?;:") not in frequent_words
    ]

    schwierige_worte = set(schwierige_worte)
    text = ' '.join(schwierige_worte)
    return text


# Hauptfunktion für Streamlit
def main():
    st.title("📖 Digitaler Leseassistent - Wörter Erkennen und Erklären")

    text = st.text_area("Gib hier deinen Text ein:", height=200)

    if st.button("🔍 Wörter analysieren"):
        if text.strip():
            with st.spinner("Analysiere den Text..."):
                text2 = text
                text3 = textcheck(text2)
                definitions = find_difficult_words(text)

            if definitions:
                st.markdown("### 🧠 Gefundene schwierige Wörter:")
                for word, definition in definitions.items():
                    if word in text3:
                        st.markdown(f"- **{word}**: {definition}")
            else:
                st.success("Keine schwierigen Wörter erkannt!")
        else:
            st.error("Bitte gib einen Text ein.")

if __name__ == "__main__":
    main()
