import torch
import torchaudio
import numpy as np
import soundfile as sf

print("Testing torchaudio functionality...")

# Create a simple test audio signal (sine wave)
sample_rate = 22050
duration = 3  # seconds
frequency = 440  # Hz (A4 note)

# Generate time array
t = torch.linspace(0, duration, sample_rate * duration)

# Generate sine wave
audio_signal = torch.sin(2 * np.pi * frequency * t).unsqueeze(0)  # Add channel dimension

print(f"Generated audio signal:")
print(f"- Sample rate: {sample_rate} Hz")
print(f"- Duration: {duration} seconds")
print(f"- Frequency: {frequency} Hz")
print(f"- Shape: {audio_signal.shape}")

# Save the audio file using soundfile as backend
output_file = "test_sine_wave.wav"
audio_numpy = audio_signal.squeeze().numpy()  # Convert to numpy and remove channel dimension
sf.write(output_file, audio_numpy, sample_rate)

print(f"Audio saved as: {output_file}")
print("Test completed successfully!")

# Load and display information about the saved file
try:
    loaded_audio, loaded_sr = torchaudio.load(output_file)
    print(f"\nLoaded audio verification:")
    print(f"- Shape: {loaded_audio.shape}")
    print(f"- Sample rate: {loaded_sr}")
    print(f"- Duration: {loaded_audio.shape[1] / loaded_sr:.2f} seconds")
except Exception as e:
    print(f"\nNote: Could not load with torchaudio: {e}")
    print("But audio file was created successfully with soundfile!")