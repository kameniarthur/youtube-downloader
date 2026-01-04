# 🎥 Téléchargeur YouTube en Python

Un outil simple et efficace pour télécharger des vidéos YouTube avec audio intégré, à des fins éducatives.

## 📋 Fonctionnalités

- Téléchargement de vidéos YouTube en haute qualité
- **Audio + Vidéo fusionnés** automatiquement via FFmpeg
- Support des formats MP4 (vidéo) et MP3 (audio uniquement)
- Interface en ligne de commande claire
- Gestion des erreurs et messages d’aide

## ⚙️ Fonctionnement

Utilise la bibliothèque `yt-dlp` pour :
1. Extraire les flux vidéo et audio séparés
2. Télécharger les meilleurs formats disponibles
3. Fusionner automatiquement avec FFmpeg en MP4

## 🛠️ Installation

### 1. Prérequis
- Python 3.7+
- [FFmpeg](https://ffmpeg.org/) (pour la fusion audio/vidéo)

Sur Arch Linux :
```bash
sudo pacman -S ffmpeg   