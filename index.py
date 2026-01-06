import yt_dlp
import os



def afficher_progression(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        print(f"📦 {p} | Vitesse: {speed}", end="\r")

def telecharger(url):
    ydl_opts_info = {'quiet': True, 'extract_flat': 'in_playlist'}
    
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info = ydl.extract_info(url, download=False)
    
    if 'entries' in info:
        playlist_title = info.get('title', 'Playlist')
        os.makedirs(playlist_title, exist_ok=True)
        outtmpl = f'{playlist_title}/%(playlist_index)s - %(title)s.%(ext)s'
        print(f"📁 Playlist détectée : {playlist_title}")
    else:
        outtmpl = '%(title)s.%(ext)s'
        print(f"🎬 Vidéo détectée : {info['title']}")

    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': outtmpl,
        'progress_hooks': [afficher_progression],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = input("🔗 Entrez l'URL YouTube : ")
telecharger(url)   

