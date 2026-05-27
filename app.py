import json
import streamlit as st

from textblob import TextBlob
from googletrans import Translator
from streamlit_lottie import st_lottie

# CONFIG
st.set_page_config(
    page_title="Análisis de Sentimiento"
)

# FUNCION LOTTIE
def cargar_lottie(ruta):
    with open(ruta, "r") as archivo:
        return json.load(archivo)

# ANIMACIONES
feliz_anim = cargar_lottie("feliz.json")
triste_anim = cargar_lottie("triste.json")
neutral_anim = cargar_lottie("neutral.json")

# TITULO
st.title('Análisis de Sentimiento')

st.image(
    "emoticones.jpg",
    width=250
)

st.subheader(
    "Por favor escribe en el campo de texto la frase que deseas analizar"
)

translator = Translator()

# SIDEBAR
with st.sidebar:

    st.subheader("Polaridad y Subjetividad")

    st.write("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

    Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# ANALISIS
with st.expander('Analizar texto'):

    text = st.text_input('Escribe por favor: ')

    if text:

        translation = translator.translate(
            text,
            src="es",
            dest="en"
        )

        trans_text = translation.text

        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        # POSITIVO
        if polarity > 0:

            st.success(
                'Es un sentimiento Positivo 😊'
            )

            st_lottie(
                feliz_anim,
                width=250
            )

        # NEGATIVO
        elif polarity < 0:

            st.error(
                'Es un sentimiento Negativo 😔'
            )

            st_lottie(
                triste_anim,
                width=250
            )

        # NEUTRAL
        else:

            st.warning(
                'Es un sentimiento Neutral 😐'
            )

            st_lottie(
                neutral_anim,
                width=250
            )
