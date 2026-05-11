import streamlit as st
import google.generativeai as genai
from transformers import pipeline

# Configuración de la página
st.set_page_config(page_title="Proyecto final EEMG", layout="wide")
st.title("Proyecto final: Satisfacción del Cliente y Resúmenes con Gemini")

# --- CONFIGURACIÓN DE MODELOS ---
# 1. Configurar Gemini (Asegúrate de poner tu API KEY)
# genai.configure(api_key="clave")
model_gemini = genai.GenerativeModel('gemini-2.5-flash')

# 2. Configurar Hugging Face (Análisis de sentimiento)
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_analysis = load_sentiment_model()

# --- INTERFAZ DE USUARIO ---
tab1, tab2 = st.tabs(["📊 Encuesta de Satisfacción", "📝 Resumen de Temas GEMINI"])

# --- TAB 1: ANÁLISIS DE SENTIMIENTO ---
with tab1:
    st.header("Encuesta de Satisfacción")
    text_input = st.text_area("Descríbenos como fue tu experiencia:", key="sentiment_in")

    # Agregamos una 'key' única para diferenciar este botón
    if st.button("Enviar Feedback", key="btn_sentiment"):
        if text_input:
            result = sentiment_analysis(text_input)[0]
            label = result['label']
            score = result['score']

            st.info(f"Resultado: {label}")
            st.write(f"Confianza del modelo: {score:.2f}")
            st.progress(score)
        else:
            st.warning("Por favor, ingresa un texto.")

# --- TAB 2: RESUMEN CON GEMINI ---
with tab2:
    st.header("Generador de Resúmenes con Gemini")
    long_text = st.text_area("Pega aquí el artículo o texto largo (Máx 200 caracteres):", height=200, key="summary_in")

    # El botón ahora está DENTRO del bloque 'with tab2' e incluye una 'key' única
    if st.button("Generar Resumen", key="btn_gemini"):
        if long_text:
            with st.spinner("Gemini está procesando... por favor espera."):
                try:
                    prompt = f"Resume de forma concisa y en español: {long_text}"
                    response = model_gemini.generate_content(
                        prompt, 
                        request_options={"timeout": 60}
                    )
                    st.subheader("Resumen:")
                    st.write(response.text)
                except Exception as e:
                    if "DeadlineExceeded" in str(e):
                        st.error("La conexión tardó demasiado. Reintenta con menos texto.")
                    else:
                        st.error(f"Hubo un problema con la API: {e}")
        else:
            st.warning("El campo de texto está vacío.")
