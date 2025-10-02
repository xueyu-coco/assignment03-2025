# Week 05: AI Image Generator

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

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   For CUDA-enabled systems:
   ```bash
   pip install -r cuda_torch_requirements.txt
   ```

2. **Run the main application**
   ```bash
   streamlit run streamlit_image_generator.py
   ```

## 📁 Project Files

### Main Applications
- `streamlit_image_generator.py` - Main Streamlit application (Chinese)
- `streamlit_image_generator_en.py` - English version of the main app
- `integrated_ai_app.py` - Multi-feature integrated app with video processing

### Specialized Generators
- `cartoon_dog_generator.py` - Specialized cartoon dog generator
- `teddy_generator.py` - Teddy bear image generator
- `teddy_dog_generator.py` - Combined teddy and dog generator

### Image Processing
- `image_processor.py` - Basic image processing utilities
- `advanced_image_processor.py` - Advanced image effects and filters

### Additional Features
- `st_controlnet.py` - ControlNet integration for precise image control
- `st_tti_lcm.py` - LCM (Latent Consistency Model) implementation
- `st_video_stream.py` - Video streaming and real-time filters
- `2_gen_image.py` - Basic image generation script
- `3_gen_image_lcm.py` - LCM-based image generation
- `4_controlnet_canny.py` - Canny edge detection with ControlNet

### Configuration
- `requirements.txt` - Basic dependencies
- `cuda_torch_requirements.txt` - CUDA-optimized dependencies

### Generated Images
The project includes several example generated images:
- `basic_teddy.png` - Basic teddy bear generation
- `gallery_teddy_*.png` - Gallery of teddy bear images
- `brown_cartoon_dog_style_*.png` - Cartoon dog variations
- `teddy_dog_brown_curly_fur_sitt_*.png` - Combined teddy-dog images

## 🎮 Usage Examples

### 1. Main Image Generator
```bash
streamlit run streamlit_image_generator.py
```
Features intuitive web interface with real-time generation and download functionality.

### 2. English Version
```bash
streamlit run streamlit_image_generator_en.py
```
English interface for international users.

### 3. Integrated Creative Studio
```bash
streamlit run integrated_ai_app.py
```
Comprehensive toolkit with multiple generation modes and video processing.

### 4. Specialized Generators
```python
from cartoon_dog_generator import CartoonDogGenerator
generator = CartoonDogGenerator()
image = generator.generate_cartoon_dog("brown fluffy puppy playing in grass")
```

## 🛠️ Technical Details

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

## 🎨 Prompt Engineering Tips

### Effective Prompts
- **Be specific**: Use detailed descriptions instead of vague terms
- **Include style**: Specify art styles like "oil painting", "cartoon style", "photorealistic"
- **Add quality modifiers**: Use terms like "high quality", "detailed", "professional"
- **Describe lighting**: Include lighting conditions like "soft lighting", "golden hour"

### Example Prompts
- **Landscape**: "serene mountain lake at sunset, golden hour lighting, reflection in water, detailed, cinematic"
- **Portrait**: "portrait of a wise old wizard, detailed face, magical atmosphere, fantasy art style"
- **Animal**: "cute red panda sitting on bamboo, fluffy fur, adorable expression, soft lighting"

### Negative Prompts
Use negative prompts to avoid unwanted elements:
- "blurry, low quality, distorted, ugly, poorly drawn"
- "extra limbs, deformed, mutated, bad anatomy"

## 🔧 Configuration

### GPU Setup
The application automatically detects and uses GPU acceleration when available. For optimal performance:

1. Install CUDA toolkit
2. Use the CUDA-optimized requirements:
   ```bash
   pip install -r cuda_torch_requirements.txt
   ```

### Model Configuration
The project uses Stable Diffusion v1.5 by default. Models are automatically downloaded on first use and cached for future sessions.

---

**Happy Creating! 🎨✨**

This is part of the AI programming course Week 05 assignment focusing on practical AI image generation applications.