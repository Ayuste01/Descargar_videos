import streamlit as st
from pytube import YouTube
import os

# Carpeta de descargas
CARPETA_DESCARGA = 'descargas'

def descargar_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        if not os.path.exists(CARPETA_DESCARGA):
            os.makedirs(CARPETA_DESCARGA)
        archivo = stream.download(output_path=CARPETA_DESCARGA)
        return f"✅ Video descargado: {yt.title}"
    except Exception as e:
        return f"❌ Error al descargar video: {e}"

def descargar_audio(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        if not os.path.exists(CARPETA_DESCARGA):
            os.makedirs(CARPETA_DESCARGA)
        archivo = stream.download(output_path=CARPETA_DESCARGA)
        base, ext = os.path.splitext(archivo)
        nuevo_archivo = base + '.mp3'
        os.rename(archivo, nuevo_archivo)
        return f"✅ Audio descargado: {yt.title}"
    except Exception as e:
        return f"❌ Error al descargar audio: {e}"

# Interfaz de Streamlit
st.set_page_config(page_title="YouTube Downloader", layout="centered")
st.title("📥 YouTube Downloader")

url = st.text_input("🎬 Pega aquí la URL del video de YouTube")

modo = st.radio("¿Qué deseas descargar?", ("Video", "Solo audio (MP3)"))

if st.button("Descargar"):
    if url:
        with st.spinner("Descargando..."):
            if modo == "Video":
                resultado = descargar_video(url)
            else:
                resultado = descargar_audio(url)
        st.success(resultado)
    else:
        st.warning("Por favor, ingresa una URL válida.")
