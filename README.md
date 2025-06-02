# 🎵 YoutubeAutomationScript-Project
Winter 2024 YouTube Music Downloading Automation Project by Adarsh Bellamane.
A simple terminal-based Python automation script to download **music videos** or **playlists** from YouTube.  
Built using `pytubefix` and a custom regex engine `regex_utils.py` for extracting video IDs.

> ⚠️ **Note:** This script works best with music content. For non‑music videos, accuracy is not guaranteed.

## ⚙️ Requirements

- Python 3.6+
- [`pytubefix`](https://github.com/pytube/pytube) (a maintained fork of pytube)

Install dependencies:

```bash
pip install pytubefix
```

---

## 🚀 How to Use

### 🎧 Download a Single Song

```bash
python script.py
```

1. Answer **no** when prompted for a playlist.  
2. Enter the song name _and_ artist when asked.  
3. The highest‑resolution video is downloaded to the folder set in `DOWNLOAD_DIR`.

### 📃 Download an Entire Playlist

```bash
python script.py
```

1. Answer **yes** when prompted for a playlist.  
2. Paste the full YouTube playlist URL.  
3. Every video in the playlist is downloaded to `DOWNLOAD_DIR`.

---

## ✏️ Configuration

Open **`script.py`** and edit the line:

```python
DOWNLOAD_DIR = '/Users/YourName/Downloads'  # ← change this!
```

Set it to any absolute path where you want the videos saved.

---

## 🔍 How It Works

1. **Search Query** – The script constructs a YouTube search URL that appends `" audio"` to bias results toward music.
2. **Custom Regex** – `regex_utils.py` scans the raw HTML for `/watch?v=` followed by an 11‑character video ID (without using the `re` module).
3. **Downloading** – `pytubefix` fetches the video, selects the highest‑resolution stream, and saves it locally with a progress bar.

---

## 🛑 Disclaimer

- This project is provided **for educational purposes** only.  
- Downloading or distributing copyrighted material without permission may violate YouTube’s Terms of Service and/or local laws.  
- Use responsibly.

---
