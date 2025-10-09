# Music Dance Project 🎵🕺

A comprehensive AI-powered music visualization and dance system that creates interactive, real-time dance performances synchronized with music and voice input.

## 🌟 Features

### 🎭 Multiple Dance Styles
- **Human**: Classic stick figure dancer with natural movements
- **Abstract**: Morphing polygonal shapes that dance to the rhythm
- **Robot**: Mechanical movements with joint animations
- **Hip-Hop**: Street dance style with baggy clothes and dynamic moves
- **Ballet**: Elegant poses with tutu and graceful movements
- **Cartoon**: Exaggerated features with big eyes and animated expressions
- **Animal**: Cute animal dancer with ears and tail

### 🎨 Visual Effects
- **Particle System**: Dynamic particles that react to music beats
- **Dynamic Lighting**: Radial glows and light effects on strong beats
- **Rainbow Spectrum**: Color-changing audio visualization bars
- **Background Animation**: Mood-responsive background colors
- **Real-time Audio Visualization**: Live spectrum analysis display

### 🎤 Voice Control Systems
- **Speech Recognition**: Voice command control for dance moves
- **Real-time Voice Response**: Responds to volume, pitch, and speech rate
- **Voice Visualization**: Live voice analysis and feedback

## 📁 Project Structure

```
music_dance/
├── enhanced_dance_visualizer.py    # Main enhanced visualizer with all features
├── dance_visualizer_main.py        # Original dance visualizer
├── fixed_dance_visualizer.py       # Simplified stable version
├── dancer.py                       # Dancer class with multiple styles
├── music_analyzer.py               # Basic music analysis
├── music_analyzer_main.py          # Advanced music feature extraction
├── debug_test.py                   # Simple pygame test
├── simple_dance_test.py            # Basic dance test
├── requirements_dance.txt          # Dependencies for dance features
├── test_music.mp3                  # Sample music file
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Virtual environment** (recommended)
3. **Audio drivers** properly configured
4. **Microphone** (for voice control features)

### Installation

1. **Clone or download** the project files
2. **Navigate** to the music_dance directory:
   ```bash
   cd path/to/music_dance
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements_dance.txt
   ```

4. **Install additional packages** if needed:
   ```bash
   pip install pygame numpy librosa scipy
   ```

### Basic Usage

#### 🎵 Enhanced Dance Visualizer (Recommended)

Run the full-featured visualizer with all dance styles and effects:

```bash
python enhanced_dance_visualizer.py
```

**Features:**
- 7 different dance styles
- Advanced particle effects
- Dynamic lighting
- Music synchronization
- Interactive controls

**Controls:**
- **SPACE**: Play/Pause music
- **ESC**: Exit application
- **Mouse Click**: Change tempo (click position determines BPM)
- **Arrow Keys**: 
  - ↑ Up: Energetic mood
  - ↓ Down: Calm mood
  - ← Left: Neutral mood
  - → Right: Happy mood

#### 🎭 Simple Dance Visualizer

For a lighter version with stable performance:

```bash
python fixed_dance_visualizer.py
```

#### 🔍 Debug and Testing

Test basic pygame functionality:

```bash
python debug_test.py
```

Simple dance animation test:

```bash
python simple_dance_test.py
```

## 🎵 Music Setup

### Adding Your Own Music

1. **Place MP3 files** in the music_dance directory
2. **Rename your file** to `test_music.mp3` or modify the code:
   ```python
   # In enhanced_dance_visualizer.py, line ~200
   music_loaded = self.load_music("your_music_file.mp3")
   ```

### Supported Formats
- **MP3** (recommended)
- **WAV** 
- **OGG**

### Music Analysis Features
- **Tempo detection** (BPM)
- **Beat tracking** 
- **Energy analysis**
- **Mood classification** (energetic, happy, calm, neutral)
- **Onset detection**
- **Spectral analysis**

## 🎤 Voice Control Features

### Voice Commands (voice_command_dancer.py)

Located in the parent directory, supports speech recognition:

```bash
cd ..
python voice_command_dancer.py
```

**Supported Commands:**
- "dance" - Start dancing
- "spin" - Rotate dancers
- "jump" - Make dancers jump
- "stop" - Stop movement
- "bigger" / "smaller" - Change size
- "red" / "blue" / "green" - Change colors

### Real-time Voice Response (voice_dance_controller.py)

Responds to voice characteristics in real-time:

```bash
cd ..
python voice_dance_controller.py
```

**Voice Actions:**
- **🗣️ SHOUT LOUDLY** → Dancers spin and turn red
- **🎵 HIGH PITCH** → Dancers jump and turn green
- **⚡ FAST SPEECH** → Dancers wave and turn blue
- **📏 VOLUME** → Controls dancer size

## ⚙️ Configuration

### Performance Settings

Edit the visualizer files to adjust performance:

```python
# In enhanced_dance_visualizer.py
def __init__(self, width=1200, height=800):  # Screen resolution
    # Lower resolution for better performance:
    # width=800, height=600
```

### Visual Effects Settings

```python
# Reduce particles for performance
for _ in range(5):  # Change to range(2) for fewer particles
    particle = {
        # ... particle settings
    }
```

### Audio Settings

```python
# In voice_dance_controller.py
self.sample_rate = 44100  # Lower to 22050 for less CPU usage
self.chunk_size = 4096    # Adjust buffer size
```

## 🔧 Troubleshooting

### Common Issues

#### 1. **ImportError: No module named 'pygame'**
```bash
pip install pygame
```

#### 2. **Audio not working**
- Check microphone permissions
- Verify audio drivers
- Try different sample rates

#### 3. **Window closes immediately**
- Check for Python errors in terminal
- Try the debug_test.py first
- Ensure all dependencies are installed

#### 4. **Music not loading**
- Verify MP3 file exists
- Check file path and permissions
- Try converting to different audio format

#### 5. **Performance issues**
- Lower screen resolution
- Reduce particle count
- Close other applications
- Try fixed_dance_visualizer.py

### System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- Integrated graphics
- Audio input/output

**Recommended:**
- Python 3.9+
- 8GB RAM
- Dedicated graphics card
- High-quality microphone

## 🎨 Customization

### Adding New Dance Styles

1. **Edit dancer.py**:
```python
def draw_custom_dancer(self, screen):
    # Your custom drawing code here
    pass
```

2. **Add to style list**:
```python
self.available_styles.append("custom")
```

### Creating New Visual Effects

1. **Add particle types**:
```python
def add_custom_particles(self):
    # Custom particle system
    pass
```

2. **Modify background effects**:
```python
def draw_custom_background(self):
    # Custom background rendering
    pass
```

### Music Analysis Customization

Edit `music_analyzer_main.py` to add new features:
```python
def extract_custom_features(self):
    # Add custom music analysis
    pass
```

## 📖 API Reference

### Dancer Class

```python
class EnhancedDancer:
    def __init__(self, x, y, size=50, style="human")
    def update_from_voice(self, voice_features)
    def draw(self, screen)
```

### Visualizer Class

```python
class EnhancedDanceVisualizer:
    def __init__(self, width=1200, height=800)
    def create_dancers(self)
    def load_music(self, file_path)
    def run(self)
```

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Add** your improvements
4. **Test** thoroughly
5. **Submit** a pull request

### Development Setup

```bash
# Clone repository
git clone <repository-url>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements_dance.txt
pip install pytest black flake8  # For testing and formatting
```

## 📄 License

This project is open source. Feel free to use, modify, and distribute according to your needs.

## 🙋‍♂️ Support

For issues and questions:
1. Check the troubleshooting section
2. Review error messages carefully
3. Test with debug_test.py first
4. Create an issue with detailed information

## 🎯 Future Features

- **AI choreography generation**
- **Multi-user dance battles**
- **Custom dance style uploads**
- **Mobile app support**
- **VR/AR integration**
- **Social media sharing**

---

**Enjoy creating amazing music visualizations and dance performances!** 🎉

*Last updated: October 2025*
