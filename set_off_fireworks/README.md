# Voice-Controlled Fireworks 🎆🎤

An interactive voice-controlled fireworks display that responds to your voice input in real-time. The louder you speak, the bigger and more spectacular the fireworks become!

## 🌟 Features

### 🎤 Voice Control
- **Volume-Reactive Fireworks**: Speak into your microphone to launch fireworks
- **Dynamic Sizing**: Louder voice = Bigger fireworks, Quieter voice = Smaller fireworks
- **Real-time Audio Analysis**: Advanced voice volume detection and processing
- **Smart Cooldown**: Intelligent timing to prevent firework spam

### 🎆 Spectacular Visual Effects
- **Realistic Rocket Launch**: Rockets fly from bottom to target with trails
- **Multi-Color Explosions**: 5 different color schemes (Red-Orange-Yellow, Blue-Purple-Pink, Green variations, Orange variations, Purple-Pink)
- **Particle Physics**: Gravity-affected particles with realistic movement
- **Glow Effects**: Beautiful particle glow and fade effects
- **Animated Background**: Twinkling stars in a night sky

### 🔊 Dynamic Sound Effects
- **Size-Based Audio**: Different sound effects for different firework sizes
- **Realistic Explosion Sounds**: Procedurally generated explosion audio with harmonics and noise
- **Volume Scaling**: Louder fireworks produce louder, deeper explosion sounds
- **Crackle Effects**: Large fireworks include authentic crackling sounds
- **Multi-layered Audio**: Base explosion + harmonics + noise + crackle for realism

### 🎨 Interactive Interface
- **Real-time Volume Indicator**: Visual bar showing current voice volume
- **Color-coded Feedback**: Green (good level), Yellow (loud), Red (very loud)
- **Live Statistics**: Track total fireworks launched and active fireworks
- **On-screen Instructions**: Clear usage guidelines displayed

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Microphone connected and working
- Audio drivers properly configured

### Installation

1. **Navigate to project directory**:
   ```bash
   cd set_off_fireworks
   ```

2. **Activate virtual environment**:
   ```bash
   # Windows
   .\venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python voice_fireworks.py
```

## 🎮 How to Use

### Controls
- **🎤 Speak into microphone**: Launch fireworks (volume determines size)
- **SPACE**: Manual test firework launch
- **ESC**: Exit the application

### Voice Instructions
1. **Speak normally**: Creates medium-sized fireworks
2. **Speak loudly**: Creates large, spectacular fireworks
3. **Whisper**: Creates small, delicate fireworks
4. **Stay quiet**: No fireworks launch

### Volume Indicator
- **Gray Bar**: Too quiet (below threshold)
- **Green Bar**: Good volume level
- **Yellow Bar**: Loud volume (big fireworks)
- **Red Bar**: Very loud (maximum fireworks)

## 🔧 Technical Details

### Audio Processing
- **Sample Rate**: 44.1 kHz
- **Chunk Size**: 1024 samples
- **Volume Analysis**: RMS (Root Mean Square) calculation
- **Threshold Detection**: Automatic noise floor adjustment

### Sound Effects System
- **Audio Generation**: Real-time procedural sound synthesis
- **Sound Sample Rate**: 22.05 kHz for effects
- **Dynamic Frequency**: 60-250 Hz based on firework size
- **Harmonic Layers**: Base tone + 2nd/3rd harmonics for richness
- **Noise Component**: Realistic explosion texture
- **Envelope Shaping**: Exponential decay with size-based duration
- **Crackle Effects**: High-frequency sparkle sounds for large fireworks

### Firework Physics
- **Launch Speed**: 8-12 pixels/frame (based on size)
- **Explosion Size**: 50-150 particles (volume-dependent)
- **Particle Count**: 30-80 particles per firework
- **Gravity Effect**: 0.2 pixels/frame² downward acceleration
- **Particle Decay**: 98% size reduction per frame

### Performance
- **Frame Rate**: 60 FPS
- **Resolution**: 1200x800 (configurable)
- **Memory Efficient**: Automatic particle cleanup
- **CPU Optimized**: Efficient audio processing

## 📁 Project Structure

```
set_off_fireworks/
├── venv/                    # Virtual environment
├── voice_fireworks.py       # Main application
├── audio_loopback.py        # Audio testing utility
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## � Customization

### Adjusting Sensitivity
Edit `voice_fireworks.py`:
```python
self.volume_threshold = 0.01    # Minimum volume to trigger
self.max_volume = 0.5          # Maximum expected volume
self.firework_cooldown = 0.3   # Time between fireworks (seconds)
```

### Adding New Colors
```python
color_sets = [
    [(R, G, B), (R, G, B), (R, G, B)],  # Your custom colors
    # Add more color combinations
]
```

### Modifying Firework Size
```python
self.explosion_size = int(50 + size_multiplier * 100)    # Explosion radius
self.particle_count = int(30 + size_multiplier * 50)     # Number of particles
```

## 🔍 Troubleshooting

### Common Issues

#### No Fireworks Launching
- Check microphone permissions
- Verify microphone is working (test in other apps)
- Adjust `volume_threshold` if too sensitive/insensitive
- Try speaking closer to microphone

#### Audio Errors
- Ensure no other apps are using microphone
- Check audio drivers are up to date
- Try different sample rates in code
- Restart application

#### Performance Issues
- Close other applications
- Lower resolution in code
- Reduce particle count
- Check CPU usage

#### No Sound Detection
```python
# Test microphone independently
python audio_loopback.py
```

### System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- Integrated audio
- Microphone input

**Recommended:**
- Python 3.9+
- 8GB RAM
- Dedicated graphics
- High-quality microphone

## 🎯 Future Enhancements

- **Multiple Voice Recognition**: Different voices trigger different firework types
- **Music Synchronization**: Sync fireworks to background music
- **Mobile App**: Create smartphone version
- **VR Support**: Virtual reality fireworks experience
- **Social Features**: Share firework shows
- **AI Choreography**: Machine learning firework patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🎊 Enjoy the Show!

Have fun creating your own voice-controlled fireworks display! Try different speaking patterns, volumes, and timing to create unique firework shows.

---

*Created: October 10, 2025*  
*Voice-Controlled Fireworks - Where Your Voice Lights Up the Sky!* 🎆✨