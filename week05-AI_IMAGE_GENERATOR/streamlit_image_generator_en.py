import streamlit as st
from diffusers import DiffusionPipeline
import torch
from PIL import Image
import io
import time

# Language configurations
LANGUAGES = {
    "English": {
        "page_title": "AI Image Generator",
        "page_header": "🎨 AI Image Generator",
        "page_subtitle": "### Transform text descriptions into beautiful images using Stable Diffusion",
        "sidebar_settings": "⚙️ Generation Settings",
        "sidebar_language": "🌍 Language",
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
        "default_prompt": "a beautiful landscape with mountains"
    },
    "中文": {
        "page_title": "AI图像生成器",
        "page_header": "🎨 AI图像生成器",
        "page_subtitle": "### 使用Stable Diffusion将文本描述转换为精美图像",
        "sidebar_settings": "⚙️ 生成设置",
        "sidebar_language": "🌍 语言",
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
        "default_prompt": "美丽的山峰风景"
    },
    "粤语": {
        "page_title": "AI圖像生成器",
        "page_header": "🎨 AI圖像生成器",
        "page_subtitle": "### 用Stable Diffusion將文字描述變成靚靚嘅圖像",
        "sidebar_settings": "⚙️ 生成設定",
        "sidebar_language": "🌍 語言",
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
        "default_prompt": "靚靚嘅山峰風景"
    }
}

# Page configuration
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

# Initialize model
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
            # Get current language for success message
            if 'language' in st.session_state:
                texts = LANGUAGES[st.session_state.language]
                st.success(texts["gpu_enabled"])
            else:
                st.success("✅ GPU acceleration enabled")
        else:
            # Get current language for warning message
            if 'language' in st.session_state:
                texts = LANGUAGES[st.session_state.language]
                st.warning(texts["gpu_warning"])
            else:
                st.warning("⚠️ Using CPU mode, generation will be slower")
        return pipe
    except Exception as e:
        # Get current language for error message
        if 'language' in st.session_state:
            texts = LANGUAGES[st.session_state.language]
            st.error(f"{texts['model_error']}{e}")
        else:
            st.error(f"Model loading failed: {e}")
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
        # Get current language for error message
        if 'language' in st.session_state:
            texts = LANGUAGES[st.session_state.language]
            st.error(f"{texts['generation_error']}{e}")
        else:
            st.error(f"Image generation failed: {e}")
        return None

def main():
    # Initialize session state for language
    if 'language' not in st.session_state:
        st.session_state.language = "English"
    
    # Get current language texts
    texts = LANGUAGES[st.session_state.language]
    
    # Title and description
    st.title(texts["page_header"])
    st.markdown(texts["page_subtitle"])
    
    # Sidebar settings
    with st.sidebar:
        # Language selector at the top
        st.header(texts["sidebar_language"])
        language = st.selectbox(
            "Select Language / 选择语言 / 揀語言:",
            ["English", "中文", "粤语"],
            index=["English", "中文", "粤语"].index(st.session_state.language)
        )
        
        # Update session state if language changed
        if language != st.session_state.language:
            st.session_state.language = language
            st.rerun()
        
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
                time.sleep(0.1)  # Not needed during actual generation
            
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
    
    # Usage instructions and examples (only show in expanded form for better UX)
    add_usage_instructions(texts)
    add_example_gallery(texts)

def add_usage_instructions(texts):
    """Add usage instructions section"""
    with st.expander(texts["usage_instructions"]):
        if texts == LANGUAGES["English"]:
            st.markdown("""
            ### How to use:
            1. **Enter description**: Describe the image you want in detail in the text box
            2. **Choose settings**: Adjust generation steps and guidance scale (optional)
            3. **Generate image**: Click the generate button and wait for AI to create the image
            4. **Download & save**: Download the image if you're satisfied with the result
            
            ### Prompt tips:
            - Use specific descriptive words, like "blue" instead of "nice color"
            - You can specify art styles, like "oil painting style", "cartoon style"
            - Add quality words, like "high quality", "detailed", "professional"
            - Describe lighting, like "soft lighting", "golden hour"
            
            ### Negative prompts:
            - Used to avoid unwanted content, like "blurry", "low quality"
            - Can avoid specific objects or styles
            """)
        elif texts == LANGUAGES["中文"]:
            st.markdown("""
            ### 使用方法：
            1. **输入描述**：在文本框中详细描述你想要的图像
            2. **选择设置**：调整生成步数和引导比例（可选）
            3. **生成图像**：点击生成按钮，等待AI创建图像
            4. **下载保存**：如果满意结果，可以下载图像
            
            ### 提示词技巧：
            - 使用具体的描述词，比如"蓝色"而不是"好看的颜色"
            - 可以指定艺术风格，如"油画风格"、"卡通风格"
            - 添加质量词，如"高质量"、"详细"、"专业"
            - 描述光照，如"柔和光线"、"黄金时光"
            
            ### 负面提示词：
            - 用于避免不想要的内容，如"模糊"、"低质量"
            - 可以避免特定对象或风格
            """)
        else:  # 粤语
            st.markdown("""
            ### 使用方法：
            1. **輸入描述**：喺文本框入面詳細描述你想要嘅圖像
            2. **揀設定**：調整生成步數同引導比例（可選）
            3. **生成圖像**：㩒生成按鈕，等AI整圖像
            4. **下載保存**：如果滿意結果，可以下載圖像
            
            ### 提示詞技巧：
            - 用具體嘅描述詞，比如"藍色"而唔係"靚嘅顏色"
            - 可以指定藝術風格，如"油畫風格"、"卡通風格"
            - 加質量詞，如"高質量"、"詳細"、"專業"
            - 描述光照，如"柔和光線"、"黃金時光"
            
            ### 負面提示詞：
            - 用嚟避免唔想要嘅內容，如"模糊"、"低質量"
            - 可以避免特定對象或風格
            """)

def add_example_gallery(texts):
    """Add example gallery section"""
    with st.expander(texts["example_gallery"]):
        if texts == LANGUAGES["English"]:
            st.markdown("Here are some example prompts for generation:")
            example_cols = st.columns(3)
            examples = [
                ("Landscape", "sunset over mountains, golden hour, peaceful lake reflection"),
                ("Animal", "cute red panda eating bamboo, soft fur, adorable eyes"),
                ("Art", "abstract art, colorful geometric shapes, modern style")
            ]
        elif texts == LANGUAGES["中文"]:
            st.markdown("这里是一些生成示例提示词：")
            example_cols = st.columns(3)
            examples = [
                ("风景", "山峰上的日落，黄金时光，宁静的湖面倒影"),
                ("动物", "可爱的小熊猫吃竹子，柔软的毛发，adorable眼睛"),
                ("艺术", "抽象艺术，彩色几何形状，现代风格")
            ]
        else:  # 粤语
            st.markdown("呢度係一啲生成示例提示詞：")
            example_cols = st.columns(3)
            examples = [
                ("風景", "山峰上嘅日落，黃金時光，寧靜嘅湖面倒影"),
                ("動物", "可愛嘅小熊貓食竹子，柔軟嘅毛髮，adorable眼睛"),
                ("藝術", "抽象藝術，彩色幾何形狀，現代風格")
            ]
        
        for i, (title, example_prompt) in enumerate(examples):
            with example_cols[i]:
                st.markdown(f"**{title}**")
                st.code(example_prompt, language=None)

if __name__ == "__main__":
    main()