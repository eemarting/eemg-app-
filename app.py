import streamlit as st
import google.generativeai as genai
from transformers import pipeline

# codigo en phyton

# Configuración de la página
st.set_page_config(page_title="Proyecto final", layout="wide")
st.title("Proyecto final, Satisfacción del Cliente, Resumenes de temas con GEMINI ")

# --- CONFIGURACIÓN DE MODELOS ---
# 1. Configurar Gemini (Necesitarás tu API KEY)
# genai.configure(api_key="TU_API_KEY_AQUI")
model_gemini = genai.GenerativeModel('gemini-2.5-flash')

# 2. Configurar Hugging Face (Análisis de sentimiento)
# Este modelo se descarga la primera vez que se ejecuta
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_analysis = load_sentiment_model()

# --- INTERFAZ DE USUARIO ---
tab1, tab2 = st.tabs(["📊 Encuesta de Satisfacción", "📝 Resumen de Temas GEMINI"])

# --- OPERACIÓN A: ANÁLISIS DE SENTIMIENTO ---
with tab1:
    st.header("Encuesta de Satisfacción")
    text_input = st.text_area("Describenos como fue tu experiencia (Español, Inglés, etc.):", key="sentiment_in")

    if st.button("Enviar"):
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
    st.header("Generador de Resumenes con GEMINI")
    long_text = st.text_area("Pega aquí el artículo o texto largo (Max. 200 caracteres):", height=200)

if st.button("Enviar"):
    if long_text:
        with st.spinner("Gemini está procesando... por favor espera."):
            try:
                # Intentamos la generación con tiempo extendido
                prompt = f"Resume de forma concisa: {long_text}"
                response = model_gemini.generate_content(
                    prompt, 
                    request_options={"timeout": 60}
                )
                st.subheader("Resumen:")
                st.write(response.text)
            except Exception as e:
                if "DeadlineExceeded" in str(e):
                    st.error("La conexión tardó demasiado. Por favor, intenta con un texto más corto o presiona el botón de nuevo.")
                else:
                    st.error(f"Hubo un problema con la API: {e}")
    else:
        st.warning("El campo de texto está vacío.")
