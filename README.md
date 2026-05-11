# eemg-app-
Todo lo relacionado al curso AI Fundamentos de Programacion OBS proyecto final
# Aplicación de Análisis de Satisfacción y Resúmenes con IA

Este proyecto es una herramienta web interactiva diseñada para procesar texto mediante Inteligencia Artificial, ofreciendo análisis de sentimiento multilingüe y generación de resúmenes ejecutivos.

## 🚀 Descripción General
La aplicación utiliza modelos avanzados de Procesamiento de Lenguaje Natural (NLP) para ayudar a las empresas a entender el feedback de sus clientes y sintetizar grandes volúmenes de información de manera eficiente.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.x
- **Interfaz de Usuario:** [Streamlit](https://streamlit.io/) (Layout Wide)
- **Análisis de Sentimiento:** `nlptown/bert-base-multilingual-uncased-sentiment` vía Hugging Face Transformers.
- **Generación de Contenido (LLM):** Google Gemini 1.5 Flash.
- **Gestión de Modelos:** `st.cache_resource` para carga eficiente de modelos.

## 📦 Arquitectura del Proyecto
La interfaz está dividida en dos módulos principales:

### 1. Análisis de Satisfacción (BERT)
Evalúa la experiencia del cliente en una escala de 1 a 5 estrellas.
- **Entrada:** Texto libre con la experiencia del usuario.
- **Salida:** Clasificación por estrellas, puntaje de confianza decimal y barra de progreso visual.

### 2. Generador de Resúmenes (Gemini)
Sintetiza artículos o textos extensos utilizando el modelo de última generación de Google.
- **Entrada:** Textos largos (artículos, reportes, etc.).
- **Lógica:** Prompting estructurado para respuestas concisas en español.
- **Seguridad:** Manejo de errores para tiempos de espera agotados (Timeout) y validación de campos vacíos.

## ⚙️ Configuración e Instalación

### Requisitos Previos
Necesitarás una **API KEY** de Google Generative AI. Puedes obtenerla en [Google AI Studio](https://aistudio.google.com/).

### Instalación Local
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   cd TU_REPOSITORIO
2. Instalar dependencias
  pip install -r requirements.txt
3. Ejecutar la aplicación
   streamlit run app.py

Para evitar exponer claves sensibles en el código, esta aplicación utiliza Streamlit Secrets. Si despliegas la app en Streamlit Cloud:
Ve a los ajustes de tu aplicación en el dashboard de Streamlit.
En la sección Secrets, añade tu clave de la siguiente forma:
  GEMINI_API_KEY = "tu_clave_aqui"

El código llamará automáticamente a esta variable mediante st.secrets["GEMINI_API_KEY"]

Estructura de Archivos
app.py: Código principal de la aplicación Streamlit.
requirements.txt: Lista de dependencias de Python necesarias.
README.md: Documentación del proyecto.

👤 Autor
Proyecto Final EEMG - Ingeniería en Sistemas Electrónicos
