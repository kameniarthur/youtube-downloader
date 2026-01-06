import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import os

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("500x300")
        self.folder_path = tk.StringVar(value=os.getcwd())
        self.create_widgets()

    def create_widgets(self):
        # URL
        tk.Label(self.root, text="URL YouTube :").pack(pady=5)
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        # Dossier
        folder_frame = tk.Frame(self.root)
        tk.Label(folder_frame, text="Dossier :").pack(side="left")
        tk.Entry(folder_frame, textvariable=self.folder_path, width=30).pack(side="left", padx=5)
        tk.Button(folder_frame, text="Parcourir", command=self.choose_folder).pack(side="left")
        folder_frame.pack(pady=10)

        # Bouton téléchargement
        tk.Button(self.root, text="Télécharger", command=self.start_download).pack(pady=10)

        # Barre de progression
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Statut
        self.status_label = tk.Label(self.root, text="Prêt", fg="blue")
        self.status_label.pack(pady=5)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def afficher_progression(self, d):
        if d['status'] == 'downloading':
            p = d.get('_percent_str', 'N/A').strip()
            filename = d.get('filename', 'inconnu')
            self.root.after(0, lambda: self.status_label.config(text=f"⏬ {p} - {os.path.basename(filename)}"))
            try:
                value = float(p.replace('%', ''))
                self.root.after(0, lambda: self.progress.config(value=value))
            except:
                pass

    def telecharger(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL")
            return

        ydl_opts_info = {'quiet': True, 'extract_flat': 'in_playlist'}
        try:
            with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
                info = ydl.extract_info(url, download=False)

            outtmpl = os.path.join(self.folder_path.get(), '%(title)s.%(ext)s')
            if 'entries' in info:
                playlist_title = info.get('title', 'Playlist')
                playlist_dir = os.path.join(self.folder_path.get(), playlist_title)
                os.makedirs(playlist_dir, exist_ok=True)
                outtmpl = os.path.join(playlist_dir, '%(playlist_index)s - %(title)s.%(ext)s')

            ydl_opts = {
                'format': 'bestvideo+bestaudio',
                'merge_output_format': 'mp4',
                'outtmpl': outtmpl,
                'progress_hooks': [self.afficher_progression],
            }

            self.progress.config(value=0)
            self.status_label.config(text="Démarrage...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.config(text="✅ Téléchargement terminé !")

        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def start_download(self):
        self.root.after(0, self.telecharger)

root = tk.Tk()
app = YouTubeDownloader(root)
root.mainloop()   