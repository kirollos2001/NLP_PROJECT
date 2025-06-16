"""Pipeline orchestrator

Example CLI:
    python main.py --input audio.mp3
"""
import argparse
from transcription_and_diarization import transcribe_and_diarize
from cleaning_preprocessing import clean_arabic_transcript
from summarization_google import summarize
from text_to_speech import generate_audio as tts_generate_audio  # define in text_to_speech

def main():
    parser = argparse.ArgumentParser(description="End‑to‑end Arabic interview pipeline")
    parser.add_argument("--input", required=True, help="Path to input audio/video file")
    args = parser.parse_args()

    segments = transcribe_and_diarize(args.input)
    raw_text = "\n".join([s['text'] for s in segments])
    cleaned = clean_arabic_transcript(raw_text)
    summary = summarize(cleaned)
    audio_path = tts_generate_audio(summary)
    print("✅ Success! Audio summary saved to", audio_path)

if __name__ == "__main__":
    main()
