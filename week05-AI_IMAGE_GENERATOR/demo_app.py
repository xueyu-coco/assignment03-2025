import streamlit as st
from PIL import Image
import os

# 页面配置
st.set_page_config(
    page_title="AI Image Generator Demo",
    page_icon="🎨",
    layout="wide"
)

# 标题
st.title("🎨 AI Image Generator Demo")
st.markdown("### Welcome to the AI Image Generation Toolkit")

# 侧边栏
with st.sidebar:
    st.header("🖼️ Gallery")
    st.markdown("Here are some example generated images:")

# 主要内容
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 About This Project")
    st.markdown("""
    This is a comprehensive AI-powered image generation toolkit featuring:
    
    **🎨 Main Features:**
    - Text-to-Image Generation using Stable Diffusion
    - Specialized generators (Cartoon Dogs, Teddy Bears)
    - Advanced image processing tools
    - Real-time video filters
    - Multi-language support (English & Chinese)
    
    **🛠️ Technology Stack:**
    - Streamlit for web interface
    - Stable Diffusion for AI image generation
    - OpenCV for image processing
    - PyTorch for deep learning
    """)
    
    st.subheader("🚀 Available Applications")
    st.markdown("""
    1. **Main Image Generator** (`streamlit_image_generator.py`)
    2. **English Version** (`streamlit_image_generator_en.py`)
    3. **Integrated Creative Studio** (`integrated_ai_app.py`)
    4. **Cartoon Dog Generator** (`cartoon_dog_generator.py`)
    5. **Video Stream Processor** (`st_video_stream.py`)
    """)

with col2:
    st.subheader("🖼️ Generated Images Gallery")
    
    # 查找并显示项目中的图片
    image_files = []
    for file in os.listdir("."):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(file)
    
    if image_files:
        # 显示图片网格
        cols = st.columns(2)
        for i, img_file in enumerate(image_files[:6]):  # 只显示前6张图片
            try:
                img = Image.open(img_file)
                with cols[i % 2]:
                    st.image(img, caption=img_file, use_container_width=True)
            except Exception as e:
                st.error(f"无法加载图片 {img_file}: {e}")
    else:
        st.info("No generated images found in the current directory.")

# 使用说明
st.markdown("---")
st.subheader("📖 How to Use")

tab1, tab2, tab3 = st.tabs(["🎨 Basic Generation", "🐕 Specialized Generators", "⚙️ Setup"])

with tab1:
    st.markdown("""
    ### Text-to-Image Generation
    1. **Describe your image**: Enter a detailed description of what you want to generate
    2. **Adjust settings**: Fine-tune generation parameters like steps and guidance scale
    3. **Generate**: Click the generate button and wait for AI to create your image
    4. **Download**: Save your generated image
    
    **Example prompts:**
    - "A beautiful landscape with mountains and lakes at sunset"
    - "Cute cartoon dog playing in a garden"
    - "Futuristic cityscape with flying cars"
    """)

with tab2:
    st.markdown("""
    ### Specialized Generators
    
    **🐕 Cartoon Dog Generator:**
    - Generates cute cartoon-style dogs
    - Various breeds and poses
    - Customizable styles and colors
    
    **🧸 Teddy Bear Generator:**
    - Creates adorable teddy bear images
    - Different sizes and expressions
    - Various backgrounds and settings
    """)

with tab3:
    st.markdown("""
    ### Installation & Setup
    
    **Prerequisites:**
    ```bash
    pip install streamlit diffusers accelerate transformers opencv-python torch
    ```
    
    **Run the applications:**
    ```bash
    # Main Chinese interface
    streamlit run streamlit_image_generator.py
    
    # English interface
    streamlit run streamlit_image_generator_en.py
    
    # Integrated studio
    streamlit run integrated_ai_app.py
    ```
    
    **System Requirements:**
    - Python 3.8+
    - 8GB+ RAM (16GB recommended)
    - NVIDIA GPU with CUDA (optional but recommended)
    """)

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
<p>🎨 AI Image Generator Toolkit | Made with ❤️ using Streamlit</p>
<p>This demo showcases the capabilities of our AI image generation project.</p>
</div>
""", unsafe_allow_html=True)