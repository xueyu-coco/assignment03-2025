import torch
import torchaudio
import soundfile as sf
import pyttsx3
import numpy as np
from pathlib import Path

print("Text-to-Speech Demo using PyTTS3")
print("=" * 40)

# Check device availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize TTS engine
engine = pyttsx3.init()

# Configure TTS settings
voices = engine.getProperty('voices')
if voices:
    print(f"Available voices: {len(voices)}")
    for i, voice in enumerate(voices[:3]):  # Show first 3 voices
        print(f"  {i}: {voice.name}")

# Set voice properties
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

def text_to_speech_file(text, filename):
    """Convert text to speech and save as file"""
    try:
        engine.save_to_file(text, filename)
        engine.runAndWait()
        return True
    except Exception as e:
        print(f"Error generating speech: {e}")
        return False

# English example
print("\n1. Generating English speech...")
english_text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
if text_to_speech_file(english_text, "test-english.wav"):
    print("✓ Generated English speech - saved as test-english.wav")
else:
    print("✗ Failed to generate English speech")

# Additional examples
print("\n2. Generating additional speech samples...")

texts_and_files = [
    ("Hello world! This is a test of text to speech functionality.", "hello-world.wav"),
    ("Python is an amazing programming language for audio processing.", "python-audio.wav"),
    ("Real-time audio processing with PyAudio and PyTorch is powerful.", "realtime-audio.wav")
]

for text, filename in texts_and_files:
    if text_to_speech_file(text, filename):
        print(f"✓ Generated speech - saved as {filename}")
    else:
        print(f"✗ Failed to generate {filename}")

print("\n3. Audio file information:")
wav_files = ["test-english.wav", "hello-world.wav", "python-audio.wav", "realtime-audio.wav"]

for filename in wav_files:
    if Path(filename).exists():
        try:
            # Load and get info
            audio_data, sample_rate = sf.read(filename)
            duration = len(audio_data) / sample_rate if len(audio_data.shape) == 1 else len(audio_data) / sample_rate
            print(f"  {filename}:")
            print(f"    - Duration: {duration:.2f} seconds")
            print(f"    - Sample rate: {sample_rate} Hz")
            if len(audio_data.shape) == 1:
                print(f"    - Samples: {len(audio_data)}")
            else:
                print(f"    - Samples: {len(audio_data)} (channels: {audio_data.shape[1]})")
        except Exception as e:
            print(f"  {filename}: Error reading file - {e}")

print("\n4. Demonstrating voice synthesis with different rates...")

# Try different speech rates
rates = [100, 150, 200]
for rate in rates:
    engine.setProperty('rate', rate)
    filename = f"speech-rate-{rate}.wav"
    text = f"This speech is at rate {rate} words per minute."
    if text_to_speech_file(text, filename):
        print(f"✓ Generated speech at rate {rate} - saved as {filename}")

print("\n" + "=" * 40)
print("Text-to-Speech demo completed successfully!")
print("You can play these WAV files with any audio player.")
print("\nNote: This uses pyttsx3 instead of the unavailable chatterbox library.")
print("pyttsx3 provides cross-platform text-to-speech capabilities.")