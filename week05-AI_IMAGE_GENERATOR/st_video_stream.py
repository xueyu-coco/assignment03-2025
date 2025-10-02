import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np
from PIL import Image, ImageDraw
import io
import base64
import os

# Load custom image from file
def load_custom_image(image_path, size=(100, 100)):
    """Load and process custom image for overlay"""
    try:
        if os.path.exists(image_path):
            # Load image
            img = Image.open(image_path)
            
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Resize to specified size
            img = img.resize(size, Image.Resampling.LANCZOS)
            
            return img
        else:
            st.warning(f"Image file not found: {image_path}")
            # Fallback to generated teddy dog
            return create_teddy_dog_image(size)
    except Exception as e:
        st.error(f"Error loading image: {e}")
        # Fallback to generated teddy dog
        return create_teddy_dog_image(size)

# 创建虚拟泰迪狗图像 (fallback function)
def create_teddy_dog_image(size=(100, 100)):
    """Create a simple teddy dog avatar"""
    # Create an RGBA image (with transparency)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Dog head (brown circle)
    head_size = min(size) * 0.8
    head_x = size[0] // 2
    head_y = size[1] // 2
    head_radius = head_size // 2
    
    # Draw head
    draw.ellipse([
        head_x - head_radius, head_y - head_radius,
        head_x + head_radius, head_y + head_radius
    ], fill=(139, 90, 43, 255))  # Brown color
    
    # Draw ears
    ear_size = head_radius * 0.4
    # Left ear
    draw.ellipse([
        head_x - head_radius * 0.8 - ear_size//2, head_y - head_radius * 0.8 - ear_size//2,
        head_x - head_radius * 0.8 + ear_size//2, head_y - head_radius * 0.8 + ear_size//2
    ], fill=(101, 67, 33, 255))  # Dark brown
    # Right ear
    draw.ellipse([
        head_x + head_radius * 0.8 - ear_size//2, head_y - head_radius * 0.8 - ear_size//2,
        head_x + head_radius * 0.8 + ear_size//2, head_y - head_radius * 0.8 + ear_size//2
    ], fill=(101, 67, 33, 255))
    
    # Draw eyes
    eye_size = head_radius * 0.15
    # Left eye
    draw.ellipse([
        head_x - head_radius * 0.3 - eye_size, head_y - head_radius * 0.2 - eye_size,
        head_x - head_radius * 0.3 + eye_size, head_y - head_radius * 0.2 + eye_size
    ], fill=(0, 0, 0, 255))  # Black
    # Right eye
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

# Global variable to store custom image
custom_image_path = r"C:\Users\lxy\Desktop\1624425308015_5589c28e_29447(1).png"
overlay_img = load_custom_image(custom_image_path)
overlay_array = np.array(overlay_img)

def overlay_custom_image(img, x, y, scale=1.0):
    """Overlay custom image at specified position"""
    # Resize custom image
    img_height, img_width = overlay_array.shape[:2]
    new_height = int(img_height * scale)
    new_width = int(img_width * scale)
    
    if new_height <= 0 or new_width <= 0:
        return img
    
    # Resize image
    resized_img = cv2.resize(overlay_array, (new_width, new_height))
    
    # Ensure coordinates are within image bounds
    y1 = max(0, y - new_height // 2)
    y2 = min(img.shape[0], y1 + new_height)
    x1 = max(0, x - new_width // 2)
    x2 = min(img.shape[1], x1 + new_width)
    
    # Adjust custom image to match actual overlay area
    actual_height = y2 - y1
    actual_width = x2 - x1
    
    if actual_height <= 0 or actual_width <= 0:
        return img
    
    img_roi = resized_img[:actual_height, :actual_width]
    
    # Handle Alpha channel for transparent overlay
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

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    
    # Load OpenCV face detector
    try:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Add custom image at each detected face location
        for (x, y, w, h) in faces:
            # Calculate custom image position and size
            center_x = x + w // 2
            center_y = y + h // 2
            scale = w / 100.0  # Adjust custom image size based on face size
            
            # Overlay custom image
            img = overlay_custom_image(img, center_x, center_y, scale)
            
            # Optional: Draw face rectangle (for debugging)
            # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    except Exception as e:
        # If face detection fails, add a custom image in the center of the screen
        center_x = img.shape[1] // 2
        center_y = img.shape[0] // 2
        img = overlay_custom_image(img, center_x, center_y, 1.5)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")

# Streamlit Application
st.title("🎭 Custom Image Video Filter")
st.markdown("### This app adds your custom image at detected face locations!")

# Add control options
col1, col2 = st.columns(2)

with col1:
    st.info("📹 Once the camera is enabled, the app will automatically detect faces and display your custom image at face locations")

with col2:
    st.info("🎭 If no faces are detected, your custom image will appear in the center of the screen")

# Display current image path
st.sidebar.header("📸 Current Image")
st.sidebar.text(f"Using: {custom_image_path}")
if os.path.exists(custom_image_path):
    st.sidebar.success("✅ Image loaded successfully")
    # Show preview of the image
    preview_img = Image.open(custom_image_path)
    preview_img.thumbnail((150, 150))
    st.sidebar.image(preview_img, caption="Image Preview")
else:
    st.sidebar.error("❌ Image file not found")
    st.sidebar.warning("Using fallback teddy dog image")

# 视频流组件
webrtc_streamer(
    key="custom_image_filter",
    video_frame_callback=video_frame_callback,
    rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)

# Usage instructions
with st.expander("📖 Usage Instructions"):
    st.markdown("""
    ### How to use:
    1. **Click "START" button** to enable the camera
    2. **Allow camera permissions** when the browser requests them
    3. **Face the camera** and the app will automatically detect your face
    4. **Enjoy the custom image filter** - your custom image will appear at your face locations
    
    ### Features:
    - 🔍 **Real-time face detection** - Uses OpenCV to detect faces
    - �️ **Custom image overlay** - Uses your specified image file
    - 📏 **Adaptive sizing** - Image size adjusts based on face size
    - 🎭 **Multi-person support** - Can add images for multiple faces simultaneously
    
    ### Technical details:
    - Uses **WebRTC** technology for low-latency video transmission
    - Uses **OpenCV** for real-time face detection
    - Uses **PIL** to process and overlay custom images
    - Supports transparency overlay effects
    - Automatically handles image format conversion (RGBA)
    
    ### Current Image Path:
    `{}`
    """.format(custom_image_path))
