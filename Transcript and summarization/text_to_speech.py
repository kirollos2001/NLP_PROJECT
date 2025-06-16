"""
Text‑to‑Speech generation (Arabic XTTS demo)
"""

import torchaudio
from TTS.api import TTS
import os
import logging

# Enable verbose logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Define paths
summary_path = "/content/summary.txt"
model_path = "/content/EGTTS-V0.1"
config_path = "/content/EGTTS-V0.1/config.json"
speaker_wav = "/content/EGTTS-V0.1/speaker_reference.wav"
output_path = "/content/xtts_audio.wav"

# Verify paths exist
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model directory {model_path} does not exist")
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file {config_path} does not exist")
if not os.path.exists(speaker_wav):
    raise FileNotFoundError(f"Speaker reference {speaker_wav} does not exist")

# Initialize the model
print("Loading model...")
model = TTS(model_path=model_path, config_path=config_path, progress_bar=True).to("cuda" if torch.cuda.is_available() else "cpu")

with open(summary_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Inference...")
out = model.tts(
    text=text,
    language="ar",
    speaker_wav=speaker_wav,
    temperature=0.75,
)


torchaudio.save(output_path, torch.tensor(out).unsqueeze(0), 24000)

display(Audio(output_path, autoplay=True))