# AI Programming Course - Assignment 03

A comprehensive collection of AI-powered applications featuring interactive chatbots, fortune-telling systems, advanced image generation tools, and immersive audio-visual experiences. This repository contains four major projects developed as part of the AI programming course.

## 📁 Project Overview

### 🍀 [Week 04: Lucky AI - Fortune-Telling Chatbot](./week04-LUCKY_AI/)
An interactive AI chatbot application featuring tarot card readings, horoscope predictions, and advanced conversational AI with memory capabilities.

### 🎨 [Week 05: AI Creative Studio](./week05-AI_IMAGE_GENERATOR/)
A comprehensive AI-powered creative toolkit built with Stable Diffusion, featuring image generation, real-time video processing, and face detection with dynamic AI overlays.

### 🎵 [Week 06: Music Dance Visualizer](./week06_audio_project/music_dance/)
An AI-powered music visualization and dance system with real-time audio analysis, multiple dance styles, and interactive voice control features.

### 🎆 [Week 06: Voice-Controlled Fireworks](./set_off_fireworks/)
An immersive voice-controlled fireworks display with New Year Monster Hunt combat mode, featuring real-time audio processing and spectacular visual effects.

---

## 🍀 Week 04: Lucky AI - Fortune-Telling Assistant

### ✨ Key Features
- **🔮 Interactive Tarot Reading**: 22 Major Arcana cards with detailed interpretations
- **⭐ Daily Horoscope**: Complete zodiac predictions for all 12 signs  
- **🧠 Advanced Memory System**: Remembers user information across sessions
- **🎭 Multiple AI Personalities**: Programming tutor, creative writer, life coach, study buddy, travel guide
- **🎤 Voice Input Interface**: Simulated voice-to-text functionality
- **🎨 Enhanced UI**: Typewriter effects, custom CSS styling, responsive design

### 🛠️ Technical Stack
- **Framework**: Streamlit web application with custom styling
- **AI Backend**: LMStudio with local AI model hosting (OpenAI-compatible)
- **Models**: Meta-Llama-3-8B-Instruct-GGUF or compatible models
- **Features**: Session state management, regex-based memory extraction

### 🚀 How to Run
```bash
# Navigate to project directory
cd week04-LUCKY_AI

# Install dependencies
pip install streamlit openai pandas numpy ollama

# Start LMStudio with a compatible model on port 1234
# OR start Ollama service: ollama serve

# Launch the application
streamlit run lmstudio_chatbot.py

# Access at http://localhost:8501
```

### 🎯 How to Interact
**Basic Chat**: Simply type messages in the input field
- Switch AI personalities using the sidebar dropdown
- Share personal information for AI to remember ("My name is John, I'm 25...")

**Tarot Reading**: 
- Type: `"tarot reading"`, `"draw tarot cards"`, or `"塔罗牌抽签"`
- Click on any of the 18 displayed mystical cards
- Receive detailed interpretation with spiritual guidance

**Horoscope Consultation**:
- Type: `"horoscope"`, `"zodiac"`, or `"daily fortune"`
- Select your zodiac sign from the 12 visual options
- Get comprehensive daily predictions for love, career, finance, health

**Memory Features**:
- View remembered details in the "🧠 Memory" sidebar section
- AI extracts and stores personal information automatically
- Clear memory using the "🧹 Clear Memory" button

### 💡 Use Cases
- **Entertainment**: Interactive fortune-telling and mystical guidance
- **Personal Assistant**: Multi-personality AI with persistent memory
- **Educational**: Programming help, creative writing, life coaching
- **Conversational AI**: Advanced chatbot with context awareness

---

## 🎨 Week 05: AI Creative Studio

### ✨ Key Features
- **🖼️ Text-to-Image Generation**: Transform descriptions into stunning artwork
- **📹 Real-time Video Processing**: Live face detection with AI-generated overlays
- **🎨 Multiple Generation Modes**: Basic generator, ControlNet, LCM models
- **🐕 Specialized Generators**: Cartoon animals, teddy bears, custom themes
- **🎛️ Advanced Controls**: Parameter tuning, negative prompts, batch generation
- **🌍 Multi-language Support**: English/Chinese interface with full localization
- **💾 Export Features**: Save images, download functionality, batch processing

### 🛠️ Technical Stack
- **Framework**: Streamlit with WebRTC for video processing
- **AI Models**: Stable Diffusion v1.5, ControlNet, LCM (Latent Consistency Models)
- **Libraries**: Diffusers, Transformers, OpenCV, PIL, PyTorch
- **Hardware**: GPU acceleration with CUDA support (8GB+ VRAM recommended)

### 🚀 How to Run
```bash
# Navigate to project directory
cd week05-AI_IMAGE_GENERATOR

# Install dependencies (choose based on hardware)
pip install -r requirements.txt  # CPU version
# OR
pip install -r cuda_torch_requirements.txt  # GPU accelerated

# Launch main application
streamlit run streamlit_image_generator.py
# OR integrated studio
streamlit run combined_creative_studio.py

# Access at http://localhost:8501
```

### 🎯 How to Interact
**Text-to-Image Generation**:
- Enter descriptive prompts: `"a beautiful sunset over mountains, oil painting style"`
- Adjust parameters: image size, inference steps, guidance scale
- Use negative prompts to avoid unwanted elements
- Download generated images instantly

**Real-time Video Effects**:
- Enable webcam for live video processing
- Apply AI-generated overlays to detected faces
- Switch between different effect styles
- Record enhanced video output

**Specialized Generators**:
- **Cartoon Dog Generator**: `"brown fluffy puppy playing in grass"`
- **Teddy Bear Creator**: `"cute teddy bear with bow tie, soft lighting"`
- **ControlNet Mode**: Upload reference images for precise control

**Advanced Features**:
- Batch generation for multiple images
- Custom model loading and configuration
- Parameter presets for different art styles
- Multi-language interface switching

### 💡 Use Cases
- **Creative Content**: Generate artwork, illustrations, marketing materials
- **Real-time Effects**: Interactive video calls with AI-enhanced backgrounds
- **Prototyping**: Quick visual concept development for projects
- **Education**: Learn AI image generation and computer vision techniques
- **Entertainment**: Create custom images and interactive video effects

---

## 🎵 Week 06: Music Dance Visualizer

### ✨ Key Features
- **🎭 Multiple Dance Styles**: 7 unique dancer types (Human, Abstract, Robot, Hip-Hop, Ballet, Cartoon, Animal)
- **🎨 Real-time Audio Visualization**: Dynamic particle systems and spectrum analysis
- **🎤 Voice Control**: Speech recognition and real-time voice response systems
- **🎵 Music Synchronization**: Advanced beat detection and tempo analysis
- **🌈 Dynamic Effects**: Particle systems, lighting effects, mood-responsive backgrounds
- **🎮 Interactive Controls**: Real-time tempo adjustment and dance style switching
- **🔊 Audio Processing**: Librosa-based feature extraction and frequency analysis

### 🛠️ Technical Stack
- **Framework**: Pygame for graphics and audio processing
- **Audio Analysis**: Librosa for music feature extraction and beat detection
- **Voice Processing**: Real-time microphone input with speech recognition
- **Visual Effects**: Custom particle systems, dynamic lighting, and OpenGL acceleration
- **AI Components**: Machine learning for dance pattern generation

### 🚀 How to Run
```bash
# Navigate to project directory
cd week06_audio_project/music_dance

# Install audio processing dependencies
pip install pygame librosa numpy scipy soundfile pyaudio

# Install additional requirements
pip install -r requirements_dance.txt

# Launch the enhanced visualizer
python enhanced_dance_visualizer.py

# Alternative: Run basic version
python music_dance_visualizer.py
```

### 🎯 How to Interact
**Music Loading**:
- Load audio files: MP3, WAV, FLAC formats supported
- Use built-in sample tracks for instant demo
- Real-time microphone input for live music analysis

**Dance Style Selection**:
- Press `1-7` keys to switch between dancer types:
  - `1`: Human dancer with realistic movements
  - `2`: Abstract geometric patterns
  - `3`: Robot with mechanical motion
  - `4`: Hip-Hop with street dance moves
  - `5`: Ballet with graceful movements
  - `6`: Cartoon with playful animation
  - `7`: Animal movements (cat, bird, etc.)

**Voice Control**:
- Say `"change style"` to cycle through dancers
- Say `"faster"` or `"slower"` to adjust tempo
- Say `"more energy"` to increase visual intensity
- Say `"pause"` or `"play"` to control playback

**Visual Controls**:
- `SPACE`: Pause/resume music
- `UP/DOWN`: Adjust volume
- `LEFT/RIGHT`: Seek through track
- `R`: Reset visualizer
- `F`: Toggle fullscreen mode

**Interactive Features**:
- Click and drag to influence particle movements
- Mouse position affects lighting and color schemes
- Keyboard input creates rhythm-synced effects

### 💡 Use Cases
- **Entertainment**: Interactive music visualization for parties and events
- **Education**: Music theory demonstration and rhythm training
- **Creative Arts**: Visual music performance and artistic expression
- **Accessibility**: Voice-controlled music interface for hands-free operation
- **Therapy**: Relaxing visual feedback for music meditation

---

## 🎆 Week 06: Voice-Controlled Fireworks

### ✨ Key Features
- **🎤 Voice-Reactive Fireworks**: Launch fireworks using voice volume and intensity
- **👹 Monster Hunt Combat Mode**: New Year themed survival game with AI monsters
- **⚔️ Complete Combat System**: Player health (30 HP), monster fireballs, defensive mechanics
- **🎯 Precision Fireball Interception**: Skill-based projectile blocking system
- **🔊 Dynamic Sound Effects**: Realistic launch and explosion audio with size-based variations
- **🎮 Dual Game Modes**: Peaceful fireworks display and intense combat survival
- **🌟 Spectacular Visual Effects**: Particle physics, multiple colors, realistic explosions
- **📊 Real-time Statistics**: Score tracking, health monitoring, monster counts

### 🛠️ Technical Stack
- **Framework**: Pygame for graphics and PyAudio for real-time voice processing
- **Audio Processing**: Ultra-sensitive voice detection with 3x signal amplification
- **Game Engine**: Custom physics simulation with collision detection
- **Sound Generation**: Procedural audio synthesis for realistic firework sounds
- **AI Systems**: Monster behavior patterns and intelligent spawning

### 🚀 How to Run
```bash
# Navigate to project directory
cd set_off_fireworks

# Install dependencies
pip install pygame pyaudio numpy imageio pillow

# Install all requirements
pip install -r requirements.txt

# Launch the voice-controlled fireworks game
python voice_fireworks.py

# Alternative: Create gameplay recording
python record_gameplay.py
```

### 🎯 How to Interact
**Voice Control**:
- **Speak into microphone**: Voice volume determines firework size and power
- **Louder voice = Bigger explosions**: Scale effects with voice intensity
- **Continuous speech**: Rapid-fire fireworks with 150ms cooldown
- **Whisper**: Small, delicate fireworks
- **Shout**: Massive explosions with wide blast radius

**Game Mode Switching**:
- **Press `M`**: Toggle between Normal and Monster Hunt modes
- **Normal Mode**: Peaceful fireworks display for celebration
- **Monster Hunt**: Survival combat with voice-controlled weapons

**Monster Hunt Combat**:
- **Objective**: Survive as long as possible (30 HP starting health)
- **Enemy Monsters**: AI-driven creatures with glowing red eyes
- **Monster Attacks**: Fireballs that deal 1 damage per hit
- **Defense Strategy**: Use voice to create firework explosions that intercept fireballs
- **Precision Timing**: Place explosions in fireball paths to block attacks
- **Scoring**: Earn points for monsters destroyed + bonus for fireball interceptions

**Combat Controls**:
- **Voice Volume**: Controls firework placement and explosion size
- **Strategic Positioning**: Aim voice-controlled explosions at incoming threats
- **Health Management**: Monitor health bar and damage indicators
- **Game Over**: Press `R` to restart when health reaches zero

**Additional Controls**:
- **ESC**: Exit application
- **Mouse Movement**: Affects firework launch direction
- **Visual Feedback**: Screen flashes and health bar changes show damage

### 💡 Use Cases
- **Entertainment**: Voice-controlled celebration and interactive gaming
- **Party Activities**: Group entertainment with voice-based fireworks launching
- **Gaming**: Survival combat with innovative voice-controlled weapons
- **Audio Technology**: Real-time voice processing and audio-visual synchronization
- **Accessibility**: Voice-only control for hands-free gaming experience
- **Educational**: Demonstrates voice signal processing and game physics

---

### 1. Main Image Generator (`streamlit_image_generator.py`)

## 🌟 Project HighlightsThe primary application featuring:

- Intuitive web interface

### 🔬 Technical Innovation- Real-time image generation

- **Multi-modal AI**: Combining text, image, and voice interactions- Download functionality

- **Local AI Integration**: LMStudio for privacy-focused AI hosting- Preset prompts for quick start

- **Advanced UI/UX**: Custom Streamlit interfaces with enhanced styling- Advanced parameter controls

- **GPU Optimization**: CUDA acceleration for high-performance image generation

**Usage:**

### 🎓 Learning Outcomes```bash

- **AI Integration**: Practical experience with modern AI APIs and modelsstreamlit run streamlit_image_generator.py

- **Web Development**: Building interactive applications with Streamlit```

- **Image Processing**: Advanced computer vision and image manipulation

- **Memory Systems**: Implementing persistent AI memory and context### 2. Integrated Creative Studio (`integrated_ai_app.py`)

- **Multi-language Support**: Creating accessible, international applicationsA comprehensive toolkit with:

- Multiple generation modes

### 🚀 Practical Applications- Video processing capabilities

- **Business**: Content creation, marketing materials, customer engagement- Multi-language interface

- **Education**: Interactive learning tools and educational content- Advanced image controls

- **Entertainment**: Games, creative tools, and interactive experiences

- **Research**: AI experimentation and prototype development**Usage:**

```bash

---streamlit run integrated_ai_app.py

```

## 📋 System Requirements

### 3. Specialized Generators

### Minimum Requirements- **Cartoon Dog Generator**: Create cute cartoon-style dog images

- **OS**: Windows 10/11, macOS 10.14+, or Linux- **Teddy Generator**: Generate adorable teddy bear images

- **Python**: 3.8 or higher- **ControlNet**: Precise image control using edge detection

- **RAM**: 8GB minimum (16GB recommended)

- **Storage**: 15GB free space for models and dependencies### 4. Video Processing

Real-time video effects and filters for webcam or video files.

### Recommended for Optimal Performance

- **GPU**: NVIDIA RTX 3060 or better with 8GB+ VRAM## 🛠️ Configuration

- **RAM**: 16GB or higher

- **Storage**: SSD with 20GB+ free space### GPU Setup

- **CUDA**: Toolkit installed for GPU accelerationThe application automatically detects and uses GPU acceleration when available. For optimal performance:



---1. Install CUDA toolkit

2. Use the CUDA-optimized requirements:

## 🚀 Getting Started   ```bash

   pip install -r cuda_torch_requirements.txt

### 1. Clone the Repository   ```

```bash

git clone https://github.com/xueyu-coco/assignment03-2025.git### Model Configuration

cd assignment03-2025The project uses Stable Diffusion v1.5 by default. Models are automatically downloaded on first use and cached for future sessions.

```

## 📖 Usage Examples

### 2. Choose Your Project

### Basic Text-to-Image Generation

#### For Lucky AI (Week 04):```python

```bashfrom diffusers import DiffusionPipeline

cd week04-LUCKY_AIimport torch

pip install -r requirements.txt

# Start LMStudio with compatible model# Load the pipeline

streamlit run lmstudio_chatbot.pypipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

```

# Generate an image

#### For AI Image Generator (Week 05):prompt = "a beautiful landscape with mountains, golden hour lighting"

```bashimage = pipe(prompt).images[0]

cd week05-AI_IMAGE_GENERATORimage.save("generated_image.png")

pip install -r requirements.txt```

streamlit run streamlit_image_generator.py

```### Using the Cartoon Dog Generator

```python

### 3. Access Applicationsfrom cartoon_dog_generator import CartoonDogGenerator

- Open your browser to `http://localhost:8501`

- Start exploring the AI applications!generator = CartoonDogGenerator()

image = generator.generate_cartoon_dog("brown fluffy puppy playing in grass")

---```



## 📚 Documentation## 🎨 Prompt Engineering Tips



### Project Documentation### Effective Prompts

- [Week 04 - Lucky AI README](./week04-LUCKY_AI/README.md) - Detailed setup and usage guide- **Be specific**: Use detailed descriptions instead of vague terms

- [Week 05 - AI Image Generator README](./week05-AI_IMAGE_GENERATOR/README.md) - Comprehensive feature documentation- **Include style**: Specify art styles like "oil painting", "cartoon style", "photorealistic"

- **Add quality modifiers**: Use terms like "high quality", "detailed", "professional"

### Learning Resources- **Describe lighting**: Include lighting conditions like "soft lighting", "golden hour", "dramatic shadows"

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io/)

- **Stable Diffusion Guide**: [huggingface.co/docs/diffusers](https://huggingface.co/docs/diffusers)### Example Prompts

- **LMStudio Setup**: Local AI model hosting and configuration- **Landscape**: "serene mountain lake at sunset, golden hour lighting, reflection in water, detailed, cinematic"

- **OpenAI API**: Compatible API integration patterns- **Portrait**: "portrait of a wise old wizard, detailed face, magical atmosphere, fantasy art style"

- **Animal**: "cute red panda sitting on bamboo, fluffy fur, adorable expression, soft lighting"

---

### Negative Prompts

## 🔧 TroubleshootingUse negative prompts to avoid unwanted elements:

- "blurry, low quality, distorted, ugly, poorly drawn"

### Common Issues- "extra limbs, deformed, mutated, bad anatomy"



#### Week 04 (Lucky AI)## 🔧 Technical Details

- **LMStudio Connection**: Ensure server is running on port 1234

- **Memory Issues**: Clear browser cache and restart application### Dependencies

- **Model Loading**: Verify compatible AI model is loaded in LMStudio- **Streamlit**: Web interface framework

- **Diffusers**: Hugging Face diffusion models

#### Week 05 (Image Generator)- **Transformers**: Natural language processing

- **GPU Detection**: Install CUDA toolkit for GPU acceleration- **OpenCV**: Computer vision and image processing

- **Model Downloads**: Ensure stable internet for initial model downloads- **PIL/Pillow**: Image manipulation

- **Memory Errors**: Reduce image resolution or inference steps- **PyTorch**: Deep learning framework

- **Slow Generation**: Enable GPU acceleration or use LCM models

### System Requirements

### Performance Optimization- **Minimum**: 8GB RAM, Intel i5 or equivalent

- **GPU Setup**: Install appropriate CUDA toolkit version- **Recommended**: 16GB+ RAM, NVIDIA RTX 3060 or better

- **Memory Management**: Close unnecessary applications during AI operations- **Storage**: 10GB+ free space for models

- **Model Caching**: Allow time for initial model downloads and caching

- **Network**: Stable internet connection for model downloads### Performance Optimization

- **GPU Memory**: Adjust batch size based on available VRAM

---- **CPU Mode**: Increase swap file size for CPU-only systems

- **Model Caching**: Models are cached locally after first download

## 🤝 Contributing

## 🐛 Troubleshooting

We welcome contributions to improve these AI applications! Here's how you can help:

### Common Issues

### Ways to Contribute

1. **Bug Reports**: Report issues with detailed reproduction steps1. **Out of Memory Error**

2. **Feature Requests**: Suggest new features or improvements   - Reduce image resolution

3. **Code Contributions**: Submit pull requests with enhancements   - Lower the number of inference steps

4. **Documentation**: Improve guides and documentation   - Close other GPU-intensive applications

5. **Testing**: Help test new features and report feedback

2. **Model Download Issues**

### Development Guidelines   - Check internet connection

1. Fork the repository   - Ensure sufficient disk space

2. Create a feature branch (`git checkout -b feature/amazing-feature`)   - Try running with administrator privileges

3. Commit your changes (`git commit -m 'Add amazing feature'`)

4. Push to the branch (`git push origin feature/amazing-feature`)3. **CUDA Not Found**

5. Open a Pull Request   - Install appropriate CUDA toolkit version

   - Verify PyTorch CUDA installation: `torch.cuda.is_available()`

---

4. **Slow Generation**
   - Enable GPU acceleration
   - Reduce inference steps for faster generation
   - Use LCM models for rapid prototyping

## 📚 Learning Resources

### Notebooks
- `week05_notebook.ipynb`: Comprehensive tutorial on AI image generation
- `python_classes_tutorial.ipynb`: Python programming fundamentals

### Documentation
- [Stable Diffusion Documentation](https://huggingface.co/docs/diffusers)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyTorch Documentation](https://pytorch.org/docs/)

## 🏆 Project Statistics

### Week 04 - Lucky AI
- **Lines of Code**: ~800+ lines
- **Features**: 6 major components
- **AI Personalities**: 5 different assistants
- **Memory System**: Advanced context retention

### Week 05 - AI Image Generator
- **Lines of Code**: ~2,600+ lines
- **Applications**: 8 different interfaces
- **AI Models**: Multiple Stable Diffusion variants
- **Image Types**: Unlimited creative possibilities

### Week 06 - Music Dance Visualizer
- **Lines of Code**: ~1,500+ lines
- **Dance Styles**: 7 unique dancer types
- **Audio Features**: Real-time spectrum analysis
- **Voice Control**: Speech recognition and voice response

### Week 06 - Voice-Controlled Fireworks
- **Lines of Code**: ~990+ lines
- **Game Modes**: 2 distinct gameplay experiences
- **Combat System**: Complete health and attack mechanics
- **Audio Processing**: Ultra-sensitive voice detection

### Combined Project
- **Total Files**: 60+ Python files
- **Dependencies**: 25+ AI/ML libraries
- **Supported Languages**: English and Chinese
- **Platform Support**: Cross-platform compatibility

- **Total Files**: 40+ Python files## 🤝 Contributing

- **Dependencies**: 20+ AI/ML libraries

- **Supported Languages**: English and ChineseWe welcome contributions! Please feel free to:

- **Platform Support**: Cross-platform compatibility- Report bugs and issues

- Suggest new features

---- Submit pull requests

- Improve documentation

## 📄 License

## 📄 License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for details.

This project is open-source and available under the MIT License.

---

## 🙏 Acknowledgments

## 🙏 Acknowledgments

- Hugging Face for the Diffusers library

### Technologies Used- Stability AI for Stable Diffusion

## 🙏 Acknowledgments

### Technologies Used
- **Streamlit**: Amazing web framework for AI applications
- **Hugging Face**: Diffusers library and model hosting
- **Stability AI**: Stable Diffusion models
- **LMStudio**: Local AI model hosting platform
- **OpenAI**: API compatibility and standards
- **Pygame**: Graphics and audio processing for interactive applications
- **Librosa**: Advanced audio analysis and music processing

### Inspiration
- **AI Community**: Open-source AI development community
- **Educational Resources**: AI programming course materials
- **User Feedback**: Continuous improvement based on user needs

## 🔮 Future Plans

- [ ] Support for more AI models (DALL-E, Midjourney-style)
- [ ] Advanced editing capabilities
- [ ] Batch generation features
- [ ] Custom model training interface
- [ ] API endpoints for integration
- [ ] Mobile-responsive design improvements
- [ ] VR/AR integration for audio-visual projects
- [ ] Multiplayer features for interactive applications

---

**Happy Creating! 🎨✨**

For questions or support, please open an issue or contact the development team.

---

## 🌟 Project Highlights Summary

This comprehensive AI programming collection demonstrates the evolution from conversational AI to creative visual generation, and finally to immersive audio-visual interactive experiences:

- **🍀 Week 04**: Advanced chatbot systems with memory and personality
- **🎨 Week 05**: AI-powered creative tools with real-time image generation
- **🎵 Week 06**: Interactive audio-visual applications combining music, voice, and graphics
- **🎆 Week 06**: Gaming experiences with voice control and real-time audio processing

### 🔬 Technical Evolution
- **AI Integration**: From simple API calls to complex multi-modal systems
- **User Interaction**: From text-based to voice-controlled interfaces
- **Visual Complexity**: From static images to dynamic real-time graphics
- **Audio Processing**: From basic input to advanced signal analysis and synthesis

### 🎯 Learning Outcomes
- **AI/ML Mastery**: Practical experience with modern AI frameworks and models
- **Interactive Design**: Building engaging user interfaces with real-time feedback
- **Audio-Visual Programming**: Combining multiple media streams for immersive experiences
- **Game Development**: Creating interactive entertainment with physics and AI

**Explore the fascinating world of AI through interactive chatbots, creative image generation, and immersive audio-visual experiences!** 🚀

---

*Last updated: October 11, 2025*

### 📞 Support & Contact

For questions, issues, or contributions:
1. **Check Documentation**: Review individual project README files for detailed setup instructions
2. **Common Issues**: Check troubleshooting sections in each project
3. **GitHub Issues**: Create an issue for bugs or feature requests
4. **Community Support**: Engage with the AI development community

### 📋 Course Information
- **Institution**: AI Programming Course
- **Assignment**: Assignment 03 - 2025
- **Repository**: [assignment03-2025](https://github.com/xueyu-coco/assignment03-2025)

---

**Happy Coding and Creating! 🚀✨**

*Explore the fascinating world of AI through interactive chatbots, creative image generation, and immersive audio-visual experiences. These projects demonstrate the practical applications of modern AI technologies in engaging, user-friendly applications.*

*Last updated: October 2, 2025*