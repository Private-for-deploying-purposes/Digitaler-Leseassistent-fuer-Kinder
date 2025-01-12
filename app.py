from streamlit_lottie import st_lottie
import speech_recognition as sr
import streamlit as st
from PIL import Image
import requests
import json
import os

# ---- Funktion zum Laden einer Lottie-Animation ----
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# ---- CSS für Styling ----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    html, body {
        background: url('https://images.unsplash.com/photo-1531427186611-ecfd6d936c79?fit=crop&w=1920&q=80') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Comic Neue', sans-serif;
    }
    .title {
        color: #4CAF50;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #FF8C42;
        font-size: 24px;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #FFA500, #FF4500);
        transform: scale(1.1);
    }
    .highlight {
        background-color: #FFFF99;
        padding: 3px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---- Wolken-Schwebebewegung hinzufügen ----
st.markdown("""
    <style>
    @keyframes floatClouds {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    .cloud-animation {
        animation: floatClouds 20s linear infinite;  /* Schwebende Bewegung */
    }
    </style>
""", unsafe_allow_html=True)

# ---- Abstand zwischen Wolken und Inhalten reduzieren ----
st.markdown("""
    <style>
    .stApp > div:first-child {
        margin-top: -20px;  /* Verringerter Abstand nach oben */
    }
    </style>
""", unsafe_allow_html=True)  

# ---- Navigation ----
st.sidebar.title("Navigation")
page = st.sidebar.radio("Seite auswählen:", ["Startseite", "Wörter-Entdecker"])

# ---- Startseite ----
if page == "Startseite":
    st.markdown("<h1 class='title'>📚 Willkommen bei deinem Digitalen Leseassistenten! ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Hier kannst du schwierige Wörter verstehen und deine Lesereise starten. Lass uns gemeinsam spannende Texte entdecken! 🚀</p>", unsafe_allow_html=True)

    # ---- Wolken-Animation hinzufügen ----
    from streamlit_lottie import st_lottie
    import json

    # Funktion zum Laden der Lottie-Animation
    def load_lottie_url(url):
        import requests
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Wolken-Animation laden
    lottie_clouds_url = "https://raw.githubusercontent.com/mxhmxt/Digitaler-Leseassistent-fuer-Kinder/refs/heads/main/Animation%20-%201736697073312.json"
    lottie_clouds = load_lottie_url(lottie_clouds_url)
    if lottie_clouds:
        st_lottie(
            lottie_clouds,
            height=200,  # Höhe der Animation
            width=1000,  # Breite der Animation
            key="clouds"
        )
    else:
        st.error("Wolken-Animation konnte nicht geladen werden.")

    # ---- Hauptanimation für die Startseite ----
    lottie_url = "https://raw.githubusercontent.com/mxhmxt/Digitaler-Leseassistent-fuer-Kinder/refs/heads/main/Kids%20reading%20books.json"
    lottie_animation = load_lottie_url(lottie_url)
    if lottie_animation:
        st_lottie(lottie_animation, height=400, key="kids_reading_animation")
    else:
        st.error("Animation konnte nicht geladen werden.")

    # Buttons
    st.markdown("<p style='text-align:center;'>Kinder entdecken die Welt des Lesens! 🌟</p>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Schwierige Wörter erklären"):
            st.experimental_set_query_params(page="Textanalyse", feature="wortanalyse")
            st.session_state.page = "Textanalyse"
            st.session_state.feature = "wortanalyse"
    with col2:
        if st.button("❓ Fragen beantworten"):
            st.experimental_set_query_params(page="Textanalyse", feature="fragen")
            st.session_state.page = "Textanalyse"
            st.session_state.feature = "fragen"


# ---- Wörter-Entdecker ----
elif page == "Wörter-Entdecker":
    st.markdown("<h1 class='title'>🔍 Wörter-Entdecker</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Entdecke neue Wörter und finde Antworten auf spannende Fragen!</p>", unsafe_allow_html=True)

    # Animation für Textanalyse: Bücher oder Lesesymbol
    alternative_animation_url = "https://raw.githubusercontent.com/mxhmxt/Digitaler-Leseassistent-fuer-Kinder/refs/heads/main/Animation%20-%201736695644411.json"  # Animation mit Buch
    alternative_animation = load_lottie_url(alternative_animation_url)

    # Animation anzeigen
    if alternative_animation:
       st_lottie(
           alternative_animation,
           height=300,
           key="book_animation",
           speed=1.2,
           loop=True
        )
    else:
        st.error("Animation konnte nicht geladen werden.")


    # Eingabefeld für Textanalyse
    st.markdown("### 📝 Gib hier deinen Text ein:")
    text_input = st.text_area("Deinen Text hier eingeben...", height=100)

    # Wörterbuch für schwierige Wörter
    wort_definitionen = {
        "kompliziert": "Etwas, das schwer zu verstehen oder zu machen ist.",
        "technologie": "Dinge, die mit Maschinen oder Computern gemacht werden.",
        "phänomen": "Etwas Besonderes, das man sehen oder beobachten kann.",
        "wissenschaft": "Das Lernen über die Natur und die Welt durch Experimente."
    }

    # Funktion zum Hervorheben schwieriger Wörter
    def analyse_text(text):
        schwierige_worte = [wort for wort in text.split() if wort.lower() in wort_definitionen]
        if schwierige_worte:
            st.markdown("<h4>Erkannte schwierige Wörter:</h4>", unsafe_allow_html=True)
            for wort in schwierige_worte:
                st.markdown(f"- <span class='highlight'>{wort.capitalize()}</span>: {wort_definitionen[wort.lower()]}", unsafe_allow_html=True)
        else:
            st.success("Keine schwierigen Wörter gefunden!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗣️ Spracheingabe starten"):
            st.info("Spracheingabe-Funktion wird bald verfügbar!")
    with col2:
        if st.button("🔍 Los!"):
            if text_input:
                analyse_text(text_input)
            else:
                st.error("Bitte gib zuerst einen Text ein!")

    # Eingabefeld für Fragen
    st.markdown("### ❓ Fragen beantworten")
    question_input = st.text_input("Gib hier deine Frage ein:")
    if st.button("🧠 Frage beantworten"):
        st.success("Frage beantwortet!")