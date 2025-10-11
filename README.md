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
- **🎭 Multiple AI Personalities**: Programming tutor, creative writer, life coach, and more
- **🎤 Voice Input Interface**: Simulated voice-to-text functionality
- **🎨 Enhanced UI**: Typewriter effects and modern design

### 🛠️ Technical Stack
- **Framework**: Streamlit web application
- **AI Backend**: LMStudio with local AI model hosting
- **API**: OpenAI-compatible interface
- **Features**: Session state management, custom CSS styling

### 🚀 Quick Start
```bash
cd week04-LUCKY_AI
pip install -r requirements.txt
streamlit run lmstudio_chatbot.py
```

### 🎯 Use Cases
- **Entertainment**: Interactive fortune-telling games
- **Personal Assistant**: AI chat with memory capabilities
- **Educational**: Multiple AI personalities for different learning needs
- **Conversational AI**: Advanced chatbot with context awareness

---

## 🎨 Week 05: AI Creative Studio

### ✨ Key Features
- **🖼️ AI Image Generation**: Transform text descriptions into stunning images
- **📹 Real-time Video Processing**: Live face detection with AI-generated overlays
- **� Combined Creative Studio**: Integrated interface for all features
- **🐕 Specialized Generators**: Cartoon animals, teddy bears, and custom themes
- **🎛️ Advanced Controls**: ControlNet, LCM models, and parameter tuning
- **🌍 Multi-language Support**: Bilingual interface with full localization

### 🛠️ Technical Stack
- **Framework**: Streamlit web applications with WebRTC
- **AI Models**: Stable Diffusion v1.5, ControlNet, LCM
- **Libraries**: Diffusers, Transformers, OpenCV, PIL
- **Hardware**: GPU acceleration with CUDA support

### 🚀 Quick Start
```bash
cd week05-AI_IMAGE_GENERATOR
pip install -r requirements.txt
streamlit run combined_creative_studio.py
```

### 🎯 Use Cases
- **Creative Content**: Generate artwork, illustrations, and designs
- **Real-time Effects**: Apply AI-generated images to live video
- **Prototyping**: Quick visual concept development
- **Education**: Learn AI image generation techniques
- **Entertainment**: Create custom images and interactive video effects

---

## 🎵 Week 06: Music Dance Visualizer

### ✨ Key Features
- **🎭 Multiple Dance Styles**: 7 unique dancer types (Human, Abstract, Robot, Hip-Hop, Ballet, Cartoon, Animal)
- **🎨 Real-time Audio Visualization**: Dynamic particle systems and spectrum analysis
- **🎤 Voice Control**: Speech recognition and real-time voice response systems
- **🎵 Music Synchronization**: Advanced beat detection and tempo analysis
- **🌈 Dynamic Effects**: Particle systems, lighting effects, and mood-responsive backgrounds
- **🎮 Interactive Controls**: Real-time tempo adjustment and dance style switching

### 🛠️ Technical Stack
- **Framework**: Pygame for graphics and audio processing
- **Audio Analysis**: Librosa for music feature extraction
- **Voice Processing**: Real-time microphone input with speech recognition
- **Visual Effects**: Custom particle systems and dynamic lighting

### 🚀 Quick Start
```bash
cd week06_audio_project/music_dance
pip install -r requirements_dance.txt
python enhanced_dance_visualizer.py
```

### 🎯 Use Cases
- **Entertainment**: Interactive music visualization and dance performances
- **Education**: Music theory demonstration and rhythm training
- **Creative Arts**: Visual music performance and artistic expression
- **Voice Interaction**: Hands-free control and voice-responsive entertainment

---

## 🎆 Week 06: Voice-Controlled Fireworks

### ✨ Key Features
- **� Voice-Reactive Fireworks**: Launch fireworks using voice volume and intensity
- **👹 Monster Hunt Combat Mode**: New Year themed survival game with monster battles
- **⚔️ Complete Combat System**: Player health, monster fireballs, and defensive mechanics
- **🔊 Dynamic Sound Effects**: Realistic launch and explosion audio with size-based variations
- **�🎮 Dual Game Modes**: Peaceful fireworks display and intense combat survival
- **🌟 Spectacular Visual Effects**: Particle physics, multiple colors, and realistic explosions

### 🛠️ Technical Stack
- **Framework**: Pygame for graphics and PyAudio for real-time voice processing
- **Audio Processing**: Ultra-sensitive voice detection with advanced signal amplification
- **Game Engine**: Custom physics simulation with collision detection
- **Sound Generation**: Procedural audio synthesis for realistic firework sounds

### 🚀 Quick Start
```bash
cd set_off_fireworks
pip install -r requirements.txt
python voice_fireworks.py
```

### 🎯 Use Cases
- **Entertainment**: Voice-controlled celebration and interactive gaming
- **Party Activities**: Group entertainment with voice-based fireworks launching
- **Gaming**: Survival combat with voice-controlled weapons
- **Audio Technology**: Real-time voice processing and audio-visual synchronization

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