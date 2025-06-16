# Modular Colab Project

This repo was **auto‑generated** on 2025‑06‑15 from a Colab notebook.
The monolithic notebook has been refactored into modular Python packages.

## Module overview

| File | Purpose |
|------|---------|
| `transcription_and_diarization.py` | ASR + speaker diarization |
| `cleaning_preprocessing.py` | Arabic transcript cleanup and normalization |
| `summarization_google.py` | Summarization using Google Generative Language API |
| `text_to_speech.py` | Arabic XTTS inference demo |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Common files to ignore |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Then open the folder in **Cursor** or **VS Code** and start hacking!

### End‑to‑end example

```python
from transcription_and_diarization import transcribe_and_diarize
from cleaning_preprocessing import clean_arabic_transcript
from summarization_google import summarize
from text_to_speech import generate_audio  # you'll create this wrapper

segments = transcribe_and_diarize("interview.mp3")
raw_text = "\n".join([s["text"] for s in segments])
cleaned = clean_arabic_transcript(raw_text)
summary = summarize(cleaned)
audio_path = generate_audio(summary)
print("Done! 🎉", audio_path)
```

## License

MIT (see LICENSE if you add one)
