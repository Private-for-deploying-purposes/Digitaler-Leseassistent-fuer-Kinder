from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import streamlit as st

# NER-Pipeline mit deutschem Modell
ner_pipeline = pipeline("ner", model="dbmdz/bert-base-german-cased", aggregation_strategy="simple")

def get_duden_definition(word):
    """
    Holt die Definition eines Wortes aus dem Duden.
    """
    word = word.lower().strip(",.?!")  # Normalisiere das Wort
    try:
        url = f"https://www.duden.de/rechtschreibung/{word}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Suche nach der Hauptdefinition
            definition_element = soup.find("div", class_="lemma__determination")
            if definition_element:
                return definition_element.get_text(strip=True)

            # Alternative Definition (z. B. bei Synonymen)
            additional_definition = soup.find("div", class_="tuple__definition")
            if additional_definition:
                return additional_definition.get_text(strip=True)

            # Kein Treffer gefunden
            return f"Keine Definition für '{word}' im Duden gefunden."
        else:
            return f"Duden-Seite nicht gefunden für '{word}'."
    except Exception as e:
        return f"Fehler bei der Definitionsermittlung: {str(e)}"

def find_and_define_difficult_words(text):
    """
    Erkennt schwierige Wörter im Text und holt Definitionen.
    """
    detected_words = set()
    results = ner_pipeline(text)

    for entity in results:
        word = entity['word']
        if not word.startswith("##") and len(word) > 2 and word.isalpha():
            detected_words.add(word)

    definitions = {}
    for word in detected_words:
        definitions[word] = get_duden_definition(word)

    return definitions

def main():
    """
    Streamlit-App für die Verarbeitung von Text und Darstellung der Ergebnisse.
    """
    st.title("📖 Digitaler Leseassistent - Wörter Erkennen und Erklären")

    text = st.text_area("Gib hier deinen Text ein, um schwierige Wörter zu erkennen:", height=200)

    if st.button("🔍 Wörter analysieren"):
        if text.strip():
            with st.spinner("Analysiere den Text und hole Definitionen..."):
                definitions = find_and_define_difficult_words(text)

            if definitions:
                st.markdown("### 🧠 Gefundene schwierige Wörter und ihre Definitionen:")
                for word, definition in definitions.items():
                    st.markdown(f"- **{word}**: {definition}")
            else:
                st.success("Keine schwierigen Wörter erkannt!")
        else:
            st.error("Bitte gib einen gültigen Text ein!")

if __name__ == "__main__":
    main()
