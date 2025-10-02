# Week 05: AI Creative Studio

A comprehensive AI-powered creative toolkit built with Stable Diffusion and Streamlit. This project provides an integrated creative studio for generating stunning images from text descriptions, applying real-time video effects, face detection with AI-generated overlays, and dynamic visual compositions.

## 🌟 Features

### 🎨 AI Image Generation
- **Text-to-Image**: Transform text descriptions into beautiful images using Stable Diffusion
- **Fast Generation**: Optimized with LCM (Latent Consistency Model) for quick results
- **Multiple Animal Styles**: Generate cartoon animals, teddy bears, dogs, and more
- **Advanced Controls**: Fine-tune generation with adjustable steps and guidance scale
- **Negative Prompts**: Specify what you don't want in the generated images
- **GPU Acceleration**: Automatic GPU detection and acceleration when available

### � Real-time Video Processing
- **Live Face Detection**: Real-time face detection using OpenCV Haar cascades
- **Dynamic AI Overlays**: Apply AI-generated images to detected faces in real-time
- **Video Filters**: Apply various effects and filters to live video streams
- **Thread-safe Processing**: Robust video processing with proper synchronization
- **Dynamic Effects**: Scaling, rotation, and positioning of overlay images

### � Combined Creative Studio
- **Integrated Interface**: Unified application combining all features
- **Multiple Modes**: Switch between image generation, video filters, and composition modes
- **Image Gallery**: Browse and manage generated images
- **Real-time Preview**: Live preview of effects and generations
- **Export Functionality**: Save and download created content

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

2. **Run the Combined Creative Studio (Recommended)**
   ```bash
   streamlit run combined_creative_studio.py
   ```

   Or run individual applications:
   ```bash
   streamlit run streamlit_image_generator.py
   ```

## 📁 Project Files

### Main Applications
- `combined_creative_studio.py` - **NEW!** Integrated Creative Studio with all features
- `streamlit_image_generator.py` - Main Streamlit application (Chinese)
- `streamlit_image_generator_en.py` - English version of the main app
- `integrated_ai_app.py` - Multi-feature integrated app with video processing

### Video & Real-time Processing
- `st_video_stream.py` - Video streaming and real-time filters with face detection
- `st_controlnet.py` - ControlNet integration for precise image control
- `st_tti_lcm.py` - LCM (Latent Consistency Model) implementation

### Specialized Generators
- `cartoon_dog_generator.py` - Specialized cartoon dog generator
- `teddy_generator.py` - Teddy bear image generator
- `teddy_dog_generator.py` - Combined teddy and dog generator

### Image Processing
- `image_processor.py` - Basic image processing utilities
- `advanced_image_processor.py` - Advanced image effects and filters

### Additional Features
- `4_controlnet_canny.py` - Canny edge detection with ControlNet
- `2_gen_image.py` - Basic image generation script
- `3_gen_image_lcm.py` - LCM-based image generation
- `1_random_image.py` - Random image generation examples

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

### 1. Combined Creative Studio (Recommended)
```bash
streamlit run combined_creative_studio.py
```
**Features:**
- Unified interface with all capabilities
- AI image generation with multiple animal types
- Real-time video processing with face detection
- Dynamic AI-generated overlays on detected faces
- Image gallery and management

### 2. Individual Applications
```bash
# Main image generator
streamlit run streamlit_image_generator.py

# English version
streamlit run streamlit_image_generator_en.py

# Integrated app with video features
streamlit run integrated_ai_app.py
```

### 3. Video Processing with Face Detection
```bash
streamlit run st_video_stream.py
```
Features real-time face detection and AI-generated image overlays.

### 4. Specialized Generators
```python
from cartoon_dog_generator import CartoonDogGenerator
generator = CartoonDogGenerator()
image = generator.generate_cartoon_dog("brown fluffy puppy playing in grass")
```

## 🛠️ Technical Details

### Dependencies
- **Streamlit**: Web interface framework
- **streamlit-webrtc**: Real-time video processing
- **Diffusers**: Hugging Face diffusion models
- **Transformers**: Natural language processing
- **OpenCV**: Computer vision and face detection
- **PIL/Pillow**: Image manipulation
- **PyTorch**: Deep learning framework
- **Threading**: Multi-threaded processing for real-time features

### System Requirements
- **Minimum**: 8GB RAM, Intel i5 or equivalent
- **Recommended**: 16GB+ RAM, NVIDIA RTX 3060 or better
- **Storage**: 10GB+ free space for models

## 🎨 Creative Tips

### AI Image Generation
- **Animal Prompts**: "cute brown teddy bear sitting in garden, fluffy fur, adorable expression"
- **Cartoon Style**: "cartoon style brown dog, big eyes, happy expression, children's book illustration"
- **Quality Enhancers**: Add "high quality, detailed, professional" to improve results

### Video Effects
- **Face Detection**: Ensure good lighting for optimal face detection
- **Dynamic Overlays**: Generated images automatically scale and position on detected faces
- **Real-time Performance**: Use GPU acceleration for smooth video processing

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
The project uses Stable Diffusion v1.5 with LCM (Latent Consistency Model) for fast generation. Models are automatically downloaded on first use and cached for future sessions.

### Video Processing
- **Face Detection**: Uses OpenCV Haar cascades for real-time face detection
- **Thread Safety**: Implements thread-safe communication between UI and video processing
- **File Caching**: Uses pickle-based caching for cross-thread image sharing
- **WebRTC**: Leverages streamlit-webrtc for real-time video streaming

## 🚀 New Features in Combined Creative Studio

### Integrated Workflow
1. **Generate AI Images**: Create custom cartoon animals and characters
2. **Apply to Video**: Use generated images as dynamic overlays on detected faces
3. **Real-time Processing**: See effects applied instantly in live video
4. **Gallery Management**: Save and reuse generated images

### Face Detection & AI Overlay
- Automatic face detection in real-time video
- Dynamic scaling and positioning of AI-generated images
- Thread-safe image sharing between generation and video processing
- Support for multiple face detection with individual overlays

---

**Create Amazing AI-Powered Visual Experiences! 🎨✨**

This project demonstrates the integration of AI image generation with real-time video processing, showcasing practical applications of modern AI technologies in creative workflows.