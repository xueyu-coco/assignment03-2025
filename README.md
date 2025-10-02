# AI Programming Course - Assignment 03# AI Image Generator



A comprehensive collection of AI-powered applications featuring interactive chatbots, fortune-telling systems, and advanced image generation tools. This repository contains two major projects developed as part of the AI programming course.A comprehensive AI-powered image generation toolkit built with Stable Diffusion and Streamlit. This project provides multiple applications for creating stunning images from text descriptions, applying image filters, and real-time video processing.



## 📁 Project Overview## 🌟 Features



### 🍀 [Week 04: Lucky AI - Fortune-Telling Chatbot](./week04-LUCKY_AI/)### 🎨 Image Generation

An interactive AI chatbot application featuring tarot card readings, horoscope predictions, and advanced conversational AI with memory capabilities.- **Text-to-Image**: Transform text descriptions into beautiful images using Stable Diffusion

- **Preset Prompts**: Quick start with pre-configured prompts for landscapes, animals, sci-fi scenes, and more

### 🎨 [Week 05: AI Image Generator](./week05-AI_IMAGE_GENERATOR/)- **Advanced Controls**: Fine-tune generation with adjustable steps and guidance scale

A comprehensive AI-powered image generation toolkit built with Stable Diffusion, featuring multiple applications for creating stunning images from text descriptions.- **Negative Prompts**: Specify what you don't want in the generated images

- **GPU Acceleration**: Automatic GPU detection and acceleration when available

---

### 🖼️ Image Processing

## 🍀 Week 04: Lucky AI - Fortune-Telling Assistant- **Advanced Filters**: Apply various image processing effects

- **ControlNet Integration**: Precise image control using edge detection and other techniques

### ✨ Key Features- **Batch Processing**: Handle multiple images efficiently

- **🔮 Interactive Tarot Reading**: 22 Major Arcana cards with detailed interpretations

- **⭐ Daily Horoscope**: Complete zodiac predictions for all 12 signs### 📹 Video Processing

- **🧠 Advanced Memory System**: Remembers user information across sessions- **Real-time Filters**: Apply effects to live video streams

- **🎭 Multiple AI Personalities**: Programming tutor, creative writer, life coach, and more- **Video Enhancement**: Improve video quality with AI-powered filters

- **🎤 Voice Input Interface**: Simulated voice-to-text functionality

- **🎨 Enhanced UI**: Typewriter effects and modern design### 🌍 Multi-language Support

- **Bilingual Interface**: Support for English and Chinese languages

### 🛠️ Technical Stack- **Localized Content**: Fully translated user interface and instructions

- **Framework**: Streamlit web application

- **AI Backend**: LMStudio with local AI model hosting## 🚀 Quick Start

- **API**: OpenAI-compatible interface

- **Features**: Session state management, custom CSS styling### Prerequisites

- Python 3.8 or higher

### 🚀 Quick Start- NVIDIA GPU (recommended for faster generation)

```bash- CUDA toolkit (for GPU acceleration)

cd week04-LUCKY_AI

pip install -r requirements.txt### Installation

streamlit run lmstudio_chatbot.py

```1. **Clone the repository**

   ```bash

### 🎯 Use Cases   git clone <repository-url>

- **Entertainment**: Interactive fortune-telling games   cd "week05_AI Image Generator"

- **Personal Assistant**: AI chat with memory capabilities   ```

- **Educational**: Multiple AI personalities for different learning needs

- **Conversational AI**: Advanced chatbot with context awareness2. **Install dependencies**

   ```bash

---   pip install -r requirements.txt

   ```

## 🎨 Week 05: AI Image Generator

   For CUDA-enabled systems:

### ✨ Key Features   ```bash

- **🖼️ Text-to-Image Generation**: Transform descriptions into stunning images   pip install -r cuda_torch_requirements.txt

- **🎮 Multiple Interfaces**: Chinese, English, and integrated versions   ```

- **🐕 Specialized Generators**: Cartoon dogs, teddy bears, and custom themes

- **🎛️ Advanced Controls**: ControlNet, LCM models, and parameter tuning3. **Run the main application**

- **📹 Video Processing**: Real-time filters and video enhancement   ```bash

- **🌍 Multi-language Support**: Bilingual interface with full localization   streamlit run streamlit_image_generator.py

   ```

### 🛠️ Technical Stack

- **Framework**: Streamlit web applications## 📁 Project Structure

- **AI Models**: Stable Diffusion v1.5, ControlNet, LCM

- **Libraries**: Diffusers, Transformers, OpenCV, PIL```

- **Hardware**: GPU acceleration with CUDA support├── streamlit_image_generator.py    # Main Streamlit application

├── integrated_ai_app.py           # Multi-feature integrated app

### 🚀 Quick Start├── cartoon_dog_generator.py       # Specialized cartoon dog generator

```bash├── teddy_generator.py             # Teddy bear image generator

cd week05-AI_IMAGE_GENERATOR├── image_processor.py             # Image processing utilities

pip install -r requirements.txt├── advanced_image_processor.py    # Advanced image effects

streamlit run streamlit_image_generator.py├── st_controlnet.py              # ControlNet integration

```├── st_tti_lcm.py                 # LCM (Latent Consistency Model) implementation

├── st_video_stream.py            # Video streaming and filters

### 🎯 Use Cases├── requirements.txt              # Basic dependencies

- **Creative Content**: Generate artwork, illustrations, and designs├── cuda_torch_requirements.txt   # CUDA-optimized dependencies

- **Prototyping**: Quick visual concept development└── README.md                     # This file

- **Education**: Learn AI image generation techniques```

- **Entertainment**: Create custom images and artwork

## 🎮 Applications

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

## 🏆 Project Statistics   - Enable GPU acceleration

   - Reduce inference steps for faster generation

### Week 04 - Lucky AI   - Use LCM models for rapid prototyping

- **Lines of Code**: ~800+ lines

- **Features**: 6 major components## 📚 Learning Resources

- **AI Personalities**: 5 different assistants

- **Memory System**: Advanced context retention### Notebooks

- `week05_notebook.ipynb`: Comprehensive tutorial on AI image generation

### Week 05 - AI Image Generator- `python_classes_tutorial.ipynb`: Python programming fundamentals

- **Lines of Code**: ~2,600+ lines

- **Applications**: 8 different interfaces### Documentation

- **AI Models**: Multiple Stable Diffusion variants- [Stable Diffusion Documentation](https://huggingface.co/docs/diffusers)

- **Image Types**: Unlimited creative possibilities- [Streamlit Documentation](https://docs.streamlit.io/)

- [PyTorch Documentation](https://pytorch.org/docs/)

### Combined Project

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

- **Streamlit**: Amazing web framework for AI applications- Streamlit for the amazing web framework

- **Hugging Face**: Diffusers library and model hosting- The open-source AI community

- **Stability AI**: Stable Diffusion models

- **LMStudio**: Local AI model hosting platform## 🔮 Future Plans

- **OpenAI**: API compatibility and standards

- [ ] Support for more AI models (DALL-E, Midjourney-style)

### Inspiration- [ ] Advanced editing capabilities

- **AI Community**: Open-source AI development community- [ ] Batch generation features

- **Educational Resources**: AI programming course materials- [ ] Custom model training interface

- **User Feedback**: Continuous improvement based on user needs- [ ] API endpoints for integration

- [ ] Mobile-responsive design improvements

---

---

## 📞 Support & Contact

**Happy Creating! 🎨✨**

### Getting Help

1. **Check Documentation**: Review README files for setup instructionsFor questions or support, please open an issue or contact the development team.
2. **Common Issues**: Check troubleshooting sections
3. **GitHub Issues**: Create an issue for bugs or questions
4. **Community Support**: Engage with the AI development community

### Course Information
- **Institution**: AI Programming Course
- **Assignment**: Assignment 03 - 2025
- **Repository**: [assignment03-2025](https://github.com/xueyu-coco/assignment03-2025)

---

**Happy Coding and Creating! 🚀✨**

*Explore the fascinating world of AI through interactive chatbots and creative image generation. These projects demonstrate the practical applications of modern AI technologies in engaging, user-friendly applications.*

---

*Last updated: October 2, 2025*