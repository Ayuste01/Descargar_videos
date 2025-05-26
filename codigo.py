from pytube import YouTube
import os
pip install streamlit

def descargar_video(url, carpeta='descargas'):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    print(f"Descargando video: {yt.title}")
    video.download(output_path=carpeta)
    print("¡Video descargado con éxito!\n")

def descargar_audio(url, carpeta='descargas'):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    print(f"Descargando audio: {yt.title}")
    archivo = audio.download(output_path=carpeta)

    # Renombrar a .mp3
    base, ext = os.path.splitext(archivo)
    nuevo_archivo = base + '.mp3'
    os.rename(archivo, nuevo_archivo)
    print("¡Audio descargado con éxito!\n")

def main():
    print("=== DESCARGADOR DE YOUTUBE ===")
    url = input("🔗 Ingresa la URL del video de YouTube: ")
    print("¿Qué deseas descargar?")
    print("1. Video")
    print("2. Solo audio (MP3)")

    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        descargar_video(url)
    elif opcion == "2":
        descargar_audio(url)
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
