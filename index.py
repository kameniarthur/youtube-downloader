from pytube import YouTube



def telecharger_video(url):
    try:
        yt = YouTube(url)
        print(f"Téléchargement de : {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("✅ Téléchargement terminé !")
    except Exception as e:
        print(f"❌ Erreur : {e}")

# Exemple d'utilisation
lien = input("Entrez l'URL YouTube : ")
telecharger_video(lien)   