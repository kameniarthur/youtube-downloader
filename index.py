import yt_dlp

url = input("Entrez l'URL YouTube : ")
ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': '%(title)s.%(ext)s'
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])   