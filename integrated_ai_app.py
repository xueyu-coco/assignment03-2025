import streamlit as st
from diffusers import DiffusionPipeline
import torch
from PIL import Image, ImageDraw
import io
import time
import os
import cv2
import numpy as np
import av
from streamlit_webrtc import webrtc_streamer

# Language configurations
LANGUAGES = {
    "English": {
        "page_title": "AI Creative Studio",
        "page_header": "🎨 AI Creative Studio",
        "page_subtitle": "### Your all-in-one AI creative toolkit",
        "sidebar_language": "🌍 Language",
        "sidebar_navigation": "📱 Navigation",
        "nav_image_gen": "🎨 Image Generator",
        "nav_video_filter": "📹 Video Filter",
        
        # Image Generator
        "img_title": "🎨 AI Image Generator",
        "img_subtitle": "Transform text descriptions into beautiful images using Stable Diffusion",
        "sidebar_settings": "⚙️ Generation Settings",
        "preset_prompts": "Choose preset prompt:",
        "advanced_settings": "🔧 Advanced Settings",
        "system_status": "💻 System Status",
        "input_description": "📝 Input Description",
        "generation_result": "🖼️ Generation Result",
        "prompt_label": "Image description (prompt):",
        "prompt_help": "Describe in detail what image you want to generate, including style, colors, composition, etc.",
        "negative_prompt_label": "Negative prompt (content to avoid):",
        "negative_prompt_help": "Describe what you don't want to appear in the image",
        "generate_button": "🎨 Generate Image",
        "steps_label": "Generation steps",
        "steps_help": "More steps usually produce better quality but take longer",
        "guidance_label": "Guidance scale",
        "guidance_help": "Controls how closely AI follows the prompt",
        "gpu_available": "GPU: ",
        "cuda_version": "CUDA Version: ",
        "gpu_unavailable": "GPU unavailable, using CPU",
        "gpu_enabled": "✅ GPU acceleration enabled",
        "gpu_warning": "⚠️ Using CPU mode, generation will be slower",
        "model_error": "Model loading failed: ",
        "generation_error": "Image generation failed: ",
        "generating": "Generating image...",
        "generation_complete": "✅ Generation complete! Time: ",
        "download_button": "📥 Download Image",
        "prompt_warning": "⚠️ Please enter an image description",
        "usage_instructions": "📖 Usage Instructions",
        "example_gallery": "🖼️ Example Gallery",
        "preset_landscape": "a beautiful landscape with mountains, lakes, and trees, golden hour lighting",
        "preset_animal": "a cute fluffy kitten playing in a garden, soft lighting, adorable",
        "preset_scifi": "futuristic cityscape with flying cars, neon lights, cyberpunk style",
        "preset_portrait": "portrait of a person, artistic style, detailed, professional lighting",
        "preset_cartoon": "cartoon style illustration, colorful, friendly, animated character",
        "negative_default": "blurry, low quality, distorted, ugly",
        "default_prompt": "a beautiful landscape with mountains",
        
        # Video Filter
        "video_title": "🎭 Custom Image Video Filter",
        "video_subtitle": "Add your custom image at detected face locations in real-time video",
        "video_info1": "📹 Once the camera is enabled, the app will automatically detect faces and display your custom image at face locations",
        "video_info2": "🎭 If no faces are detected, your custom image will appear in the center of the screen",
        "current_image": "📸 Current Image",
        "image_loaded": "✅ Image loaded successfully",
        "image_not_found": "❌ Image file not found",
        "fallback_warning": "Using fallback teddy dog image",
        "image_path_label": "Image Path:",
        "browse_button": "📁 Browse Image",
        "upload_image": "📤 Upload Image"
    },
    "中文": {
        "page_title": "AI创意工作室",
        "page_header": "🎨 AI创意工作室", 
        "page_subtitle": "### 您的一体化AI创意工具包",
        "sidebar_language": "🌍 语言",
        "sidebar_navigation": "📱 导航",
        "nav_image_gen": "🎨 图像生成器",
        "nav_video_filter": "📹 视频滤镜",
        
        # Image Generator
        "img_title": "🎨 AI图像生成器",
        "img_subtitle": "使用Stable Diffusion将文本描述转换为精美图像",
        "sidebar_settings": "⚙️ 生成设置",
        "preset_prompts": "选择预设提示词：",
        "advanced_settings": "🔧 高级设置",
        "system_status": "💻 系统状态",
        "input_description": "📝 输入描述",
        "generation_result": "🖼️ 生成结果",
        "prompt_label": "图像描述（提示词）：",
        "prompt_help": "详细描述你想要生成的图像，包括风格、颜色、构图等",
        "negative_prompt_label": "负面提示词（要避免的内容）：",
        "negative_prompt_help": "描述你不希望在图像中出现的内容",
        "generate_button": "🎨 生成图像",
        "steps_label": "生成步数",
        "steps_help": "更多步数通常产生更好的质量，但需要更长时间",
        "guidance_label": "引导比例",
        "guidance_help": "控制AI遵循提示词的程度",
        "gpu_available": "GPU: ",
        "cuda_version": "CUDA版本: ",
        "gpu_unavailable": "GPU不可用，使用CPU",
        "gpu_enabled": "✅ GPU加速已启用",
        "gpu_warning": "⚠️ 使用CPU模式，生成速度较慢",
        "model_error": "模型加载失败: ",
        "generation_error": "图像生成失败: ",
        "generating": "正在生成图像...",
        "generation_complete": "✅ 生成完成！用时: ",
        "download_button": "📥 下载图像",
        "prompt_warning": "⚠️ 请输入图像描述",
        "usage_instructions": "📖 使用说明",
        "example_gallery": "🖼️ 示例画廊",
        "preset_landscape": "美丽的风景，有山峰、湖泊和树木，黄金时光照明",
        "preset_animal": "可爱的毛茸茸小猫在花园里玩耍，柔和的光线，adorable",
        "preset_scifi": "未来主义城市景观，有飞行汽车，霓虹灯，赛博朋克风格",
        "preset_portrait": "人物肖像，艺术风格，详细，专业照明",
        "preset_cartoon": "卡通风格插图，色彩鲜艳，友好，动画角色",
        "negative_default": "模糊，低质量，扭曲，丑陋",
        "default_prompt": "美丽的山峰风景",
        
        # Video Filter
        "video_title": "🎭 自定义图像视频滤镜",
        "video_subtitle": "在实时视频中检测到的人脸位置添加自定义图像",
        "video_info1": "📹 开启摄像头后，应用会自动检测人脸并在人脸位置显示自定义图像",
        "video_info2": "🎭 如果没有检测到人脸，自定义图像会出现在屏幕中央",
        "current_image": "📸 当前图像",
        "image_loaded": "✅ 图像加载成功",
        "image_not_found": "❌ 图像文件未找到",
        "fallback_warning": "使用备用泰迪狗图像",
        "image_path_label": "图像路径：",
        "browse_button": "📁 浏览图像",
        "upload_image": "📤 上传图像"
    },
    "粤语": {
        "page_title": "AI創意工作室",
        "page_header": "🎨 AI創意工作室",
        "page_subtitle": "### 你嘅一體化AI創意工具包",
        "sidebar_language": "🌍 語言",
        "sidebar_navigation": "📱 導航",
        "nav_image_gen": "🎨 圖像生成器",
        "nav_video_filter": "📹 視頻濾鏡",
        
        # Image Generator
        "img_title": "🎨 AI圖像生成器",
        "img_subtitle": "用Stable Diffusion將文字描述變成靚靚嘅圖像",
        "sidebar_settings": "⚙️ 生成設定",
        "preset_prompts": "揀預設提示詞：",
        "advanced_settings": "🔧 進階設定",
        "system_status": "💻 系統狀態",
        "input_description": "📝 輸入描述",
        "generation_result": "🖼️ 生成結果",
        "prompt_label": "圖像描述（提示詞）：",
        "prompt_help": "詳細描述你想要生成嘅圖像，包括風格、顏色、構圖等",
        "negative_prompt_label": "負面提示詞（要避免嘅內容）：",
        "negative_prompt_help": "描述你唔想喺圖像入面出現嘅內容",
        "generate_button": "🎨 生成圖像",
        "steps_label": "生成步數",
        "steps_help": "更多步數通常產生更好嘅質量，但需要更長時間",
        "guidance_label": "引導比例",
        "guidance_help": "控制AI跟從提示詞嘅程度",
        "gpu_available": "GPU: ",
        "cuda_version": "CUDA版本: ",
        "gpu_unavailable": "GPU唔可用，用CPU",
        "gpu_enabled": "✅ GPU加速已啟用",
        "gpu_warning": "⚠️ 用緊CPU模式，生成速度比較慢",
        "model_error": "模型加載失敗: ",
        "generation_error": "圖像生成失敗: ",
        "generating": "正在生成圖像...",
        "generation_complete": "✅ 生成完成！用時: ",
        "download_button": "📥 下載圖像",
        "prompt_warning": "⚠️ 請輸入圖像描述",
        "usage_instructions": "📖 使用說明",
        "example_gallery": "🖼️ 示例畫廊",
        "preset_landscape": "靚靚嘅風景，有山峰、湖泊同樹木，黃金時光照明",
        "preset_animal": "可愛嘅毛茸茸小貓喺花園入面玩，柔和嘅光線，adorable",
        "preset_scifi": "未來主義城市景觀，有飛行汽車，霓虹燈，賽博朋克風格",
        "preset_portrait": "人物肖像，藝術風格，詳細，專業照明",
        "preset_cartoon": "卡通風格插圖，色彩鮮艷，友好，動畫角色",
        "negative_default": "模糊，低質量，扭曲，醜樣",
        "default_prompt": "靚靚嘅山峰風景",
        
        # Video Filter
        "video_title": "🎭 自定義圖像視頻濾鏡",
        "video_subtitle": "喺實時視頻中檢測到嘅人臉位置添加自定義圖像",
        "video_info1": "📹 開啟攝像頭後，應用會自動檢測人臉並喺人臉位置顯示自定義圖像",
        "video_info2": "🎭 如果冇檢測到人臉，自定義圖像會出現喺屏幕中央",
        "current_image": "📸 當前圖像",
        "image_loaded": "✅ 圖像加載成功",
        "image_not_found": "❌ 圖像文件未搵到",
        "fallback_warning": "使用備用泰迪狗圖像",
        "image_path_label": "圖像路徑：",
        "browse_button": "📁 瀏覽圖像",
        "upload_image": "📤 上傳圖像"
    }
}

# Page configuration
st.set_page_config(
    page_title="AI Creative Studio",
    page_icon="🎨",
    layout="wide"
)

# Load custom image from file for video filter
def load_custom_image(image_path, size=(100, 100)):
    """Load and process custom image for overlay"""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            img = img.resize(size, Image.Resampling.LANCZOS)
            return img
        else:
            return create_teddy_dog_image(size)
    except Exception as e:
        return create_teddy_dog_image(size)

# Fallback teddy dog image creation
def create_teddy_dog_image(size=(100, 100)):
    """Create a simple teddy dog avatar"""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    head_size = min(size) * 0.8
    head_x = size[0] // 2
    head_y = size[1] // 2
    head_radius = head_size // 2
    
    # Draw head
    draw.ellipse([
        head_x - head_radius, head_y - head_radius,
        head_x + head_radius, head_y + head_radius
    ], fill=(139, 90, 43, 255))
    
    # Draw ears
    ear_size = head_radius * 0.4
    draw.ellipse([
        head_x - head_radius * 0.8 - ear_size//2, head_y - head_radius * 0.8 - ear_size//2,
        head_x - head_radius * 0.8 + ear_size//2, head_y - head_radius * 0.8 + ear_size//2
    ], fill=(101, 67, 33, 255))
    draw.ellipse([
        head_x + head_radius * 0.8 - ear_size//2, head_y - head_radius * 0.8 - ear_size//2,
        head_x + head_radius * 0.8 + ear_size//2, head_y - head_radius * 0.8 + ear_size//2
    ], fill=(101, 67, 33, 255))
    
    # Draw eyes
    eye_size = head_radius * 0.15
    draw.ellipse([
        head_x - head_radius * 0.3 - eye_size, head_y - head_radius * 0.2 - eye_size,
        head_x - head_radius * 0.3 + eye_size, head_y - head_radius * 0.2 + eye_size
    ], fill=(0, 0, 0, 255))
    draw.ellipse([
        head_x + head_radius * 0.3 - eye_size, head_y - head_radius * 0.2 - eye_size,
        head_x + head_radius * 0.3 + eye_size, head_y - head_radius * 0.2 + eye_size
    ], fill=(0, 0, 0, 255))
    
    # Draw nose
    nose_size = head_radius * 0.1
    draw.ellipse([
        head_x - nose_size, head_y + head_radius * 0.1 - nose_size,
        head_x + nose_size, head_y + head_radius * 0.1 + nose_size
    ], fill=(0, 0, 0, 255))
    
    # Draw mouth
    mouth_width = head_radius * 0.3
    draw.arc([
        head_x - mouth_width, head_y + head_radius * 0.2,
        head_x + mouth_width, head_y + head_radius * 0.4
    ], start=0, end=180, fill=(0, 0, 0, 255), width=3)
    
    return img

# Initialize model for image generation
@st.cache_resource
def load_model():
    """Load and cache Stable Diffusion model"""
    try:
        pipe = DiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        if torch.cuda.is_available():
            pipe = pipe.to("cuda")
        return pipe
    except Exception as e:
        return None

def generate_image(pipe, prompt, negative_prompt="", steps=20, guidance_scale=7.5):
    """Generate image"""
    try:
        with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
            result = pipe(
                prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=steps,
                guidance_scale=guidance_scale
            )
            return result.images[0]
    except Exception as e:
        return None

# Video filter functions
def overlay_custom_image(img, x, y, scale=1.0, overlay_array=None):
    """Overlay custom image at specified position"""
    if overlay_array is None:
        return img
        
    img_height, img_width = overlay_array.shape[:2]
    new_height = int(img_height * scale)
    new_width = int(img_width * scale)
    
    if new_height <= 0 or new_width <= 0:
        return img
    
    resized_img = cv2.resize(overlay_array, (new_width, new_height))
    
    y1 = max(0, y - new_height // 2)
    y2 = min(img.shape[0], y1 + new_height)
    x1 = max(0, x - new_width // 2)
    x2 = min(img.shape[1], x1 + new_width)
    
    actual_height = y2 - y1
    actual_width = x2 - x1
    
    if actual_height <= 0 or actual_width <= 0:
        return img
    
    img_roi = resized_img[:actual_height, :actual_width]
    
    if img_roi.shape[2] == 4:  # RGBA
        alpha = img_roi[:, :, 3] / 255.0
        for c in range(3):  # BGR
            img[y1:y2, x1:x2, c] = (
                alpha * img_roi[:, :, c] + 
                (1 - alpha) * img[y1:y2, x1:x2, c]
            )
    else:  # RGB
        img[y1:y2, x1:x2] = img_roi[:, :, :3]
    
    return img

def main():
    # Initialize session state
    if 'language' not in st.session_state:
        st.session_state.language = "English"
    if 'page' not in st.session_state:
        st.session_state.page = "Image Generator"
    if 'custom_image_path' not in st.session_state:
        st.session_state.custom_image_path = r"C:\Users\lxy\Desktop\1624425308015_5589c28e_29447(1).png"
    
    # Get current language texts
    texts = LANGUAGES[st.session_state.language]
    
    # Title and description
    st.title(texts["page_header"])
    st.markdown(texts["page_subtitle"])
    
    # Sidebar
    with st.sidebar:
        # Language selector
        st.header(texts["sidebar_language"])
        language = st.selectbox(
            "Select Language / 选择语言 / 揀語言:",
            ["English", "中文", "粤语"],
            index=["English", "中文", "粤语"].index(st.session_state.language)
        )
        
        if language != st.session_state.language:
            st.session_state.language = language
            st.rerun()
        
        st.header(texts["sidebar_navigation"])
        page = st.selectbox(
            "Choose Function:",
            [texts["nav_image_gen"], texts["nav_video_filter"]]
        )
        
        # Update page state
        if page == texts["nav_image_gen"]:
            st.session_state.page = "Image Generator"
        else:
            st.session_state.page = "Video Filter"
    
    # Main content based on selected page
    if st.session_state.page == "Image Generator":
        show_image_generator(texts)
    else:
        show_video_filter(texts)

def show_image_generator(texts):
    """Display the image generator interface"""
    st.header(texts["img_title"])
    st.markdown(f"### {texts['img_subtitle']}")
    
    with st.sidebar:
        st.header(texts["sidebar_settings"])
        
        # Preset prompts
        preset_prompts = {
            "Select preset...": "",
            "Beautiful Landscape": texts["preset_landscape"],
            "Cute Animal": texts["preset_animal"],
            "Sci-fi Scene": texts["preset_scifi"],
            "Art Portrait": texts["preset_portrait"],
            "Cartoon Style": texts["preset_cartoon"]
        }
        
        selected_preset = st.selectbox(texts["preset_prompts"], list(preset_prompts.keys()))
        
        # Advanced settings
        st.subheader(texts["advanced_settings"])
        steps = st.slider(texts["steps_label"], min_value=10, max_value=50, value=20, 
                         help=texts["steps_help"])
        guidance_scale = st.slider(texts["guidance_label"], min_value=1.0, max_value=20.0, value=7.5, step=0.5,
                                 help=texts["guidance_help"])
        
        # GPU status display
        st.subheader(texts["system_status"])
        if torch.cuda.is_available():
            st.success(f"{texts['gpu_available']}{torch.cuda.get_device_name(0)}")
            st.info(f"{texts['cuda_version']}{torch.version.cuda}")
        else:
            st.warning(texts["gpu_unavailable"])
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(texts["input_description"])
        
        # Main prompt
        if selected_preset != "Select preset...":
            default_prompt = preset_prompts[selected_preset]
        else:
            default_prompt = texts["default_prompt"]
            
        prompt = st.text_area(
            texts["prompt_label"], 
            value=default_prompt,
            height=100,
            help=texts["prompt_help"]
        )
        
        # Negative prompt
        negative_prompt = st.text_area(
            texts["negative_prompt_label"],
            value=texts["negative_default"],
            height=60,
            help=texts["negative_prompt_help"]
        )
        
        # Generate button
        generate_button = st.button(texts["generate_button"], type="primary", use_container_width=True)
    
    with col2:
        st.subheader(texts["generation_result"])
        
        # Create placeholders for displaying images
        image_placeholder = st.empty()
        info_placeholder = st.empty()
        download_placeholder = st.empty()
    
    # Handle generation request
    if generate_button and prompt.strip():
        # Load model
        pipe = load_model()
        
        if pipe is not None:
            # Show progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text(texts["generating"])
            start_time = time.time()
            
            # Simulate progress updates
            for i in range(steps):
                progress_bar.progress((i + 1) / steps)
                time.sleep(0.1)
            
            # Generate image
            image = generate_image(pipe, prompt, negative_prompt, steps, guidance_scale)
            
            if image is not None:
                # Calculate generation time
                generation_time = time.time() - start_time
                
                # Display image
                with col2:
                    image_placeholder.image(image, caption=prompt, use_container_width=True)
                    
                    # Show information
                    info_placeholder.info(f"{texts['generation_complete']}{generation_time:.2f}s")
                    
                    # Prepare download
                    img_buffer = io.BytesIO()
                    image.save(img_buffer, format='PNG')
                    img_data = img_buffer.getvalue()
                    
                    # Download button
                    download_placeholder.download_button(
                        label=texts["download_button"],
                        data=img_data,
                        file_name=f"ai_generated_{int(time.time())}.png",
                        mime="image/png",
                        use_container_width=True
                    )
            
            # Clear progress display
            progress_bar.empty()
            status_text.empty()
    
    elif generate_button and not prompt.strip():
        st.warning(texts["prompt_warning"])

def show_video_filter(texts):
    """Display the video filter interface"""
    st.header(texts["video_title"])
    st.markdown(f"### {texts['video_subtitle']}")
    
    # Control options
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(texts["video_info1"])
    
    with col2:
        st.info(texts["video_info2"])
    
    # Image upload/selection section
    with st.sidebar:
        st.header(texts["current_image"])
        
        # File uploader
        uploaded_file = st.file_uploader(
            texts["upload_image"],
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
            accept_multiple_files=False
        )
        
        # Use uploaded file or default path
        if uploaded_file is not None:
            # Save uploaded file temporarily
            temp_path = f"temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            current_image_path = temp_path
            st.success(texts["image_loaded"])
        else:
            current_image_path = st.session_state.custom_image_path
            st.text(f"{texts['image_path_label']}")
            st.code(current_image_path)
        
        # Check if image exists and show preview
        if os.path.exists(current_image_path):
            st.success(texts["image_loaded"])
            try:
                preview_img = Image.open(current_image_path)
                preview_img.thumbnail((150, 150))
                st.image(preview_img, caption="Image Preview")
            except Exception as e:
                st.error(f"Error loading image: {e}")
        else:
            st.error(texts["image_not_found"])
            st.warning(texts["fallback_warning"])
    
    # Load the overlay image
    overlay_img = load_custom_image(current_image_path if os.path.exists(current_image_path) else "")
    overlay_array = np.array(overlay_img)
    
    # Video frame callback function
    def video_frame_callback(frame):
        img = frame.to_ndarray(format="bgr24")
        
        try:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Add custom image at each detected face location
            for (x, y, w, h) in faces:
                center_x = x + w // 2
                center_y = y + h // 2
                scale = w / 100.0
                img = overlay_custom_image(img, center_x, center_y, scale, overlay_array)
        
        except Exception as e:
            # If face detection fails, add image in center
            center_x = img.shape[1] // 2
            center_y = img.shape[0] // 2
            img = overlay_custom_image(img, center_x, center_y, 1.5, overlay_array)
        
        return av.VideoFrame.from_ndarray(img, format="bgr24")
    
    # Video stream component
    webrtc_streamer(
        key="integrated_video_filter",
        video_frame_callback=video_frame_callback,
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        }
    )
    
    # Usage instructions
    with st.expander(texts["usage_instructions"]):
        st.markdown(f"""
        ### {texts["usage_instructions"]}:
        
        **{texts["nav_image_gen"]}:**
        - {texts["img_subtitle"]}
        - {texts["prompt_help"]}
        
        **{texts["nav_video_filter"]}:**
        - {texts["video_subtitle"]}
        - {texts["video_info1"]}
        - {texts["video_info2"]}
        """)

if __name__ == "__main__":
    main()