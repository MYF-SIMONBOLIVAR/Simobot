import streamlit as st
import base64

# Función para codificar imágenes locales en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Cargar imagen del avatar y del logo
img_bot_base64 = get_base64_image("Simobot.PNG")
img_logo_base64 = get_base64_image("logo.png")

# CSS personalizado
st.markdown("""
    <style>
        body {
            background-color: #e6f0ff;
        }
        .stApp {
            background-color: #e6f0ff;
        }
        .bot-avatar-center {
            display: flex;
            justify-content: center;
            margin-top: -10px;
            margin-bottom: 20px;
        }
        .bot-avatar-center img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 3px solid white;
            box-shadow: 0 0 8px rgba(0,0,0,0.15);
        }
        .chat-iframe {
            width: 100%;
            height: 650px;
            border-radius: 16px;
            border: none;
        }
        .chat-container {
            margin-top: 40px;
            margin-bottom: 60px;
        }
        .responsive-logo {
            text-align: center;
            margin-top: 20px;
        }
        .responsive-logo img {
            max-width: 80%;
            height: auto;
            width: 180px;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 style='text-align: center; color: #19287f;'>Muelles y Frenos Simón Bolívar</h1>", unsafe_allow_html=True)

# Línea decorativa
st.markdown("<hr style='border: none; height: 4px; background-color: #fab70e;'>", unsafe_allow_html=True)

# Subtítulo
st.markdown("<h2 style='text-align: center; color:#fab70e;'> Chatbot Soporte TI 🧠 </h2>", unsafe_allow_html=True)

# Avatar centrado
st.markdown(f"""
    <div class="bot-avatar-center">
        <img src="{img_bot_base64}" alt="Simonbot">
    </div>
""", unsafe_allow_html=True)

# Descripción
st.markdown("""
    <div style="text-align: center; font-size: 16px; color: #333;">
        Este es el canal principal de soporte técnico de la empresa. A través de este chatbot puedes resolver preguntas frecuentes, consultar información útil y realizar solicitudes básicas de asistencia.<br><br>
        En caso de que tu solicitud no pueda ser atendida por el asistente virtual, solicita el link para montar un ticket y pueda ser escalada al personal humano del área TIC para su seguimiento.
    </div>
""", unsafe_allow_html=True)

# Línea decorativa
st.markdown("<hr style='border: none; height: 4px; background-color: #fab70e;'>", unsafe_allow_html=True)

# Chat embebido responsivo
st.markdown(f"""
    <div class="chat-container">
        <iframe
            src="https://copilotstudio.microsoft.com/environments/Default-e5b459bb-3dbe-4999-a52e-cbf1ceddb166/bots/cr28b_agente/webchat?__version__=2"
            class="chat-iframe"
            allow="microphone; camera">
        </iframe>
    </div>
""", unsafe_allow_html=True)

# Línea decorativa inferior
st.markdown("<hr style='border: none; height: 4px; background-color: #fab70e;'>", unsafe_allow_html=True)

# Logo centrado y responsivo
st.markdown(f"""
    <div class="responsive-logo">
        <img src="{img_logo_base64}" alt="Logo">
    </div>
""", unsafe_allow_html=True)

# Pie de página
st.markdown("""
    <div style="text-align: center; margin-top: 20px; color: #19277f;">
        <p>© 2025 Muelles y Frenos Simón Bolívar. Todos los derechos reservados.</p>
    </div>
""", unsafe_allow_html=True)

