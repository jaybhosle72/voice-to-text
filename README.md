# 🎙️ VoiceScribe — Audio to Text

> A sleek, locally-running speech-to-text web app powered by OpenAI Whisper and Flask.  
> **No API key. No internet. No cost. 100% private.**

---

## ✨ Features

- 🎤 **Live Microphone** — Real-time transcription using your browser's Web Speech API
- 📁 **Audio File Upload** — Drag & drop any audio file and get an instant transcript
- 🌍 **10+ Indian Languages** — English (India), Hindi, Marathi, Tamil, Telugu, Bengali, and more
- ⚡ **Powered by Whisper** — OpenAI's state-of-the-art speech recognition model, runs locally
- 📋 **Copy & Download** — Copy transcript to clipboard or download as `.txt`
- 🔒 **Fully Private** — Your audio never leaves your machine
- 🎨 **Modern UI** — Dark theme with smooth animations and waveform visualizer

---

## 🖥️ Demo

| Live Microphone | Audio File Upload |
|---|---|
| Click **Start Listening**, speak, see text appear in real-time | Drop any audio file, hit **Transcribe**, get your text |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI Model | OpenAI Whisper (runs locally) |
| Frontend | HTML, CSS, Vanilla JS |
| Live Mic | Web Speech API (browser built-in) |
| File Handling | Werkzeug |

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- ffmpeg

### Step 1 — Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/voicescribe.git
cd voicescribe
```

### Step 2 — Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Install ffmpeg

**Linux / Ubuntu:**
```bash
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**  
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

### Step 4 — Run the app
```bash
python app.py
```

Then open your browser and go to: **http://localhost:5000**

> ⚠️ First run will automatically download the Whisper `base` model (~140MB). This is a one-time download.

---

## 📁 Project Structure

```
voicescribe/
│
├── app.py                  # Flask backend — handles file upload & Whisper transcription
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend — UI, live mic, file upload, animations
└── uploads/                # Temporary folder for audio files (auto-created, auto-cleaned)
```

---

## 🎯 Supported Audio Formats

`mp3` · `wav` · `ogg` · `m4a` · `flac` · `mp4` · `webm`  
Max file size: **50MB**

---

## 🌐 Browser Support for Live Mic

The live microphone feature uses the **Web Speech API** which is supported in:

| Browser | Supported |
|---|---|
| Google Chrome | ✅ Yes |
| Microsoft Edge | ✅ Yes |
| Firefox | ❌ No |
| Safari | ⚠️ Partial |

> For audio file transcription (Whisper), all browsers work fine.

---

## 🔧 Configuration

You can change the Whisper model size in `app.py`:

```python
model = whisper.load_model("base")  # options: tiny, base, small, medium, large
```

| Model | Speed | Accuracy | Size |
|---|---|---|---|
| tiny | Fastest | Good | ~75MB |
| base | Fast | Better | ~145MB |
| small | Medium | Great | ~483MB |
| medium | Slow | Excellent | ~1.5GB |
| large | Slowest | Best | ~3GB |

---

## 🚀 Future Improvements

- [ ] Speaker diarization (who said what)
- [ ] Timestamp support in transcripts
- [ ] Export as `.srt` subtitle file
- [ ] Deploy to cloud (AWS / GCP / Railway)
- [ ] Support for YouTube URL transcription

---

## 👨‍💻 Author

**Jay** — CS Engineering Student  
Built as a portfolio project to learn Flask + AI integration.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) — Speech recognition model
- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) — Browser live mic support
