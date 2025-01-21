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
    - **Code-Beispiel_bert.py**: Beispiel für die Verwendung eines vortrainierten Modells **`deepset/gelectra-base-germanquad`**. Dieses Modell ist auf [Hugging Face verfügbar](https://huggingface.co/deepset/gelectra-base-germanquad)
    - **worteinteilung.py**: Ein Skript zur Wortaufteilung.
    - **grundwortschatz.txt**: Die Ursprungsversion von **grundwortschatz2.txt**, die eine Liste schwieriger Wörter enthält.
    - **schwierigeWörter_mit_NER_CodeBeispiel.py**: Beispielcode zur Worterkennung mit Named Entity Recognition (NER).
    - **test1.py**: Überprüft, ob Wörter in der Liste der schwierigen Wörter enthalten sind und führt danach eine NER-Analyse durch.
  
  - **logs**: Enthält Log-Dateien, die beim Ausführen der Datei **"training model" > "model fine tuning"** generiert werden.

  - **training model**: Dieser Ordner enthält die folgenden Dateien:
    - **evaluation.py**: Wird verwendet, um die Leistung des trainierten Modells zu bewerten.
    - **model fine tuning.py**: Hier wird das Modell mit dem SQuAD-Datensatz feinabgestimmt.
    - **testing fine tuned model.py**: Wird verwendet, um das feinabgestimmte Modell zu testen.

- **.gitattributes**: Diese Datei trackt eine große Datei, die nicht normalerweise auf github hochgeladen werden kann.

- **Aufgaben**: Enthält die Aufgabenverteilung innerhalb unseres Teams.

- **Readme.md**: Diese Datei.



- **app.py**: Die Streamlit-basierte Webanwendung.

- **grundwortschatz2.txt**: Die erweiterte Version der Datei **grundwortschatz.txt**, die zusätzliche schwierige Wörter enthält.





## Ausführung der Website (app.py)

### Anforderungen:
- Python
- Streamlit: `pip install streamlit`
- Streamlit Lottie: `pip install streamlit_lottie`
- SpeechRecognition: `pip install SpeechRecognition`
- Transformers: `pip install transformers`
- Google Translate (Version 4.0.0-rc1): `pip install googletrans==4.0.0-rc1`
- Torch: `pip install torch`
- PyAudio: `pip install pyaudio`

### Um die Website zu starten, gebe folgendes im Terminal ein:

```bash
python -m streamlit run app.py
```

> Hinweis: `python -m` ist optional, falls Streamlit nicht als globale Variable definiert ist.


## Ausführung der `model fine tuning.py` im "training model"-Ordner

### Anforderungen:
- Python
- Datasets: `pip install datasets`
- Transformers: `pip install transformers`
- Torch: `pip install torch`

### Um das Modell zu fine-tunen, gebe folgendes im Terminal ein:

```bash
python "training model/model fine tuning.py"
```
> Hinweis: Stelle sicher, dass du die richtigen Python-Pakete installiert hast, du im richtigen directory bist und der SQuAD-Datensatz korrekt verfügbar ist.


## Ausführung der `evaluation.py` im "training model"-Ordner

### Anforderungen:
- Python
- **Scikit-learn**: `pip install scikit-learn`
- **Transformers**: `pip install transformers`
- **Datasets**: `pip install datasets`
- **Torch**: `pip install torch`

### Um das Modell zu evaluieren, gebe folgendes im Terminal ein:
```bash
python "training model/evaluation.py"
```
> Hinweis: Stelle sicher, dass du die richtigen Python-Pakete installiert hast, du im richtigen directory bist und der SQuAD-Datensatz korrekt verfügbar ist.


## Ausführung der `testing fine tuned model.py` im "training model"-Ordner

### Anforderungen:
- Python
- **Transformers**: `pip install transformers`
- **Torch**: `pip install torch`

### Um das Modell zu evaluieren, gebe folgendes im Terminal ein:
```bash
python "training model/testing fine tuned model.py"
```
> Hinweis: Stelle sicher, dass du die richtigen Python-Pakete installiert hast, du im richtigen directory bist und der SQuAD-Datensatz korrekt verfügbar ist.


## Ausführung der `Worteinteilung.py` im "history"-Ordner

### Anforderungen:
- Python
- **Requests**: `pip install requests`
- **re**: `pip install re`

### Um das Modell zu evaluieren, gebe folgendes im Terminal ein:
```bash
python "history/Worteinteilung.py"
```
> Hinweis: Stelle sicher, dass du die richtigen Python-Pakete installiert hast, du im richtigen directory bist und die Grundwortschatz im richtigen Ordner ist.
>

## Ausführung ´schwierigeWörter_mit_NER_Code_Beispiel` im "history"-Ordner"
### Anforderungen:

- Python 3.8 oder höher
- Benötigte Python-Bibliotheken:
- Streamlit: pip install streamlit
- Transformers: pip install transformers
- NLTK: pip install nltk
- Requests: pip install requests
