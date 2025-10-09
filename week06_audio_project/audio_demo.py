import torch
import torchaudio
import soundfile as sf
import numpy as np
from pathlib import Path

print("Audio Generation Demo with PyTorch")
print("=" * 40)

# Check device availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

def generate_tone(frequency, duration, sample_rate=22050):
    """Generate a pure tone"""
    t = torch.linspace(0, duration, int(sample_rate * duration))
    tone = torch.sin(2 * np.pi * frequency * t)
    return tone, sample_rate

def generate_chord(frequencies, duration, sample_rate=22050):
    """Generate a chord from multiple frequencies"""
    t = torch.linspace(0, duration, int(sample_rate * duration))
    chord = torch.zeros_like(t)
    for freq in frequencies:
        chord += torch.sin(2 * np.pi * freq * t)
    chord = chord / len(frequencies)  # Normalize
    return chord, sample_rate

# Generate different audio samples
print("\n1. Generating pure tones...")

# A4 note (440 Hz)
a4_tone, sr = generate_tone(440, 2.0)
sf.write("tone_a4.wav", a4_tone.numpy(), sr)
print(f"✓ Generated A4 tone (440 Hz) - saved as tone_a4.wav")

# C major chord (C4, E4, G4)
c_major_frequencies = [261.63, 329.63, 392.00]  # C4, E4, G4
c_major_chord, sr = generate_chord(c_major_frequencies, 3.0)
sf.write("chord_c_major.wav", c_major_chord.numpy(), sr)
print(f"✓ Generated C major chord - saved as chord_c_major.wav")

print("\n2. Generating synthesized sequences...")

# Generate a simple melody
melody_notes = [
    (261.63, 0.5),  # C4
    (293.66, 0.5),  # D4
    (329.63, 0.5),  # E4
    (349.23, 0.5),  # F4
    (392.00, 1.0),  # G4
    (392.00, 0.5),  # G4
    (440.00, 1.0),  # A4
]

melody_audio = torch.tensor([])
for freq, duration in melody_notes:
    note, _ = generate_tone(freq, duration)
    melody_audio = torch.cat([melody_audio, note])

sf.write("simple_melody.wav", melody_audio.numpy(), sr)
print(f"✓ Generated simple melody - saved as simple_melody.wav")

print("\n3. Audio file information:")
files_created = ["tone_a4.wav", "chord_c_major.wav", "simple_melody.wav"]

for filename in files_created:
    if Path(filename).exists():
        # Load and get info
        audio_data, sample_rate = sf.read(filename)
        duration = len(audio_data) / sample_rate
        print(f"  {filename}:")
        print(f"    - Duration: {duration:.2f} seconds")
        print(f"    - Sample rate: {sample_rate} Hz")
        print(f"    - Samples: {len(audio_data)}")

print("\n" + "=" * 40)
print("Audio generation completed successfully!")
print("You can play these WAV files with any audio player.")

# Demonstrate some basic audio processing
print("\n4. Basic audio processing demo...")

# Load one of our generated files and apply simple effects
try:
    original_audio, sr = sf.read("tone_a4.wav")
    
    # Apply fade in/out effect
    fade_samples = int(0.1 * sr)  # 0.1 second fade
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)
    
    processed_audio = original_audio.copy()
    processed_audio[:fade_samples] *= fade_in
    processed_audio[-fade_samples:] *= fade_out
    
    sf.write("tone_a4_faded.wav", processed_audio, sr)
    print("✓ Applied fade in/out effect - saved as tone_a4_faded.wav")
    
except Exception as e:
    print(f"Error in audio processing: {e}")

print("\nDemo completed! 🎵")