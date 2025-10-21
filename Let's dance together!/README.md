# Let's dance together! 🎵🕺

An AI-powered music visualization and dance system that creates interactive, real-time dance performances synchronized with music and voice input. Experience multiple dance styles with dynamic visual effects that respond to audio analysis and voice commands.

## 🌟 Key Features

### 🎭 Seven Dance Styles
- **Human**: Classic stick figure dancer with natural human movements
- **Abstract**: Morphing geometric shapes that flow with the rhythm
- **Robot**: Mechanical movements with precise joint animations
- **Hip-Hop**: Street dance style with dynamic urban moves
- **Ballet**: Elegant poses with graceful classical movements
- **Cartoon**: Playful animations with exaggerated expressions
- **Animal**: Cute animal dancer with ears and tail movements

### 🎨 Visual Effects System
- **Dynamic Particle System**: Particles that react to music beats and intensity
- **Smart Lighting**: Radial glows and light effects triggered by strong beats
- **Rainbow Audio Spectrum**: Real-time frequency visualization bars
- **Mood-Responsive Backgrounds**: Colors change based on music energy and tempo
- **Live Audio Analysis**: Spectrum analysis with beat detection and tempo tracking

### 🎤 Voice Control Integration
- **Speech Recognition**: Control dance moves with voice commands
- **Real-time Voice Response**: Dancers react to voice volume, pitch, and speech rate
- **Voice Visualization**: Live microphone input analysis and visual feedback

## � How to Run

### Quick Setup
1. **Navigate to the "Let's dance together!" directory**
2. **Install dependencies**:
   ```bash
   pip install -r requirements_dance.txt
   ```
3. **Launch the main visualizer**:
   ```bash
   python enhanced_dance_visualizer.py
   ```

### Alternative Versions
- **Stable Performance**: `python fixed_dance_visualizer.py`
- **Basic Testing**: `python debug_test.py`
- **Simple Demo**: `python simple_dance_test.py`

## 🎯 How to Interact

### Basic Controls
- **SPACE**: Play/Pause music playback
- **ESC**: Exit the application
- **Mouse Click**: Change tempo (click position determines BPM)
- **Arrow Keys**: Control mood and energy
  - **↑ Up**: Switch to energetic mood
  - **↓ Down**: Switch to calm mood
  - **← Left**: Neutral mood setting
  - **→ Right**: Happy mood setting

### Music Integration
- **Built-in Music**: Uses included test_music.mp3 for immediate demo
- **Custom Music**: Replace test_music.mp3 with your own MP3, WAV, or OGG files
- **Real-time Analysis**: Automatic tempo detection, beat tracking, and energy analysis
- **Mood Classification**: System analyzes music to determine energetic, happy, calm, or neutral moods

### Dance Style Switching
The system automatically cycles through all seven dance styles, or you can modify the code to focus on specific styles. Each dancer responds differently to:
- **Music Tempo**: Faster songs create more energetic movements
- **Beat Intensity**: Strong beats trigger special animations
- **Frequency Analysis**: Different frequency ranges affect movement patterns
- **Voice Input**: Microphone input influences dancer behavior

### Voice Control Features
For enhanced voice interaction, run the voice control modules from the parent directory:

**Voice Commands**:
- Navigate to parent directory: `cd ..`
- Run voice command dancer: `python voice_command_dancer.py`
- Supported commands: "dance", "spin", "jump", "stop", "bigger", "smaller"
- Color commands: "red", "blue", "green"

**Real-time Voice Response**:
- Run voice controller: `python voice_dance_controller.py`
- **Shout loudly** → Dancers spin and turn red
- **High pitch voice** → Dancers jump and turn green
- **Fast speech** → Dancers wave and turn blue
- **Voice volume** → Controls dancer size dynamically

## ⚙️ Performance Optimization

### System Requirements
**Minimum**: Python 3.8+, 4GB RAM, basic audio drivers, microphone for voice features
**Recommended**: Python 3.9+, 8GB RAM, dedicated graphics, high-quality microphone

### Performance Tips
- **Lower Resolution**: Edit screen size in enhanced_dance_visualizer.py for better performance
- **Reduce Particles**: Modify particle count for smoother animations on slower systems
- **Audio Buffer**: Adjust sample rate and chunk size for optimal audio processing
- **Close Background Apps**: Free up system resources for better real-time performance

## 🎵 Music and Audio Setup

### Adding Your Music
1. Place MP3, WAV, or OGG files in the "Let's dance together!" directory
2. Rename your file to `test_music.mp3` for automatic loading
3. Or modify the file path in the visualizer code

### Audio Analysis Features
- **Automatic Tempo Detection**: Calculates BPM for dance synchronization
- **Beat Tracking**: Identifies strong beats for visual effects
- **Spectral Analysis**: Frequency analysis for different visual responses
- **Energy Classification**: Determines high/low energy sections
- **Onset Detection**: Identifies note beginnings for precise timing

## 🔧 Troubleshooting

### Common Issues and Solutions

**Import Errors**: Install required packages with `pip install pygame numpy librosa scipy`

**Audio Problems**: Check microphone permissions, verify audio drivers, ensure proper sample rates

**Performance Issues**: Lower screen resolution, reduce particle count, close other applications

**Music Loading**: Verify file exists, check file permissions, try different audio formats

**Window Crashes**: Run debug_test.py first, check terminal for error messages, ensure all dependencies installed

## 🎨 Customization Options

### Visual Customization
- **Dance Styles**: Each style has unique movement patterns and visual characteristics
- **Color Schemes**: Dynamic color changes based on music analysis and mood
- **Particle Effects**: Customizable particle systems that respond to different frequency ranges
- **Background Animations**: Mood-responsive backgrounds with gradient effects

### Audio Customization
- **Tempo Sensitivity**: Adjust how dancers respond to BPM changes
- **Frequency Response**: Modify which frequency ranges trigger specific movements
- **Beat Detection**: Fine-tune beat sensitivity for different music genres
- **Voice Thresholds**: Adjust microphone sensitivity for voice control

## 🎯 Use Cases

### Entertainment
- **Party Visualizer**: Dynamic music visualization for events and gatherings
- **Personal Enjoyment**: Interactive music experience for individual use
- **Creative Expression**: Artistic tool for music and movement exploration

### Educational
- **Music Theory**: Visual demonstration of rhythm, tempo, and musical structure
- **Audio Processing**: Learn about frequency analysis and beat detection
- **Programming**: Study real-time graphics and audio processing techniques

### Accessibility
- **Voice Control**: Hands-free interaction for accessibility needs
- **Visual Feedback**: Audio-to-visual conversion for hearing-impaired users
- **Customizable Interface**: Adjustable settings for different user requirements

## 🤝 Contributing & Support

### Contributing
We welcome contributions to improve "Let's dance together!"! You can:
- Report bugs and suggest new features
- Submit improvements for dance styles and visual effects
- Enhance voice control capabilities
- Optimize performance and add new audio analysis features

### Development Setup
1. Fork the repository and clone your fork
2. Create a virtual environment and install dependencies
3. Test your changes with debug_test.py
4. Submit a pull request with detailed description

### Getting Help
For issues and questions:
1. Check the troubleshooting section above
2. Review error messages in the terminal
3. Test with debug_test.py to isolate issues
4. Create detailed issue reports with system information

## 📄 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute according to your needs.

---

**Create amazing music visualizations and dance performances!** �

*Experience the fusion of AI, music, and interactive visual art through real-time dance animation.*

*Last updated: October 21, 2025*
