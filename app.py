import streamlit as st
from PIL import Image
import base64
from io import BytesIO

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
        .training-img-container {
            text-align: center;
            margin: 1rem 0;
        }
        .training-img {
            max-width: 60%;
            border-radius: 0.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: zoom-in;
        }
        .training-img:hover {
            transform: scale(1.3);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            z-index: 100;
            position: relative;
        }
        .zoom-img-container {
            text-align: center;
            margin: 1rem 0;
        }
        .zoom-img {
            max-width: 60%;
            border-radius: 0.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: zoom-in;
        }
        .zoom-img:hover {
            transform: scale(1.3);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            z-index: 100;
            position: relative;
        }
        .interactive-card {
            background: linear-gradient(135deg, #f0f9ff 0%, #f5f0ff 100%);
            padding: 1.5rem;
            border-radius: 0.8rem;
            margin: 1rem 0;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .interactive-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        .interactive-card h4 {
            color: #1a237e;
            margin-bottom: 0.8rem;
            font-size: 1.1rem;
        }
        .interactive-card p, .interactive-card li {
            font-size: 0.95rem;
            line-height: 1.6;
        }
        .problem-statement {
            background: linear-gradient(135deg, #ffebee 0%, #fff3e0 100%);
            padding: 1.8rem;
            border-radius: 1rem;
            border-left: 6px solid #f44336;
            margin-bottom: 1.5rem;
        }
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 0.8rem;
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
    st.markdown("""
    <div class="problem-statement">
        <h3 style="color: #d32f2f;">⚠️ El Problema de la Diabetes</h3>
        <p>El proyecto aborda la grave problemática de la diabetes como uno de los principales desafíos de salud pública mundial. El peligro principal radica en que muchas personas viven con la enfermedad durante años sin ser diagnosticadas, lo que retrasa tratamientos que podrían prevenir complicaciones graves. Aunque los análisis de sangre tradicionales son precisos, requieren tiempo, dinero e infraestructura de laboratorio, lo que limita el acceso a chequeos preventivos masivos.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("✨ Propuesta del Proyecto")
    st.markdown("""
    <p>El equipo desarrolla un sistema de software híbrido que utiliza Inteligencia Artificial para calcular la probabilidad de riesgo de diabetes en usuarios mediante:</p>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="interactive-card">
            <div class="feature-icon">👁️</div>
            <h4>Módulo de Visión por Computadora</h4>
            <p>Analiza imágenes de la piel para detectar patrones visuales asociados con la diabetes (como manchas oscuras en pliegues corporales, indicativas de <strong>acantosis nigricans</strong>, un marcador de resistencia a la insulina).</p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="interactive-card">
            <div class="feature-icon">📊</div>
            <h4>Módulo de Datos Estructurados</h4>
            <p>Procesa respuestas de una encuesta digital que recopila información sobre:</p>
            <ul style="margin-top: 0.5rem;">
                <li>Antecedentes familiares</li>
                <li>Hábitos alimenticios</li>
                <li>Edad</li>
                <li>Nivel de actividad física</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("🔧 Enfoque Técnico")
    tech_cols = st.columns(4)
    tech_info = [
        {"icon": "🧠", "title": "Deep Learning", "desc": "Para el análisis automatizado de imágenes médicas"},
        {"icon": "🖥️", "title": "Interfaz de Usuario", "desc": "Funcional para cargar imágenes y visualizar diagnósticos"},
        {"icon": "💾", "title": "Base de Datos", "desc": "Para gestionar usuarios y registros de salud"},
        {"icon": "✅", "title": "Validación", "desc": "Mecanismos de gestión de errores para estabilidad"}
    ]
    for i, col in enumerate(tech_cols):
        with col:
            st.markdown(f"""
            <div class="interactive-card">
                <div class="feature-icon">{tech_info[i]['icon']}</div>
                <h4>{tech_info[i]['title']}</h4>
                <p style="font-size: 0.9rem;">{tech_info[i]['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.subheader("🌟 Impacto Esperado")
    st.markdown("""
    <div class="interactive-card" style="background: linear-gradient(135deg, #e8f5e9 0%, #e3f2fd 100%); border-left: 5px solid #4caf50;">
        <p>El proyecto demuestra cómo el desarrollo de software inteligente puede integrarse al sector salud, creando soluciones accesibles que funcionan como un <strong>sistema de alerta temprana</strong>, motivando a las personas a buscar atención médica oportuna antes de que la enfermedad avance.</p>
    </div>
    """, unsafe_allow_html=True)
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

def img_to_base64(img):
    """Convert PIL Image to base64 string"""
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

with st.expander("🖼️ Ver Diagrama de Confusión del Modelo", expanded=False):
    try:
        confusion_img = Image.open("CUADRO_CONFUSION.jpeg")
        img_base64 = img_to_base64(confusion_img)
        st.markdown("""
        <div class="zoom-img-container">
            <img src="data:image/jpeg;base64,%s" class="zoom-img" alt="Diagrama de Confusión del Modelo de IA">
            <p style="margin-top: 0.5rem; font-size: 0.95rem; color: #37474f;">Diagrama de Confusión del Modelo de IA</p>
        </div>
        """ % img_base64, unsafe_allow_html=True)
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
        "Paso 1: ",
        "Paso 2: ",
        "Paso 3: ",
        "Paso 4: ",
        "Paso 5: ",
        "Paso 6: ",
        "Paso 7: ",
        "Paso 8: ",
        "Paso 9: ",
        "Paso 10: ",
        "Paso 11: ",
        "Paso 12: ",
        "Paso 13: "
    ]
    
    for img_path, caption in zip(training_images, captions):
        try:
            img = Image.open(img_path)
            img_base64 = img_to_base64(img)
            st.markdown(f"""
            <div class="training-img-container">
                <img src="data:image/jpeg;base64,{img_base64}" class="training-img" alt="{caption}">
                <p style="margin-top: 0.5rem; font-size: 0.95rem; color: #37474f;">{caption}</p>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"No se pudo cargar la imagen {img_path}")
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
