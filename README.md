# Digitaler-Leseassistent-fuer-Kinder-
WWI22DSA/B Natural Language Processing (Aktuelle Data Science-Entwicklungen I)
Model also found on hugging face:
https://huggingface.co/mxhmxt/distilbert-qa-digital-reading-assistant-for-children/tree/main

Digitaler Leseassistent für Kinder: 
Ein interaktives Tool zur Unterstützung beim Lesen


Beschreibung:
Wir möchten ein Tool entwickeln, das Kinder beim Lesen unterstützt. Oft stoßen sie auf Wörter, die sie nicht verstehen, oder haben Fragen zu einem Text, die sie ohne Hilfe nicht beantworten können. Unser Projekt soll genau hier helfen.


Der Plan ist, einen interaktiven Leseassistenten zu bauen, der:

Schwierige Wörter erkennt und kindgerechte Erklärungen dazu liefert.
Fragen zu Texten beantwortet, damit Kinder das Gelesene besser verstehen können.
Eine einfache Benutzeroberfläche bietet, die Spaß macht und leicht zu bedienen ist.
Um das umzusetzen, nutzen wir moderne NLP-Technologien wie Named Entity Recognition (NER) und Question-Answering-Modelle (z. B. BERT, distilbert-base-uncased). Außerdem bauen wir eine intuitive Oberfläche, die Kinder zum Lesen und Interagieren einlädt.

Gruppenmitglieder:

Alexander Rohr
Tim Stelzner
Mehmet Marijanovic
Rouah Abdul Jawad



## Informationen zu den Dateien

- **Ordner:**

  - **distilbert-qa**: Enthält das trainierte Modell. Um das Modell zu trainieren, muss die Datei im Ordner **"training model" > "model fine tuning"** ausgeführt werden. Dabei wird das **`distilbert-base-uncased`**-Modell mit dem **SQuAD-Datensatz** trainiert. Das Modell ist auch auf [Hugging Face verfügbar](https://huggingface.co/mxhmxt/distilbert-qa-digital-reading-assistant-for-children/tree/main).
  
  - **gifs**: Enthält GIFs für die Website.

  - **history**: Dieser Ordner enthält vier Dateien:
    - **Code-Beispiel_bert.py**: Beispiel für die Verwendung eines vortrainierten Modells **`deepset/gelectra-base-germanquad`**.
    - **grundwortschatz.txt**: Die Ursprungsversion von **grundwortschatz2.txt**, die eine Liste schwieriger Wörter enthält.
    - **schwierigeWörter_mit_NER_CodeBeispiel.py**: Beispielcode zur Worterkennung mit Named Entity Recognition (NER).
    - **test1.py**: Überprüft, ob Wörter in der Liste der schwierigen Wörter enthalten sind und führt danach eine NER-Analyse durch.
  
  - **logs**: Enthält Log-Dateien, die beim Ausführen der Datei **"training model" > "model fine tuning"** generiert werden.

  - **training model**: Dieser Ordner enthält die folgenden Dateien:
    - **evaluation.py**: Wird verwendet, um die Leistung des trainierten Modells zu bewerten.
    - **model fine tuning.py**: Hier wird das Modell mit dem SQuAD-Datensatz feinabgestimmt.
    - **testing fine tuned model.py**: Wird verwendet, um das feinabgestimmte Modell zu testen.

- **.gitattributes**: Diese Datei trackt eine große Datei, die nicht hochgeladen werden kann.

- **Aufgaben**: Enthält die Aufgabenverteilung innerhalb unseres Teams.

- **Readme.md**: Diese Datei.

- **worteinteilung.py**: Ein Skript zur Wortaufteilung.

- **app.py**: Die Streamlit-basierte Webanwendung.

- **grundwortschatz2.txt**: Die erweiterte Version der Datei **grundwortschatz.txt**, die zusätzliche schwierige Wörter enthält.


