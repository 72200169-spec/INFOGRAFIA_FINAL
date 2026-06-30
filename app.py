import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Detector de Diabetes - Proyecto IA",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.03); }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        .main {
            background-color: #f0f4f8;
        }
        .stApp {
            background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        }
        h1 {
            color: #1a237e;
            font-family: 'Segoe UI', sans-serif;
            font-weight: 700;
            animation: fadeIn 1s ease-out;
        }
        h2 {
            color: #283593;
            font-family: 'Segoe UI', sans-serif;
        }
        h3 {
            color: #37474f;
            font-family: 'Segoe UI', sans-serif;
        }
        p, div, span, li {
            color: #263238 !important;
        }
        .css-1d391kg {
            padding-top: 2rem;
        }
        .card {
            background-color: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.15);
            margin-bottom: 1.5rem;
            animation: fadeIn 1s ease-out;
        }
        .author-card {
            background: linear-gradient(135deg, #bbdefb 0%, #e1bee7 100%);
            padding: 2rem 1.5rem;
            border-radius: 1rem;
            margin-bottom: 1rem;
            color: #263238 !important;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            animation: fadeIn 0.8s ease-out, float 3s ease-in-out infinite;
            transition: all 0.3s ease;
        }
        .author-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        .result-box {
            background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
            border-left: 5px solid #ff9800;
            padding: 1.5rem;
            border-radius: 0.5rem;
        }
        .dataset-link {
            background-color: #e3f2fd;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 0.8rem;
        }
        .title-icon {
            animation: pulse 2s ease-in-out infinite;
            display: inline-block;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style="text-align: center;">
        <span class="title-icon">🤖</span> Sistema de Detección de Diabetes mediante Análisis de Piel
    </h1>
""", unsafe_allow_html=True)
st.markdown("""
    <p style="text-align: center; font-size: 1.3rem; color: #283593; font-weight: 600;">
        Proyecto de Inteligencia Artificial
    </p>
""", unsafe_allow_html=True)

st.markdown("<hr style='border: 2px solid #1565c0; margin: 2rem 0;'>", unsafe_allow_html=True)

st.header("👥 Autores del Proyecto")
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    st.markdown('''
        <div class="author-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">👨‍💻</div>
            <div style="font-weight: 700; font-size: 1.05rem;">Uman Apaza Jhoseph Alfredo</div>
        </div>
    ''', unsafe_allow_html=True)
with col2:
    st.markdown('''
        <div class="author-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">👨‍💻</div>
            <div style="font-weight: 700; font-size: 1.05rem;">Cussi Valenzuela Rodrigo Eduardo</div>
        </div>
    ''', unsafe_allow_html=True)
with col3:
    st.markdown('''
        <div class="author-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">👨‍💻</div>
            <div style="font-weight: 700; font-size: 1.05rem;">Acurio Jara Paul Gonzalo</div>
        </div>
    ''', unsafe_allow_html=True)
with col4:
    st.markdown('''
        <div class="author-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.8rem;">👨‍💻</div>
            <div style="font-weight: 700; font-size: 1.05rem;">Loaiza Martinez Carlos Eduardo</div>
        </div>
    ''', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

with st.expander("📋 Ver Descripción del Proyecto", expanded=True):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    Este proyecto consiste en un modelo de Inteligencia Artificial entrenado para detectar **Acantosis Nigricans**, 
    una condición de la piel fuertemente asociada con la resistencia a la insulina y el riesgo de desarrollar diabetes tipo 2.
    
    El sistema analiza imágenes de la piel y proporciona resultados de diagnóstico junto con recomendaciones médicas importantes.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("📊 Ver Resultados de Análisis de Piel", expanded=True):
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("⚠️ ACANTOSIS NIGRICANS DETECTADA")
    st.write("""
    Esta condición está fuertemente asociada con resistencia a la insulina.
    
    **Recomendaciones importantes:**
    - Consulta a un endocrinólogo lo antes posible
    - Reduce el consumo de azúcares y carbohidratos refinados
    - Realiza ejercicio físico regular
    - Un diagnóstico temprano puede prevenir el desarrollo de diabetes tipo 2
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("🖼️ Ver Diagrama de Confusión del Modelo", expanded=False):
    try:
        confusion_img = Image.open("CUADRO_CONFUSION.jpeg")
        st.image(confusion_img, caption="Diagrama de Confusión del Modelo de IA", use_container_width=True)
    except Exception as e:
        st.warning("No se pudo cargar la imagen del diagrama de confusión.")

with st.expander("📁 Ver Datasets Utilizados", expanded=False):
    st.markdown('<div class="dataset-link"><a href="https://universe.roboflow.com/sliit-gvlap/acanthosis-nigricans-detection-xempk" target="_blank" style="color: #1a237e;">Dataset 1: Acanthosis Nigricans Detection - Roboflow</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="dataset-link"><a href="https://universe.roboflow.com/naia/acantosis-nigricans/dataset/7" target="_blank" style="color: #1a237e;">Dataset 2: Acantosis Nigricans - Roboflow</a></div>', unsafe_allow_html=True)

with st.expander("⚙️ Proceso de Entrenamiento del Modelo", expanded=False):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    El entrenamiento del modelo se realizó utilizando **Google Colab**, aprovechando los datasets previamente mencionados. 
    A continuación se muestra el proceso paso a paso:
    """)
    
    # Load and display training images in order
    training_images = ["1.jpeg", "2.jpeg", "3.jpeg", "4.jpeg", "5.jpeg", "6.jpeg", "7.jpeg", "8.jpeg", "9.jpeg", "10.jpeg", "11.jpeg", "12.jpeg", "13.jpeg"]
    captions = [
        "Paso 1: Inicio del entorno de Colab",
        "Paso 2: Carga y preparación de los datasets",
        "Paso 3: Configuración del modelo de IA",
        "Paso 4: Entrenamiento del modelo",
        "Paso 5: Evaluación de métricas",
        "Paso 6: Resultados y exportación del modelo",
        "Paso 7: Pruebas iniciales del modelo",
        "Paso 8: Validación con datos reales",
        "Paso 9: Ajuste de hiperparámetros",
        "Paso 10: Evaluación final",
        "Paso 11: Exportación del modelo entrenado",
        "Paso 12: Integración con la aplicación web",
        "Paso 13: Despliegue final del sistema"
    ]
    
    for img_path, caption in zip(training_images, captions):
        try:
            img = Image.open(img_path)
            st.image(img, caption=caption, use_container_width=True)
        except Exception as e:
            st.warning(f"No se pudo cargar la imagen {img_path}")
    
    st.write("""
    Este proceso nos permitió desarrollar un modelo accesible para los usuarios, con el objetivo de ayudar a conocer su estado de salud
    de forma temprana a través del análisis de la piel para detectar Acantosis Nigricans y prevenir la diabetes tipo 2.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("🌐 Ver Sitio Web del Proyecto", expanded=True):
    st.markdown("""
    <div class="card">
        <h3>Accede a la aplicación en línea:</h3>
        <a href="https://paginaweb-amir.onrender.com" target="_blank" style="font-size: 1.2rem; color: #1a237e;">
            👉 https://paginaweb-amir.onrender.com
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
st.caption("© 2026 - Universidad Continental - Grupo 'Los Lederes'")
