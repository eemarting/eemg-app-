import streamlit as st
import google.generativeai as genai
from transformers import pipeline

# codigo en phyton

# Configuración de la página
st.set_page_config(page_title="Proyecto final, Satisfacción del Cliente, Resumenes de temas con GEMINI", layout="wide")
st.title("Proyecto final, Satisfacción del Cliente, Resumenes de temas con GEMINI ")

# --- CONFIGURACIÓN DE MODELOS ---
# 1. Configurar Gemini (Necesitarás tu API KEY)
# genai.configure(api_key="TU_API_KEY_AQUI")
model_gemini = genai.GenerativeModel('gemini-pro')

# 2. Configurar Hugging Face (Análisis de sentimiento)
# Este modelo se descarga la primera vez que se ejecuta
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_analysis = load_sentiment_model()

# --- INTERFAZ DE USUARIO ---
tab1, tab2 = st.tabs(["📊 Satisfacción del Cliente mal=1 Excelente=5", "📝 Resumen de Temas GEMINI"])

# --- OPERACIÓN A: ANÁLISIS DE SENTIMIENTO ---
with tab1:
    st.header("Satisfacción del cliente")
    text_input = st.text_area("Describe tu experiencia (Español, Inglés, etc.):", key="sentiment_in")

    if st.button("Analizar Sentimiento"):
        if text_input:
            result = sentiment_analysis(text_input)[0]
            label = result['label']
            score = result['score']

            st.info(f"Resultado: {label}")
            st.progress(score)
        else:
            st.warning("Por favor, ingresa un texto.")

# --- OPERACIÓN B: RESUMEN CON GEMINI ---
with tab2:
    st.header("Resumen de Texto con Gemini")
    long_text = st.text_area("Pega aquí el artículo o texto largo:", height=200)

    if st.button("Generar Resumen"):
        if long_text:
            with st.spinner("Gemini está procesando..."):
                prompt = f"Por favor, resume el siguiente texto de forma concisa y en puntos clave: {long_text}"
                response = model_gemini.generate_content(prompt)
                st.subheader("Resumen:")
                st.write(response.text)
        else:
            st.warning("El campo de texto está vacío.")
