from pyo import *
import time

s = Server().boot()
s.start()

# Create simple synthesizer
freq = Sig(440)  # Initial frequency 440Hz
amp = Sig(0.3)   # Volume

# Oscillator
osc = Sine(freq=freq, mul=amp).out()

print("Synthesizer started!")
print("Press Ctrl+C to stop")

try:
    while True:
        # Interactive logic can be added here
        # For example: change frequency based on user input
        time.sleep(0.1)
except KeyboardInterrupt:
    s.stop()