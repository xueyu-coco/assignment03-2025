import streamlit as st
import torch
from diffusers import AutoPipelineForText2Image, LCMScheduler
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
from PIL import Image, ImageDraw
import io
import base64
import os
import time

# 页面配置
st.set_page_config(
    page_title="AI Creative Studio",
    page_icon="🎨",
    layout="wide"
)

# 初始化session state
if "pipeline" not in st.session_state:
    st.session_state["pipeline"] = None
    st.session_state["pipeline_loaded"] = False

if "generated_images" not in st.session_state:
    st.session_state["generated_images"] = []

if "selected_overlay_image" not in st.session_state:
    st.session_state["selected_overlay_image"] = None

# 主标题
st.title("🎨 AI Creative Studio")
st.markdown("### 集成图片生成与视频合成的创意工具")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 功能选择")
    
    # 功能选择
    feature_mode = st.selectbox(
        "选择功能模式",
        ["🎨 图片生成", "📹 视频滤镜", "🔄 图片+视频合成"]
    )
    
    st.markdown("---")
    
    # GPU状态
    st.subheader("💻 系统状态")
    if torch.cuda.is_available():
        st.success(f"GPU: {torch.cuda.get_device_name(0)}")
        st.info(f"CUDA版本: {torch.version.cuda}")
    else:
        st.warning("使用CPU模式")
    
    st.markdown("---")
    
    # 生成的图片库
    st.subheader("🖼️ 图片库")
    if st.session_state["generated_images"]:
        st.write(f"已生成 {len(st.session_state['generated_images'])} 张图片")
        
        # 显示最近的3张图片缩略图
        for i, img in enumerate(st.session_state["generated_images"][-3:]):
            with st.container():
                st.image(img, caption=f"图片 {len(st.session_state['generated_images'])-2+i}", width=150)
                if st.button(f"用作视频滤镜", key=f"use_img_{i}"):
                    st.session_state["selected_overlay_image"] = img
                    st.success("已选择为视频滤镜图片")
        
        if st.button("🗑️ 清空图片库"):
            st.session_state["generated_images"] = []
            st.rerun()
    else:
        st.info("暂无生成的图片")

# 加载AI模型的函数
@st.cache_resource
def load_image_pipeline():
    """加载图片生成模型"""
    try:
        model = 'lykon/dreamshaper-8-lcm'
        pipe = AutoPipelineForText2Image.from_pretrained(
            model, 
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        pipe.to("cuda" if torch.cuda.is_available() else "cpu")
        pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
        return pipe
    except Exception as e:
        st.error(f"模型加载失败: {e}")
        return None

# 创建默认覆盖图像
def create_default_overlay(size=(100, 100)):
    """创建默认的覆盖图像"""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制一个简单的笑脸
    center = (size[0]//2, size[1]//2)
    radius = min(size) // 3
    
    # 脸部 (黄色圆圈)
    draw.ellipse([
        center[0] - radius, center[1] - radius,
        center[0] + radius, center[1] + radius
    ], fill=(255, 255, 0, 200))
    
    # 眼睛
    eye_size = radius // 4
    draw.ellipse([
        center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
        center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
    ], fill=(0, 0, 0, 255))
    
    draw.ellipse([
        center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
        center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
    ], fill=(0, 0, 0, 255))
    
    # 嘴巴
    mouth_width = radius
    draw.arc([
        center[0] - mouth_width//2, center[1],
        center[0] + mouth_width//2, center[1] + radius//2
    ], start=0, end=180, fill=(0, 0, 0, 255), width=3)
    
    return img

# 图像覆盖函数
def overlay_image_on_frame(frame_img, overlay_img, x, y, scale=1.0):
    """在视频帧上覆盖图像"""
    if overlay_img is None:
        return frame_img
    
    # 转换PIL图像为numpy数组
    if isinstance(overlay_img, Image.Image):
        overlay_array = np.array(overlay_img)
    else:
        overlay_array = overlay_img
    
    # 调整覆盖图像大小
    img_height, img_width = overlay_array.shape[:2]
    new_height = int(img_height * scale)
    new_width = int(img_width * scale)
    
    if new_height <= 0 or new_width <= 0:
        return frame_img
    
    # 缩放图像
    resized_img = cv2.resize(overlay_array, (new_width, new_height))
    
    # 确保坐标在图像边界内
    y1 = max(0, y - new_height // 2)
    y2 = min(frame_img.shape[0], y1 + new_height)
    x1 = max(0, x - new_width // 2)
    x2 = min(frame_img.shape[1], x1 + new_width)
    
    # 调整覆盖区域
    actual_height = y2 - y1
    actual_width = x2 - x1
    
    if actual_height <= 0 or actual_width <= 0:
        return frame_img
    
    img_roi = resized_img[:actual_height, :actual_width]
    
    # 处理透明度
    if img_roi.shape[2] == 4:  # RGBA
        alpha = img_roi[:, :, 3] / 255.0
        for c in range(3):  # BGR
            frame_img[y1:y2, x1:x2, c] = (
                alpha * img_roi[:, :, c] + 
                (1 - alpha) * frame_img[y1:y2, x1:x2, c]
            )
    else:  # RGB
        frame_img[y1:y2, x1:x2] = img_roi[:, :, :3]
    
    return frame_img

# 视频帧处理回调
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # 获取覆盖图像
    overlay_img = st.session_state.get("selected_overlay_image")
    
    if overlay_img is None:
        # 使用默认图像
        overlay_img = create_default_overlay((80, 80))
    
    try:
        # 人脸检测
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # 在每个检测到的人脸位置添加覆盖图像
        for (x, y, w, h) in faces:
            center_x = x + w // 2
            center_y = y + h // 2
            scale = w / 100.0
            
            img = overlay_image_on_frame(img, overlay_img, center_x, center_y, scale)
    
    except Exception as e:
        # 如果人脸检测失败，在屏幕中央添加图像
        center_x = img.shape[1] // 2
        center_y = img.shape[0] // 2
        img = overlay_image_on_frame(img, overlay_img, center_x, center_y, 1.0)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# 主要内容区域
if feature_mode == "🎨 图片生成":
    # 图片生成模式
    st.header("🎨 AI图片生成")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 输入描述")
        
        # 预设提示词
        preset_prompts = {
            "选择预设...": "",
            "可爱动物": "cute fluffy puppy playing in garden, soft lighting, adorable",
            "美丽风景": "beautiful landscape with mountains, lakes, golden hour lighting",
            "科幻场景": "futuristic cityscape with flying cars, neon lights, cyberpunk style",
            "艺术肖像": "portrait of wise wizard, detailed face, magical atmosphere, fantasy art",
            "卡通风格": "cartoon style illustration, colorful, friendly, animated character"
        }
        
        selected_preset = st.selectbox("预设提示词", list(preset_prompts.keys()))
        
        # 主要提示词输入
        if selected_preset != "选择预设...":
            default_prompt = preset_prompts[selected_preset]
        else:
            default_prompt = ""
        
        prompt = st.text_area(
            "图片描述 (Prompt)",
            value=default_prompt,
            height=100,
            help="详细描述你想要生成的图片"
        )
        
        # 生成参数
        col_param1, col_param2 = st.columns(2)
        with col_param1:
            num_steps = st.slider("推理步数", 4, 20, 8)
        with col_param2:
            guidance_scale = st.slider("引导强度", 1.0, 5.0, 2.0, 0.5)
        
        # 生成按钮
        generate_btn = st.button("🎨 生成图片", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("🖼️ 生成结果")
        
        if generate_btn and prompt.strip():
            # 加载模型
            if not st.session_state["pipeline_loaded"]:
                with st.spinner("正在加载AI模型..."):
                    pipeline = load_image_pipeline()
                    if pipeline:
                        st.session_state["pipeline"] = pipeline
                        st.session_state["pipeline_loaded"] = True
                        st.success("模型加载成功！")
                    else:
                        st.error("模型加载失败")
                        st.stop()
            
            # 生成图片
            if st.session_state["pipeline"]:
                with st.spinner("正在生成图片..."):
                    try:
                        start_time = time.time()
                        
                        images = st.session_state["pipeline"](
                            prompt,
                            num_inference_steps=num_steps,
                            guidance_scale=guidance_scale,
                            num_images_per_prompt=1
                        ).images
                        
                        generation_time = time.time() - start_time
                        
                        # 保存到session state
                        for image in images:
                            st.session_state["generated_images"].append(image)
                        
                        # 显示生成的图片
                        for image in images:
                            st.image(image, caption=prompt, use_container_width=True)
                        
                        st.success(f"✅ 生成完成！用时: {generation_time:.2f}秒")
                        
                        # 添加下载按钮
                        img_buffer = io.BytesIO()
                        images[0].save(img_buffer, format='PNG')
                        img_data = img_buffer.getvalue()
                        
                        st.download_button(
                            label="📥 下载图片",
                            data=img_data,
                            file_name=f"ai_generated_{int(time.time())}.png",
                            mime="image/png",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"生成失败: {e}")
        
        elif generate_btn and not prompt.strip():
            st.warning("请输入图片描述")
        
        # 显示最近生成的图片
        if st.session_state["generated_images"]:
            st.markdown("### 最近生成的图片")
            latest_image = st.session_state["generated_images"][-1]
            st.image(latest_image, use_container_width=True)

elif feature_mode == "📹 视频滤镜":
    # 视频滤镜模式
    st.header("📹 实时视频滤镜")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📷 摄像头预览")
        
        # 视频流组件
        webrtc_streamer(
            key="video_filter",
            video_frame_callback=video_frame_callback,
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            }
        )
    
    with col2:
        st.subheader("🎭 滤镜设置")
        
        # 显示当前选择的覆盖图像
        if st.session_state["selected_overlay_image"]:
            st.write("当前滤镜图片:")
            st.image(st.session_state["selected_overlay_image"], width=150)
            
            if st.button("🗑️ 移除滤镜图片"):
                st.session_state["selected_overlay_image"] = None
                st.rerun()
        else:
            st.info("使用默认笑脸滤镜")
            default_img = create_default_overlay((100, 100))
            st.image(default_img, width=150)
        
        st.markdown("### 📖 使用说明")
        st.markdown("""
        1. 点击 **START** 启动摄像头
        2. 允许浏览器访问摄像头权限
        3. 面向摄像头，应用会自动检测人脸
        4. 滤镜图片会覆盖在检测到的人脸位置
        5. 从图片库选择自定义滤镜图片
        """)

else:  # 图片+视频合成模式
    # 合成模式
    st.header("🔄 图片生成 + 视频滤镜合成")
    
    # 上半部分：图片生成
    st.subheader("🎨 第一步：生成滤镜图片")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # 快速生成预设
        quick_prompts = {
            "🐶 卡通狗狗": "cute cartoon dog head, friendly smile, colorful, simple design",
            "🐱 可爱猫咪": "adorable cartoon cat face, big eyes, cute expression, pastel colors",
            "🦄 独角兽": "magical unicorn head, rainbow mane, sparkles, fantasy style",
            "🐻 泰迪熊": "teddy bear face, brown fur, cute button nose, friendly expression",
            "👑 皇冠": "golden crown, jewels, royal, elegant design",
            "🎭 面具": "venetian carnival mask, decorative, colorful patterns"
        }
        
        st.write("快速生成滤镜图片:")
        
        for prompt_name, prompt_text in quick_prompts.items():
            if st.button(prompt_name, use_container_width=True):
                # 加载模型并生成
                if not st.session_state["pipeline_loaded"]:
                    with st.spinner("正在加载AI模型..."):
                        pipeline = load_image_pipeline()
                        if pipeline:
                            st.session_state["pipeline"] = pipeline
                            st.session_state["pipeline_loaded"] = True
                
                if st.session_state["pipeline"]:
                    with st.spinner(f"正在生成{prompt_name}..."):
                        try:
                            images = st.session_state["pipeline"](
                                prompt_text,
                                num_inference_steps=8,
                                guidance_scale=2.0,
                                num_images_per_prompt=1
                            ).images
                            
                            # 保存并选择为滤镜
                            for image in images:
                                st.session_state["generated_images"].append(image)
                                st.session_state["selected_overlay_image"] = image
                            
                            st.success(f"✅ {prompt_name} 生成完成并已设为滤镜！")
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"生成失败: {e}")
    
    with col2:
        # 自定义提示词
        st.write("或输入自定义描述:")
        custom_prompt = st.text_input("图片描述", placeholder="例如: 可爱的小动物头像")
        
        if st.button("🎨 生成自定义滤镜") and custom_prompt.strip():
            # 同样的生成逻辑
            if not st.session_state["pipeline_loaded"]:
                with st.spinner("正在加载AI模型..."):
                    pipeline = load_image_pipeline()
                    if pipeline:
                        st.session_state["pipeline"] = pipeline
                        st.session_state["pipeline_loaded"] = True
            
            if st.session_state["pipeline"]:
                with st.spinner("正在生成图片..."):
                    try:
                        images = st.session_state["pipeline"](
                            custom_prompt,
                            num_inference_steps=8,
                            guidance_scale=2.0,
                            num_images_per_prompt=1
                        ).images
                        
                        for image in images:
                            st.session_state["generated_images"].append(image)
                            st.session_state["selected_overlay_image"] = image
                        
                        st.success("✅ 自定义滤镜生成完成！")
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"生成失败: {e}")
    
    st.markdown("---")
    
    # 下半部分：视频滤镜
    st.subheader("📹 第二步：应用视频滤镜")
    
    col3, col4 = st.columns([2, 1])
    
    with col3:
        # 视频流
        webrtc_streamer(
            key="combined_filter",
            video_frame_callback=video_frame_callback,
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            }
        )
    
    with col4:
        st.write("当前滤镜:")
        if st.session_state["selected_overlay_image"]:
            st.image(st.session_state["selected_overlay_image"], width=150)
            st.success("✅ 使用AI生成的滤镜图片")
        else:
            default_img = create_default_overlay((100, 100))
            st.image(default_img, width=150)
            st.info("使用默认滤镜")

# 页脚
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
<p>🎨 AI Creative Studio | 图片生成 + 视频滤镜合成工具</p>
<p>使用 Stable Diffusion + OpenCV + WebRTC 技术</p>
</div>
""", unsafe_allow_html=True)