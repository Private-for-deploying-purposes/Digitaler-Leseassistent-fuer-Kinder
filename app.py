import streamlit as st
from streamlit_lottie import st_lottie
import speech_recognition as sr
import requests
import json

# -----------------------------------------------------------------------------
# 1. Set up page config (Optional: affects favicon, layout, etc.)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Digitaler Leseassistent",
    page_icon="📚",
    layout="centered"
)

# -----------------------------------------------------------------------------
# 2. Function to load Lottie animations (with caching)
# -----------------------------------------------------------------------------
@st.cache_data
def load_lottie_url(url: str):
    """Loads a Lottie animation from a provided URL and returns JSON data."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Fehler beim Laden der Animation: {e}")
        return None

# -----------------------------------------------------------------------------
# 3. Inline CSS for styling
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    .stApp {
        /* Hintergrundfarbe für sanftes Gelb */
        background: linear-gradient(to top, #fffacd, #dff0d8);
        font-family: 'Comic Neue', sans-serif;
    }
    .title {
        color: #4CAF50;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }
    .subtitle {
        color: #d35400;
        font-size: 28px;
        text-align: center;
        font-style: italic;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    .stPageLink,.stButton > button {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        color: #333 !important;
        font-size: 20px;
        font-weight: bold;
        border-radius: 20px;
        padding: 10px 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s, background 0.3s;
    }.stElementContainer  {
        padding-top: 0rem;
        padding-bottom: 0rem;
        margin-top: 0rem;
        margin-bottom: 0rem;
    }
    .stPageLink:hover, .stButton > button:hover {
        background: linear-gradient(90deg, #FFA500, #FF4500);
        color: white !important;
        box-shadow: 0px 8px 15px rgba(255, 140, 0, 0.6);
        transform: scale(1.1);
    }
    [data-testid="stSidebar"] {
        background-color: #ffeb99 !important;
        color: #333;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .custom-button {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        color: black;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .custom-button:hover {
        background: linear-gradient(90deg, #FFA500, #FF4500);
        color: white;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------------------------------------------
# 4. A dictionary for "difficult" words
# -----------------------------------------------------------------------------
wort_definitionen = {
    "kompliziert": "Etwas, das schwer zu verstehen oder zu machen ist.",
    "technologie": "Dinge, die mit Maschinen oder Computern gemacht werden.",
    "phänomen": "Etwas Besonderes, das man sehen oder beobachten kann.",
    "wissenschaft": "Das Lernen über die Natur und die Welt durch Experimente."
}

# -----------------------------------------------------------------------------
# 5. Helper function: Text analysis + highlight difficult words
# -----------------------------------------------------------------------------
def analyse_text(text: str):
    """Highlights words found in wort_definitionen and shows definitions below."""
    schwierige_worte = [
        wort for wort in text.split() 
        if wort.lower().strip(".,!?;:") in wort_definitionen
    ]

    if schwierige_worte:
        highlighted_text = text
        for wort in schwierige_worte:
            lower_wort = wort.lower().strip(".,!?;:")
            highlighted_text = highlighted_text.replace(
                wort,
                f"<span style='color: red; font-weight: bold;'>{wort}</span>"
            )

        st.markdown("### 📄 Hervorgehobener Text:")
        st.markdown(highlighted_text, unsafe_allow_html=True)

        st.markdown("<h4>Erkannte schwierige Wörter:</h4>", unsafe_allow_html=True)
        for wort in schwierige_worte:
            lower_wort = wort.lower().strip(".,!?;:")
            st.markdown(f"- **{wort.capitalize()}**: {wort_definitionen[lower_wort]}")
    else:
        st.success("Keine schwierigen Wörter gefunden!")

# -----------------------------------------------------------------------------
# 6. Define our two pages as functions
# -----------------------------------------------------------------------------

def start_page():
    """
    This page is our 'Startseite'. It welcomes users and offers the 'Los geht's!'
    button to switch to the 'Wörter-Entdecker' page.
    """
    st.markdown("<h1 class='title'>📚 Willkommen bei deinem Digitalen Leseassistenten! ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Hier kannst du schwierige Wörter verstehen und deine Lesereise starten. Lass uns gemeinsam spannende Texte entdecken! 🚀</p>", unsafe_allow_html=True)
    with st.container():
        # Load & show the clouds animation
        lottie_clouds_url = "https://raw.githubusercontent.com/mxhmxt/Digitaler-Leseassistent-fuer-Kinder/refs/heads/main/Animation%20-%201736697073312.json"
        lottie_clouds = load_lottie_url(lottie_clouds_url)
        if lottie_clouds:
            st_lottie(lottie_clouds, height=150, width=700, key="clouds")

        # Load & show the kids animation
        lottie_kids_url = "https://raw.githubusercontent.com/mxhmxt/Digitaler-Leseassistent-fuer-Kinder/refs/heads/main/Kids%20reading%20books.json"
        lottie_kids = load_lottie_url(lottie_kids_url)
        if lottie_kids:
            st_lottie(lottie_kids, height=300, key="kids")

    # "Los geht's!" button -> switch to Wörter-Entdecker
    #st.button("🚀 Los geht's!",on_click=woerter_entdecker_page)
    st.page_link(woerter_entdecker, label="Los geht's!", icon="🚀")    

def woerter_entdecker_page():
    """
    This page is the 'Wörter-Entdecker', allowing users to input text,
    highlight difficult words, and also handle speech recognition.
    """
    st.markdown("<h1 class='title'>🔍 Wörter-Entdecker</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Entdecke neue Wörter und finde Antworten auf spannende Fragen!</p>", unsafe_allow_html=True)

    # Load & show the book animation
    alternative_animation_url = "https://raw.githubusercontent.com/mxhmxt/Digitaler-Leseassistent-fuer-Kinder/refs/heads/main/Animation%20-%201736695644411.json"
    alternative_animation = load_lottie_url(alternative_animation_url)
    if alternative_animation:
        st_lottie(
            alternative_animation,
            height=200,
            key="book_animation",
            speed=1.2,
            loop=True
        )
    else:
        st.error("Animation konnte nicht geladen werden.")

    # Text input for manual analysis
    st.markdown("### 📝 Gib hier deinen Text ein:")
    text_input = st.text_area("Deinen Text hier eingeben...", height=100)

    col1, col2 = st.columns(2)

    # Button 1: Start speech recognition
    with col1:
        if st.button("🎤 Spracheingabe starten"):
            recognizer = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    st.info("🎤 Spracheingabe läuft... Bitte sprechen Sie.")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=10)
                    recognized_text = recognizer.recognize_google(audio, language="de-DE")
                    st.success(f"Erkannter Text: {recognized_text}")
                    analyse_text(recognized_text)

            except sr.UnknownValueError:
                st.error("Entschuldigung, ich konnte nichts verstehen. Bitte versuche es erneut.")
            except sr.RequestError as e:
                st.error(f"Fehler bei der Verbindung: {e}")
            except sr.WaitTimeoutError:
                st.error("Timeout-Fehler: Keine Sprache erkannt. Bitte sprich innerhalb der erlaubten Zeit.")

    # Button 2: Manually analyze text input
    with col2:
        if st.button("🔍 Los!"):
            if text_input.strip():
                analyse_text(text_input)
            else:
                st.error("Bitte gib einen Text ein!")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Questions section
    st.markdown("### ❓ Fragen beantworten")
    question_input = st.text_input("Gib hier deine Frage ein:")
    if st.button("🧠 Frage beantworten"):
        # Placeholder: Here you could integrate an actual Q&A logic
        st.success("Frage beantwortet!")

# -----------------------------------------------------------------------------
# 7. Wrap each function in an `st.Page` object, then pass them to `st.navigation`
# -----------------------------------------------------------------------------
startseite = st.Page(start_page, title="Startseite", icon="🏠")
woerter_entdecker = st.Page(
    woerter_entdecker_page, 
    title="Wörter-Entdecker", 
    icon="🔍"
)

# Create the navigation, pass the list of pages. We call .run() to execute
nav = st.navigation([startseite, woerter_entdecker])
nav.run()
