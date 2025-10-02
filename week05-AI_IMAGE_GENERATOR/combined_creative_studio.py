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
import hashlib
import random
import threading
import pickle

# 全局变量用于视频处理（线程安全）
current_overlay_image = None
overlay_lock = threading.Lock()

# 用文件来传递图片（确保跨线程可访问）
OVERLAY_CACHE_FILE = "temp_overlay.pkl"

def set_overlay_image(image):
    """线程安全的设置overlay图片（使用文件缓存）"""
    global current_overlay_image
    try:
        with overlay_lock:
            current_overlay_image = image
            # 同时保存到文件
            if image is not None:
                with open(OVERLAY_CACHE_FILE, 'wb') as f:
                    pickle.dump(image, f)
                print(f"DEBUG: Set overlay image - SUCCESS, saved to file")
            else:
                if os.path.exists(OVERLAY_CACHE_FILE):
                    os.remove(OVERLAY_CACHE_FILE)
                print(f"DEBUG: Set overlay image - NONE, removed file")
    except Exception as e:
        print(f"DEBUG: Set overlay error: {e}")

def get_overlay_image():
    """线程安全的获取overlay图片（优先从文件读取）"""
    global current_overlay_image
    try:
        # 首先尝试从文件读取
        if os.path.exists(OVERLAY_CACHE_FILE):
            with open(OVERLAY_CACHE_FILE, 'rb') as f:
                image = pickle.load(f)
                print(f"DEBUG: Get overlay image from file - SUCCESS")
                return image
        
        # 如果文件不存在，从内存读取
        with overlay_lock:
            result = current_overlay_image
            print(f"DEBUG: Get overlay image from memory - {result is not None}")
            return result
            
    except Exception as e:
        print(f"DEBUG: Get overlay error: {e}")
        return None

# Page configuration
st.set_page_config(
    page_title="AI Creative Studio",
    page_icon="🎨",
    layout="wide"
)

# Initialize session state
if "pipeline" not in st.session_state:
    st.session_state["pipeline"] = None
    st.session_state["pipeline_loaded"] = False

if "generated_images" not in st.session_state:
    st.session_state["generated_images"] = []

if "selected_overlay_image" not in st.session_state:
    st.session_state["selected_overlay_image"] = None

# Main title
st.title("🎨 AI Creative Studio")
st.markdown("### Integrated Image Generation and Video Composition Creative Tool")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Feature Selection")
    
    # Feature mode selection
    feature_mode = st.selectbox(
        "Select Feature Mode",
        ["🎨 Image Generation", "📹 Video Filter", "🔄 Image+Video Composition"]
    )
    
    st.markdown("---")
    
    # GPU status
    st.subheader("💻 System Status")
    if torch.cuda.is_available():
        st.success(f"GPU: {torch.cuda.get_device_name(0)}")
        st.info(f"CUDA Version: {torch.version.cuda}")
    else:
        st.warning("Using CPU Mode")
    
    st.markdown("---")
    
    # Generated image gallery
    st.subheader("🖼️ Image Gallery")
    if st.session_state["generated_images"]:
        st.write(f"Generated {len(st.session_state['generated_images'])} images")
        
        # Display recent 3 image thumbnails
        for i, img in enumerate(st.session_state["generated_images"][-3:]):
            with st.container():
                st.image(img, caption=f"Image {len(st.session_state['generated_images'])-2+i}", width=150)
                if st.button(f"Use as Video Filter", key=f"use_img_{i}"):
                    st.session_state["selected_overlay_image"] = img
                    # Update global variable for video processing
                    set_overlay_image(img)
                    st.success("Selected as video filter image")
        
        if st.button("🗑️ Clear Image Gallery"):
            st.session_state["generated_images"] = []
            st.rerun()
    else:
        st.info("No generated images yet")

# 加载AI模型的函数
@st.cache_resource
def load_image_pipeline():
    """Load image generation model"""
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

# Create cartoon animal overlay image
def create_cartoon_animal(animal_type, size=(100, 100)):
    """Create cartoon animal image based on animal type"""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center = (size[0]//2, size[1]//2)
    radius = min(size) // 3
    
    if animal_type == "cat":
        # 猫咪
        # 头部 (橙色)
        draw.ellipse([
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ], fill=(255, 140, 0, 220))
        
        # 猫耳朵 (三角形)
        ear_size = radius // 2
        # 左耳
        draw.polygon([
            center[0] - radius//2, center[1] - radius,
            center[0] - radius, center[1] - radius - ear_size,
            center[0], center[1] - radius - ear_size
        ], fill=(255, 140, 0, 220))
        # 右耳
        draw.polygon([
            center[0] + radius//2, center[1] - radius,
            center[0] + radius, center[1] - radius - ear_size,
            center[0], center[1] - radius - ear_size
        ], fill=(255, 140, 0, 220))
        
        # 眼睛 (绿色)
        eye_size = radius // 4
        draw.ellipse([
            center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 255, 0, 255))
        draw.ellipse([
            center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 255, 0, 255))
        
        # 鼻子 (小三角形)
        nose_size = radius // 6
        draw.polygon([
            center[0], center[1] - nose_size//2,
            center[0] - nose_size//2, center[1] + nose_size//2,
            center[0] + nose_size//2, center[1] + nose_size//2
        ], fill=(255, 192, 203, 255))
        
    elif animal_type == "dog":
        # 狗狗
        # 头部 (棕色)
        draw.ellipse([
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ], fill=(139, 90, 43, 220))
        
        # 狗耳朵 (椭圆形下垂)
        ear_width = radius // 2
        ear_height = radius // 1.5
        # 左耳
        draw.ellipse([
            center[0] - radius - ear_width//2, center[1] - radius//2 - ear_height//2,
            center[0] - radius + ear_width//2, center[1] - radius//2 + ear_height//2
        ], fill=(101, 67, 33, 220))
        # 右耳
        draw.ellipse([
            center[0] + radius - ear_width//2, center[1] - radius//2 - ear_height//2,
            center[0] + radius + ear_width//2, center[1] - radius//2 + ear_height//2
        ], fill=(101, 67, 33, 220))
        
        # 眼睛 (黑色)
        eye_size = radius // 4
        draw.ellipse([
            center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 0, 0, 255))
        draw.ellipse([
            center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 0, 0, 255))
        
        # 鼻子 (黑色圆)
        nose_size = radius // 6
        draw.ellipse([
            center[0] - nose_size//2, center[1] - nose_size//2,
            center[0] + nose_size//2, center[1] + nose_size//2
        ], fill=(0, 0, 0, 255))
        
        # 嘴巴
        mouth_width = radius // 2
        draw.arc([
            center[0] - mouth_width//2, center[1] + nose_size,
            center[0] + mouth_width//2, center[1] + radius//2
        ], start=0, end=180, fill=(0, 0, 0, 255), width=2)
        
    elif animal_type == "rabbit":
        # 兔子
        # 头部 (白色)
        draw.ellipse([
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ], fill=(255, 255, 255, 220))
        
        # 兔耳朵 (长椭圆形)
        ear_width = radius // 3
        ear_height = radius
        # 左耳
        draw.ellipse([
            center[0] - radius//2 - ear_width//2, center[1] - radius - ear_height,
            center[0] - radius//2 + ear_width//2, center[1] - radius
        ], fill=(255, 192, 203, 220))
        # 右耳
        draw.ellipse([
            center[0] + radius//2 - ear_width//2, center[1] - radius - ear_height,
            center[0] + radius//2 + ear_width//2, center[1] - radius
        ], fill=(255, 192, 203, 220))
        
        # 眼睛 (红色)
        eye_size = radius // 4
        draw.ellipse([
            center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(255, 0, 0, 255))
        draw.ellipse([
            center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(255, 0, 0, 255))
        
        # 鼻子 (粉色小圆)
        nose_size = radius // 8
        draw.ellipse([
            center[0] - nose_size//2, center[1] - nose_size//2,
            center[0] + nose_size//2, center[1] + nose_size//2
        ], fill=(255, 192, 203, 255))
        
    elif animal_type == "sheep":
        # 羊羊
        # 头部 (白色，带卷毛效果)
        draw.ellipse([
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ], fill=(255, 255, 255, 220))
        
        # 卷毛效果（小圆圈）
        wool_size = radius // 6
        for i in range(8):
            angle = i * 45  # 每45度一个卷毛
            x = center[0] + int((radius - wool_size) * np.cos(np.radians(angle)))
            y = center[1] + int((radius - wool_size) * np.sin(np.radians(angle)))
            draw.ellipse([
                x - wool_size//2, y - wool_size//2,
                x + wool_size//2, y + wool_size//2
            ], fill=(240, 240, 240, 200))
        
        # 眼睛 (黑色)
        eye_size = radius // 4
        draw.ellipse([
            center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 0, 0, 255))
        draw.ellipse([
            center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 0, 0, 255))
        
        # 鼻子 (黑色小圆)
        nose_size = radius // 8
        draw.ellipse([
            center[0] - nose_size//2, center[1] - nose_size//2,
            center[0] + nose_size//2, center[1] + nose_size//2
        ], fill=(0, 0, 0, 255))
    
    else:
        # 默认笑脸
        draw.ellipse([
            center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius
        ], fill=(255, 255, 0, 200))
        
        eye_size = radius // 4
        draw.ellipse([
            center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 0, 0, 255))
        draw.ellipse([
            center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
            center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
        ], fill=(0, 0, 0, 255))
        
        mouth_width = radius
        draw.arc([
            center[0] - mouth_width//2, center[1],
            center[0] + mouth_width//2, center[1] + radius//2
        ], start=0, end=180, fill=(0, 0, 0, 255), width=3)
    
    return img

# Generate animal type based on face position
def get_animal_for_face(face_x, face_y, face_w, face_h):
    """Generate fixed animal type based on face position features"""
    # 使用人脸位置的哈希值来确保同一个位置总是生成相同的动物
    face_id = f"{face_x//20}_{face_y//20}_{face_w//10}_{face_h//10}"
    face_hash = hashlib.md5(face_id.encode()).hexdigest()
    
    # 将哈希值转换为数字并选择动物
    hash_num = int(face_hash[:8], 16)
    animals = ["cat", "dog", "rabbit", "sheep"]
    return animals[hash_num % len(animals)]

# 创建默认覆盖图像（保留原有函数作为备用）
def create_default_overlay(size=(100, 100)):
    """创建默认的覆盖图像"""
    return create_cartoon_animal("default", size)

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

# Video frame processing callback
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    try:
        # 人脸检测
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # 转换为PIL图像进行处理
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        
        # 在每个人脸上添加对应的卡通动物覆盖层
        for (x, y, w, h) in faces:
            # 根据人脸位置获取对应的动物类型
            animal_type = get_animal_for_face(x, y, w, h)
            
            # 创建对应动物的覆盖图像
            overlay_size = (max(w, 80), max(h, 80))
            overlay = create_cartoon_animal(animal_type, overlay_size)
            
            # 计算覆盖位置
            overlay_x = max(0, x + w//2 - overlay_size[0]//2)
            overlay_y = max(0, y + h//2 - overlay_size[1]//2)
            
            # 确保覆盖层不超出图像边界
            if overlay_x + overlay_size[0] > pil_img.width:
                overlay_x = pil_img.width - overlay_size[0]
            if overlay_y + overlay_size[1] > pil_img.height:
                overlay_y = pil_img.height - overlay_size[1]
            
            # 粘贴覆盖层
            pil_img.paste(overlay, (overlay_x, overlay_y), overlay)
        
        # 转换回OpenCV格式
        img_array = np.array(pil_img)
        img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    except Exception as e:
        # 如果人脸检测失败，在屏幕中央添加默认动物图像
        center_x = img.shape[1] // 2
        center_y = img.shape[0] // 2
        
        # 创建默认动物覆盖
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        overlay = create_cartoon_animal("cat", (100, 100))
        
        overlay_x = max(0, center_x - 50)
        overlay_y = max(0, center_y - 50)
        pil_img.paste(overlay, (overlay_x, overlay_y), overlay)
        
        img_array = np.array(pil_img)
        img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# Image+Video composition mode dynamic video processing callback
def combined_video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    try:
        # 获取当前时间用于动态效果
        current_time = time.time()
        
        # 转换为PIL图像进行处理  
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        
        # 获取滤镜图片（使用线程安全方法）
        overlay_img = get_overlay_image()
        
        # 调试信息：在画面上显示状态
        cv2.putText(img, f"Overlay status: {'Found' if overlay_img else 'None'}", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # 只有当用户真正生成了AI图片时才进行处理
        if overlay_img is not None:
            cv2.putText(img, "AI Filter Active", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # 人脸检测
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            cv2.putText(img, f"Faces detected: {len(faces)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            if len(faces) > 0:
                # 在每个人脸上添加动态效果的生成图片
                for (x, y, w, h) in faces:
                    # 绘制人脸检测框（调试用）
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    
                    # 创建动态效果
                    face_center_x = x + w // 2
                    face_center_y = y + h // 2
                    
                    # 动态缩放效果（呼吸效果）
                    scale_factor = 0.7 + 0.3 * abs(np.sin(current_time * 2))  # 0.7-1.0之间变化
                    
                    # 动态位置偏移（轻微摆动）
                    offset_x = int(8 * np.sin(current_time * 3))
                    offset_y = int(4 * np.cos(current_time * 4))
                    
                    # 计算动态尺寸（让图片稍微大于人脸框）
                    face_scale = 1.3  # 图片比人脸大30%
                    base_size = max(w, h) * face_scale
                    dynamic_size = (int(base_size * scale_factor), int(base_size * scale_factor))
                    
                    try:
                        # 转换为PIL进行图片处理
                        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        pil_img = Image.fromarray(img_rgb)
                        
                        # 调整生成图片大小
                        resized_overlay = overlay_img.resize(dynamic_size, Image.Resampling.LANCZOS)
                        
                        # 添加轻微旋转效果
                        rotation_angle = 2 * np.sin(current_time * 1.5)  # -2到2度摆动（减少旋转幅度）
                        if abs(rotation_angle) > 0.3:  # 避免过小的旋转
                            # 创建带alpha通道的图像用于旋转
                            if resized_overlay.mode != 'RGBA':
                                resized_overlay = resized_overlay.convert('RGBA')
                            resized_overlay = resized_overlay.rotate(rotation_angle, expand=True)
                        
                        # 计算粘贴位置（稍微向上偏移，更好地覆盖人脸）
                        paste_x = max(0, face_center_x - resized_overlay.width // 2 + offset_x)
                        paste_y = max(0, face_center_y - resized_overlay.height // 2 - int(h * 0.1) + offset_y)  # 向上偏移10%人脸高度
                        
                        # 确保不超出边界
                        if paste_x + resized_overlay.width > pil_img.width:
                            paste_x = pil_img.width - resized_overlay.width
                        if paste_y + resized_overlay.height > pil_img.height:
                            paste_y = pil_img.height - resized_overlay.height
                        
                        # 确保有alpha通道
                        if resized_overlay.mode != 'RGBA':
                            resized_overlay = resized_overlay.convert('RGBA')
                        
                        # 粘贴到视频帧上
                        pil_img.paste(resized_overlay, (paste_x, paste_y), resized_overlay)
                        
                        # 转换回OpenCV格式
                        img_array = np.array(pil_img)
                        img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                        
                    except Exception as e:
                        cv2.putText(img, f"Paste Error: {str(e)[:30]}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            
            else:
                # 没有检测到人脸时，在屏幕中央显示动态效果
                center_x = img.shape[1] // 2
                center_y = img.shape[0] // 2
                
                try:
                    # 转换为PIL进行处理
                    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    pil_img = Image.fromarray(img_rgb)
                    
                    # 动态效果
                    scale_factor = 0.6 + 0.4 * abs(np.sin(current_time * 1.5))
                    rotation_angle = 8 * np.sin(current_time * 1)
                    
                    # 调整图片
                    dynamic_size = (int(120 * scale_factor), int(120 * scale_factor))
                    resized_overlay = overlay_img.resize(dynamic_size, Image.Resampling.LANCZOS)
                    
                    if abs(rotation_angle) > 0.5:
                        if resized_overlay.mode != 'RGBA':
                            resized_overlay = resized_overlay.convert('RGBA')
                        resized_overlay = resized_overlay.rotate(rotation_angle, expand=True)
                    
                    # 位置
                    paste_x = max(0, center_x - resized_overlay.width // 2)
                    paste_y = max(0, center_y - resized_overlay.height // 2)
                    
                    # 粘贴
                    if resized_overlay.mode != 'RGBA':
                        resized_overlay = resized_overlay.convert('RGBA')
                    pil_img.paste(resized_overlay, (paste_x, paste_y), resized_overlay)
                    
                    # 转换回OpenCV格式
                    img_array = np.array(pil_img)
                    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                    
                except Exception as e:
                    cv2.putText(img, f"Center Error: {str(e)[:30]}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
        else:
            # 没有滤镜图片时，显示提示信息
            cv2.putText(img, "Please generate AI filter first", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    except Exception as e:
        # 错误处理：在图片上显示简单的错误信息
        cv2.putText(img, f"Error: {str(e)[:30]}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# 主要内容区域
if feature_mode == "🎨 Image Generation":
    # Image generation mode
    st.header("🎨 AI Image Generation")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Input Description")
        
        # Preset prompts
        preset_prompts = {
            "Select preset...": "",
            "Cute Animals": "cute fluffy puppy playing in garden, soft lighting, adorable",
            "Beautiful Landscapes": "beautiful landscape with mountains, lakes, golden hour lighting",
            "Sci-fi Scenes": "futuristic cityscape with flying cars, neon lights, cyberpunk style",
            "Art Portraits": "portrait of wise wizard, detailed face, magical atmosphere, fantasy art",
            "Cartoon Style": "cartoon style illustration, colorful, friendly, animated character"
        }
        
        selected_preset = st.selectbox("Preset Prompts", list(preset_prompts.keys()))
        
        # Main prompt input
        if selected_preset != "Select preset...":
            default_prompt = preset_prompts[selected_preset]
        else:
            default_prompt = ""
        
        prompt = st.text_area(
            "Image Description (Prompt)",
            value=default_prompt,
            height=100,
            help="Describe in detail the image you want to generate"
        )
        
        # Generation parameters
        col_param1, col_param2 = st.columns(2)
        with col_param1:
            num_steps = st.slider("Inference Steps", 4, 20, 8)
        with col_param2:
            guidance_scale = st.slider("Guidance Scale", 1.0, 5.0, 2.0, 0.5)
        
        # Generate button
        generate_btn = st.button("🎨 Generate Image", type="primary", width="stretch")
    
    with col2:
        st.subheader("🖼️ Generation Results")
        
        if generate_btn and prompt.strip():
            # Load model
            if not st.session_state["pipeline_loaded"]:
                with st.spinner("Loading AI model..."):
                    pipeline = load_image_pipeline()
                    if pipeline:
                        st.session_state["pipeline"] = pipeline
                        st.session_state["pipeline_loaded"] = True
                        st.success("Model loaded successfully!")
                    else:
                        st.error("Model loading failed")
                        st.stop()
            
            # Generate image
            if st.session_state["pipeline"]:
                with st.spinner("Generating image..."):
                    try:
                        start_time = time.time()
                        
                        images = st.session_state["pipeline"](
                            prompt,
                            num_inference_steps=num_steps,
                            guidance_scale=guidance_scale,
                            num_images_per_prompt=1
                        ).images
                        
                        generation_time = time.time() - start_time
                        
                        # Save to session state
                        for image in images:
                            st.session_state["generated_images"].append(image)
                        
                        # Display generated images
                        for image in images:
                            st.image(image, caption=prompt, use_column_width=True)
                        
                        st.success(f"✅ Generation completed! Time: {generation_time:.2f}s")
                        
                        # Add download button
                        img_buffer = io.BytesIO()
                        images[0].save(img_buffer, format='PNG')
                        img_data = img_buffer.getvalue()
                        
                        st.download_button(
                            label="📥 Download Image",
                            data=img_data,
                            file_name=f"ai_generated_{int(time.time())}.png",
                            mime="image/png",
                            width="stretch"
                        )
                        
                    except Exception as e:
                        st.error(f"Generation failed: {e}")
        
        elif generate_btn and not prompt.strip():
            st.warning("请输入图片描述")
        
        # 显示最近生成的图片
        if st.session_state["generated_images"]:
            st.markdown("### 最近生成的图片")
            latest_image = st.session_state["generated_images"][-1]
            st.image(latest_image, use_container_width=True)

elif feature_mode == "📹 Video Filter":
    # Video filter mode
    st.header("📹 Real-time Video Filter")
    
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

else:  # Image+Video composition mode
    # Composition mode
    st.header("🔄 Image Generation + Video Filter Composition")
    
    # Upper part: Image generation
    st.subheader("🎨 Step 1: Generate Filter Images")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Quick generation presets
        quick_prompts = {
            "🐶 Cartoon Dog": "cute cartoon dog head, friendly smile, colorful, simple design",
            "🐱 Cute Cat": "adorable cartoon cat face, big eyes, cute expression, pastel colors",
            "🦄 Unicorn": "magical unicorn head, rainbow mane, sparkles, fantasy style",
            "🐻 Teddy Bear": "teddy bear face, brown fur, cute button nose, friendly expression",
            "👑 Crown": "golden crown, jewels, royal, elegant design",
            "🎭 Mask": "venetian carnival mask, decorative, colorful patterns",
            "🌸 Flower Decoration": "beautiful flower crown, cherry blossoms, soft colors, transparent background",
            "⭐ Star Halo": "glowing star halo, magical sparkles, golden light, celestial design",
            "🎀 Bow Tie": "cute bow tie, pastel ribbons, kawaii style, soft colors",
            "🎪 Jester Hat": "colorful jester hat, bells, fun carnival style, bright colors"
        }
        
        st.write("Quick Generate Face Filter Images:")
        st.caption("💡 These images will be automatically applied to detected faces")
        
        for prompt_name, prompt_text in quick_prompts.items():
            if st.button(prompt_name, width="stretch"):
                # Load model and generate
                if not st.session_state["pipeline_loaded"]:
                    with st.spinner("Loading AI model..."):
                        pipeline = load_image_pipeline()
                        if pipeline:
                            st.session_state["pipeline"] = pipeline
                            st.session_state["pipeline_loaded"] = True
                
                if st.session_state["pipeline"]:
                    with st.spinner(f"Generating {prompt_name}..."):
                        try:
                            images = st.session_state["pipeline"](
                                prompt_text,
                                num_inference_steps=8,
                                guidance_scale=2.0,
                                num_images_per_prompt=1
                            ).images
                            
                            # Save and select as filter
                            for image in images:
                                st.session_state["generated_images"].append(image)
                                st.session_state["selected_overlay_image"] = image
                                # Update global variable for video processing
                                set_overlay_image(image)
                            
                            st.success(f"✅ {prompt_name} generated and set as filter!")
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"Generation failed: {e}")
    
    with col2:
        # Custom prompts
        st.write("Or enter custom description:")
        st.caption("💡 Recommended keywords: transparent background, face decoration, head accessory")
        custom_prompt = st.text_input("Image Description", placeholder="e.g.: golden halo glowing light transparent background")
        
        if st.button("🎨 Generate Custom Filter") and custom_prompt.strip():
            # Same generation logic
            if not st.session_state["pipeline_loaded"]:
                with st.spinner("Loading AI model..."):
                    pipeline = load_image_pipeline()
                    if pipeline:
                        st.session_state["pipeline"] = pipeline
                        st.session_state["pipeline_loaded"] = True
            
            if st.session_state["pipeline"]:
                with st.spinner("Generating image..."):
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
                            # Update global variable for video processing
                            set_overlay_image(image)
                        
                        st.success("✅ Custom filter generated successfully!")
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"Generation failed: {e}")
    
    st.markdown("---")
    
    # Lower part: Video filter
    st.subheader("📹 Step 2: Apply Video Filter")
    
    col3, col4 = st.columns([2, 1])
    
    with col3:
        # Video stream (using specialized dynamic effects callback)
        webrtc_streamer(
            key="combined_filter",
            video_frame_callback=combined_video_frame_callback,
            rtc_configuration={
                "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
            }
        )
    
    with col4:
        st.write("Current Filter:")
        if st.session_state["selected_overlay_image"]:
            st.image(st.session_state["selected_overlay_image"], width=150)
            st.success("✅ 使用AI生成的滤镜图片")
            
            # 动态效果说明
            st.info("""
            🌟 **AI图片人脸应用已启用！**
            - 🎯 AI图片智能贴合人脸
            - 🔄 动态呼吸缩放效果
            - 🎪 轻微摆动旋转
            - 👤 自动人脸追踪覆盖
            - � 智能尺寸调整（比人脸大30%）
            """)
        else:
            default_img = create_default_overlay((100, 100))
            st.image(default_img, width=150)
            st.info("Please generate filter image first")
            
        # Regenerate button
        if st.button("🔄 Reselect Filter", width="stretch"):
            st.session_state["selected_overlay_image"] = None
            # Reset global variable
            set_overlay_image(None)
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
<p>🎨 AI Creative Studio | Image Generation + Video Filter Composition Tool</p>
<p>Powered by Stable Diffusion + OpenCV + WebRTC Technology</p>
</div>
""", unsafe_allow_html=True)