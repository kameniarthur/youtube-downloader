import yt_dlp

ydl_opts = {
    'format': 'bestvideo+bestaudio',  # Télécharge vidéo + audio
    'merge_output_format': 'mp4',    # Fusionne en MP4
    'outtmpl': '%(title)s.%(ext)s',
}
url = input("Entrez l'URL de la vidéo YouTube à télécharger : ")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])   