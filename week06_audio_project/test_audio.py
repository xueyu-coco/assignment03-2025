import pyaudio
import numpy as np
import time

# Audio configuration parameters
CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
DURATION = 3  # Play for 3 seconds

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)

print("Playing 3 seconds of white noise...")

# Generate and play white noise
for i in range(int(RATE / CHUNK * DURATION)):
    # Generate random audio data (white noise)
    data = np.random.randn(CHUNK).astype(np.float32) * 0.1
    stream.write(data.tobytes())

print("Playback completed")

# Clean up resources
stream.stop_stream()
stream.close()
p.terminate()