import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Audio configuration
CHUNK = 512  # Reduced buffer size for faster response
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

class AudioVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.volume_data = [0] * 100  # Store last 100 volume values for display
        self.line, = self.ax.plot(self.volume_data)
        self.ax.set_ylim(0, 1)
        self.ax.set_title('Real-time Audio Volume Visualization - Ultra High Sensitivity')
        self.ax.set_ylabel('Volume Level')
        self.ax.set_xlabel('Time Axis')
        self.ax.grid(True, alpha=0.3)  # Add grid lines
        
        # Initialize PyAudio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )
    
    def calculate_volume(self, data):
        """Calculate volume level of audio data"""
        audio_data = np.frombuffer(data, dtype=np.int16)
        volume = np.sqrt(np.mean(audio_data**2)) / 32768.0  # Normalize to 0-1
        
        # Enhance sensitivity: use exponential function and amplification factor
        volume = volume * 8.0  # Amplify by 8x (increased from 3x)
        volume = np.power(volume, 0.3)  # Use cube root for even more sensitivity to small sounds
        volume = min(volume, 1.0)  # Ensure not exceeding 1.0
        
        return volume
    
    def update(self, frame):
        """Update the chart"""
        # Read audio data
        data = self.stream.read(CHUNK, exception_on_overflow=False)
        
        # Calculate volume
        volume = self.calculate_volume(data)
        
        # Update data
        self.volume_data.append(volume)
        if len(self.volume_data) > 100:  # Update to 100 data points
            self.volume_data.pop(0)
        
        # Update chart
        self.line.set_ydata(self.volume_data)
        
        # Change line color based on volume level
        if volume > 0.5:  # Lowered threshold for red
            self.line.set_color('red')  # High volume in red
        elif volume > 0.2:  # Lowered threshold for orange
            self.line.set_color('orange')  # Medium volume in orange
        else:
            self.line.set_color('blue')  # Low volume in blue
            
        self.ax.set_title(f'Real-time Volume Visualization - Current Volume: {volume:.3f} - Ultra High Sensitivity')
        
        return self.line,
    
    def start(self):
        """Start the visualization"""
        print("Starting voice-controlled visualization...")
        print("Please speak into the microphone or make sounds")
        print("Close the window to exit")
        
        ani = FuncAnimation(self.fig, self.update, blit=True, interval=20)  # Even faster update: 20ms
        plt.show()
    
    def close(self):
        """Clean up resources"""
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    visualizer = AudioVisualizer()
    try:
        visualizer.start()
    finally:
        visualizer.close()