import argparse
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from gensim.summarization import summarize


def record_audio(duration: int, samplerate: int, filename: str) -> None:
    """Record audio from the default device."""
    print(f"Recording {duration} seconds...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    sf.write(filename, audio, samplerate)


def transcribe(filename: str) -> str:
    """Transcribe the given WAV file using Whisper (SpeechRecognition)."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_whisper(audio, language="en")
    except Exception:
        # Fallback to Google if whisper model unavailable
        return recognizer.recognize_google(audio)


def summarize_text(text: str) -> str:
    """Return a short summary of the text."""
    try:
        return summarize(text)
    except ValueError:
        return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Record audio and summarize it")
    parser.add_argument("duration", type=int, help="Recording duration in seconds")
    parser.add_argument("--samplerate", type=int, default=44100, help="Sampling rate")
    parser.add_argument("--out", default="meeting.wav", help="Output WAV file")
    parser.add_argument("--summary", default="summary.txt", help="Summary output file")
    args = parser.parse_args()

    record_audio(args.duration, args.samplerate, args.out)
    text = transcribe(args.out)
    summary = summarize_text(text)
    with open(args.summary, "w") as f:
        f.write(summary)
    print("Summary written to", args.summary)


if __name__ == "__main__":
    main()
