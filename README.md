<<<<<<< HEAD
# AI Image Generator

A comprehensive AI-powered image generation toolkit built with Stable Diffusion and Streamlit. This project provides multiple applications for creating stunning images from text descriptions, applying image filters, and real-time video processing.

## 🌟 Features

### 🎨 Image Generation
- **Text-to-Image**: Transform text descriptions into beautiful images using Stable Diffusion
- **Preset Prompts**: Quick start with pre-configured prompts for landscapes, animals, sci-fi scenes, and more
- **Advanced Controls**: Fine-tune generation with adjustable steps and guidance scale
- **Negative Prompts**: Specify what you don't want in the generated images
- **GPU Acceleration**: Automatic GPU detection and acceleration when available

### 🖼️ Image Processing
- **Advanced Filters**: Apply various image processing effects
- **ControlNet Integration**: Precise image control using edge detection and other techniques
- **Batch Processing**: Handle multiple images efficiently

### 📹 Video Processing
- **Real-time Filters**: Apply effects to live video streams
- **Video Enhancement**: Improve video quality with AI-powered filters

### 🌍 Multi-language Support
- **Bilingual Interface**: Support for English and Chinese languages
- **Localized Content**: Fully translated user interface and instructions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- NVIDIA GPU (recommended for faster generation)
- CUDA toolkit (for GPU acceleration)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "week05_AI Image Generator"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   For CUDA-enabled systems:
   ```bash
   pip install -r cuda_torch_requirements.txt
   ```

3. **Run the main application**
   ```bash
   streamlit run streamlit_image_generator.py
   ```

## 📁 Project Structure

```
├── streamlit_image_generator.py    # Main Streamlit application
├── integrated_ai_app.py           # Multi-feature integrated app
├── cartoon_dog_generator.py       # Specialized cartoon dog generator
├── teddy_generator.py             # Teddy bear image generator
├── image_processor.py             # Image processing utilities
├── advanced_image_processor.py    # Advanced image effects
├── st_controlnet.py              # ControlNet integration
├── st_tti_lcm.py                 # LCM (Latent Consistency Model) implementation
├── st_video_stream.py            # Video streaming and filters
├── requirements.txt              # Basic dependencies
├── cuda_torch_requirements.txt   # CUDA-optimized dependencies
└── README.md                     # This file
```

## 🎮 Applications

### 1. Main Image Generator (`streamlit_image_generator.py`)
The primary application featuring:
- Intuitive web interface
- Real-time image generation
- Download functionality
- Preset prompts for quick start
- Advanced parameter controls

**Usage:**
```bash
streamlit run streamlit_image_generator.py
```

### 2. Integrated Creative Studio (`integrated_ai_app.py`)
A comprehensive toolkit with:
- Multiple generation modes
- Video processing capabilities
- Multi-language interface
- Advanced image controls

**Usage:**
```bash
streamlit run integrated_ai_app.py
```

### 3. Specialized Generators
- **Cartoon Dog Generator**: Create cute cartoon-style dog images
- **Teddy Generator**: Generate adorable teddy bear images
- **ControlNet**: Precise image control using edge detection

### 4. Video Processing
Real-time video effects and filters for webcam or video files.

## 🛠️ Configuration

### GPU Setup
The application automatically detects and uses GPU acceleration when available. For optimal performance:

1. Install CUDA toolkit
2. Use the CUDA-optimized requirements:
   ```bash
   pip install -r cuda_torch_requirements.txt
   ```

### Model Configuration
The project uses Stable Diffusion v1.5 by default. Models are automatically downloaded on first use and cached for future sessions.

## 📖 Usage Examples

### Basic Text-to-Image Generation
```python
from diffusers import DiffusionPipeline
import torch

# Load the pipeline
pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Generate an image
prompt = "a beautiful landscape with mountains, golden hour lighting"
image = pipe(prompt).images[0]
image.save("generated_image.png")
```

### Using the Cartoon Dog Generator
```python
from cartoon_dog_generator import CartoonDogGenerator

generator = CartoonDogGenerator()
image = generator.generate_cartoon_dog("brown fluffy puppy playing in grass")
```

## 🎨 Prompt Engineering Tips

### Effective Prompts
- **Be specific**: Use detailed descriptions instead of vague terms
- **Include style**: Specify art styles like "oil painting", "cartoon style", "photorealistic"
- **Add quality modifiers**: Use terms like "high quality", "detailed", "professional"
- **Describe lighting**: Include lighting conditions like "soft lighting", "golden hour", "dramatic shadows"

### Example Prompts
- **Landscape**: "serene mountain lake at sunset, golden hour lighting, reflection in water, detailed, cinematic"
- **Portrait**: "portrait of a wise old wizard, detailed face, magical atmosphere, fantasy art style"
- **Animal**: "cute red panda sitting on bamboo, fluffy fur, adorable expression, soft lighting"

### Negative Prompts
Use negative prompts to avoid unwanted elements:
- "blurry, low quality, distorted, ugly, poorly drawn"
- "extra limbs, deformed, mutated, bad anatomy"

## 🔧 Technical Details

### Dependencies
- **Streamlit**: Web interface framework
- **Diffusers**: Hugging Face diffusion models
- **Transformers**: Natural language processing
- **OpenCV**: Computer vision and image processing
- **PIL/Pillow**: Image manipulation
- **PyTorch**: Deep learning framework

### System Requirements
- **Minimum**: 8GB RAM, Intel i5 or equivalent
- **Recommended**: 16GB+ RAM, NVIDIA RTX 3060 or better
- **Storage**: 10GB+ free space for models

### Performance Optimization
- **GPU Memory**: Adjust batch size based on available VRAM
- **CPU Mode**: Increase swap file size for CPU-only systems
- **Model Caching**: Models are cached locally after first download

## 🐛 Troubleshooting

### Common Issues

1. **Out of Memory Error**
   - Reduce image resolution
   - Lower the number of inference steps
   - Close other GPU-intensive applications

2. **Model Download Issues**
   - Check internet connection
   - Ensure sufficient disk space
   - Try running with administrator privileges

3. **CUDA Not Found**
   - Install appropriate CUDA toolkit version
   - Verify PyTorch CUDA installation: `torch.cuda.is_available()`

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

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgments

- Hugging Face for the Diffusers library
- Stability AI for Stable Diffusion
- Streamlit for the amazing web framework
- The open-source AI community

## 🔮 Future Plans

- [ ] Support for more AI models (DALL-E, Midjourney-style)
- [ ] Advanced editing capabilities
- [ ] Batch generation features
- [ ] Custom model training interface
- [ ] API endpoints for integration
- [ ] Mobile-responsive design improvements

---

**Happy Creating! 🎨✨**

For questions or support, please open an issue or contact the development team.
=======
# assignment03-2025
>>>>>>> 24f1596a9bf32225d8afab231e271d2158ddfa3f
