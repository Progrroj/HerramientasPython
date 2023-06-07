from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Titulo: ", yt.title)

# Descargar el audio
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download("C:/Users/agust/Escritorio/videos programacion")  # Ruta a la carpeta donde se desea guardar el audio

# Descargar audio y video
# La resolucion maxima en la que descarga es de 720p, al ser mayor a esta, YT lo hace por separado
video_stream = yt.streams.get_highest_resolution()
video_stream.download("C:/Users/agust/Escritorio/videos programacion")  

# IMPORTANTE, recordar comentar el codigo dependiendo que se desea descargar