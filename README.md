# EchoNote

EchoNote is a simple script for recording meetings and automatically generating a short summary.

## Requirements
- Python 3.8+
- `sounddevice`
- `soundfile`
- `speechrecognition`
- `gensim`

## Usage

1. Install the dependencies:

```bash
pip install sounddevice soundfile SpeechRecognition gensim
```

2. Record a meeting and produce a summary:

```bash
python echo_note.py 60 --out meeting.wav --summary summary.txt
```

Replace `60` with the number of seconds to record. The script will create a WAV file and a text summary.

### Capturing system audio

To capture audio from Zoom or Google Meet you may need to enable a loopback recording device (such as "Stereo Mix" on Windows or a virtual audio cable). Set that device as the default recording source before running the script.
