import streamlit as st
from PIL import Image, ImageDraw
import io
import time
import os

# Page Configuration
st.set_page_config(
    page_title="AI Creative Studio",
    page_icon="🎨",
    layout="wide"
)

# Initialize session state
if "generated_images" not in st.session_state:
    st.session_state["generated_images"] = []

if "selected_overlay_image" not in st.session_state:
    st.session_state["selected_overlay_image"] = None

# Main Title
st.title("🎨 AI Creative Studio")
st.markdown("### Integrated Image Generation & Video Composition Creative Tool")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Feature Selection")
    
    # Feature mode selection
    feature_mode = st.selectbox(
        "Choose Feature Mode",
        ["🎨 Image Gallery", "📹 Video Filter Demo", "🔄 Creative Composition Workflow"]
    )
    
    st.markdown("---")
    
    # System status (demo version)
    st.subheader("💻 System Status")
    st.success("Demo Mode Running")
    st.info("Full AI features require GPU support")
    
    st.markdown("---")
    
    # Project information
    st.subheader("📋 Project Features")
    st.markdown("""
    **🎨 Image Generation Features:**
    - Stable Diffusion AI model
    - LCM fast generation
    - Custom prompts
    - Multiple preset templates
    
    **📹 Video Processing Features:**
    - Real-time face detection
    - Image filter overlay
    - WebRTC video streaming
    - Custom filter images
    
    **🔄 Composition Workflow:**
    - AI-generated images as filters
    - Real-time video application
    - Seamless integration experience
    """)

# Create demo image function
def create_demo_image(prompt, size=(512, 512)):
    """Create demo image"""
    img = Image.new('RGB', size, (135, 206, 235))  # Sky blue background
    draw = ImageDraw.Draw(img)
    
    # Draw different patterns based on prompt
    if "dog" in prompt.lower():
        # Draw cartoon dog
        center = (size[0]//2, size[1]//2)
        # Head
        draw.ellipse([center[0]-80, center[1]-80, center[0]+80, center[1]+80], fill=(139, 90, 43))
        # Ears
        draw.ellipse([center[0]-120, center[1]-100, center[0]-60, center[1]-40], fill=(101, 67, 33))
        draw.ellipse([center[0]+60, center[1]-100, center[0]+120, center[1]-40], fill=(101, 67, 33))
        # Eyes
        draw.ellipse([center[0]-30, center[1]-30, center[0]-10, center[1]-10], fill=(0, 0, 0))
        draw.ellipse([center[0]+10, center[1]-30, center[0]+30, center[1]-10], fill=(0, 0, 0))
        # Nose
        draw.ellipse([center[0]-8, center[1], center[0]+8, center[1]+16], fill=(0, 0, 0))
        
    elif "cat" in prompt.lower():
        # Draw cartoon cat
        center = (size[0]//2, size[1]//2)
        # Head
        draw.ellipse([center[0]-70, center[1]-70, center[0]+70, center[1]+70], fill=(255, 140, 0))
        # Ears (triangles)
        draw.polygon([center[0]-50, center[1]-70, center[0]-80, center[1]-120, center[0]-20, center[1]-120], fill=(255, 140, 0))
        draw.polygon([center[0]+20, center[1]-120, center[0]+80, center[1]-120, center[0]+50, center[1]-70], fill=(255, 140, 0))
        # Eyes
        draw.ellipse([center[0]-25, center[1]-25, center[0]-5, center[1]-5], fill=(0, 255, 0))
        draw.ellipse([center[0]+5, center[1]-25, center[0]+25, center[1]-5], fill=(0, 255, 0))
        
    elif "bear" in prompt.lower():
        # Draw teddy bear
        center = (size[0]//2, size[1]//2)
        # Head
        draw.ellipse([center[0]-90, center[1]-90, center[0]+90, center[1]+90], fill=(160, 82, 45))
        # Ears
        draw.ellipse([center[0]-110, center[1]-110, center[0]-50, center[1]-50], fill=(139, 69, 19))
        draw.ellipse([center[0]+50, center[1]-110, center[0]+110, center[1]-50], fill=(139, 69, 19))
        # Eyes
        draw.ellipse([center[0]-30, center[1]-30, center[0]-10, center[1]-10], fill=(0, 0, 0))
        draw.ellipse([center[0]+10, center[1]-30, center[0]+30, center[1]-10], fill=(0, 0, 0))
        
    else:
        # Default pattern
        center = (size[0]//2, size[1]//2)
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
        for i in range(5):
            radius = 40 + i * 20
            color = colors[i % len(colors)]
            draw.ellipse([center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius], outline=color, width=5)
    
    # Add text
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = None
    
    text = f"Generated: {prompt[:30]}..."
    draw.text((10, size[1]-40), text, fill=(255, 255, 255), font=font)
    
    return img

# Create default filter image
def create_filter_overlay(size=(100, 100)):
    """Create filter overlay image"""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center = (size[0]//2, size[1]//2)
    radius = min(size) // 3
    
    # Yellow smiley face
    draw.ellipse([
        center[0] - radius, center[1] - radius,
        center[0] + radius, center[1] + radius
    ], fill=(255, 255, 0, 200))
    
    # Eyes
    eye_size = radius // 4
    draw.ellipse([
        center[0] - radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
        center[0] - radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
    ], fill=(0, 0, 0, 255))
    
    draw.ellipse([
        center[0] + radius//2 - eye_size//2, center[1] - radius//3 - eye_size//2,
        center[0] + radius//2 + eye_size//2, center[1] - radius//3 + eye_size//2
    ], fill=(0, 0, 0, 255))
    
    # Smile
    mouth_width = radius
    draw.arc([
        center[0] - mouth_width//2, center[1],
        center[0] + mouth_width//2, center[1] + radius//2
    ], start=0, end=180, fill=(0, 0, 0, 255), width=3)
    
    return img

# Main content area
if feature_mode == "🎨 Image Gallery":
    # Image generation demo mode
    st.header("🎨 AI Image Generation Demo")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Input Description")
        
        # Preset prompts
        preset_prompts = {
            "Select preset...": "",
            "Cute puppy": "cute cartoon dog with big eyes",
            "Orange tabby cat": "orange tabby cat with green eyes",
            "Brown teddy bear": "brown teddy bear with friendly face",
            "Colorful pattern": "colorful abstract pattern with circles",
            "Natural landscape": "beautiful mountain landscape at sunset"
        }
        
        selected_preset = st.selectbox("Preset prompts", list(preset_prompts.keys()))
        
        if selected_preset != "Select preset...":
            default_prompt = preset_prompts[selected_preset]
        else:
            default_prompt = ""
        
        prompt = st.text_area(
            "Image description",
            value=default_prompt,
            height=100,
            help="Describe the image you want to generate"
        )
        
        # Generate button
        generate_btn = st.button("🎨 Generate Demo Image", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("🖼️ Generation Result")
        
        if generate_btn and prompt.strip():
            with st.spinner("Generating demo image..."):
                # Simulate generation time
                time.sleep(2)
                
                # Create demo image
                demo_image = create_demo_image(prompt)
                st.session_state["generated_images"].append(demo_image)
                
                # Display image
                st.image(demo_image, caption=prompt, use_container_width=True)
                st.success("✅ Demo image generated successfully!")
                
                # Download button
                img_buffer = io.BytesIO()
                demo_image.save(img_buffer, format='PNG')
                img_data = img_buffer.getvalue()
                
                st.download_button(
                    label="📥 Download Image",
                    data=img_data,
                    file_name=f"demo_generated_{int(time.time())}.png",
                    mime="image/png",
                    use_container_width=True
                )
        
        elif generate_btn and not prompt.strip():
            st.warning("Please enter an image description")

elif feature_mode == "📹 Video Filter Demo":
    # Video filter demo mode
    st.header("📹 Real-time Video Filter Demo")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📷 Camera Filter Preview")
        
        # Display demo information
        st.info("""
        **📹 Real-time Video Filter Features:**
        
        - **Face Detection**: Automatically detect face positions using OpenCV
        - **Image Overlay**: Place filter images at detected face locations
        - **Real-time Processing**: WebRTC technology for low-latency video streaming
        - **Adaptive Scaling**: Filter size automatically adjusts based on face size
        
        Full functionality requires camera permissions and dependency libraries.
        """)
        
        # Simulate video preview
        st.markdown("### 🎭 Filter Effect Preview")
        placeholder_img = Image.new('RGB', (640, 480), (50, 50, 50))
        draw = ImageDraw.Draw(placeholder_img)
        
        # Draw simulated face box
        draw.rectangle([200, 150, 440, 330], outline=(0, 255, 0), width=3)
        draw.text((210, 130), "Detected Face", fill=(0, 255, 0))
        
        # Add filter effect at face position
        filter_overlay = create_filter_overlay((80, 80))
        placeholder_img.paste(filter_overlay, (280, 200), filter_overlay)
        
        st.image(placeholder_img, caption="Filter Effect Demo", use_container_width=True)
    
    with col2:
        st.subheader("🎭 Filter Settings")
        
        # Filter selection
        filter_type = st.selectbox(
            "Select Filter Type",
            ["😊 Default Smiley", "🐶 Cartoon Dog", "🐱 Cute Cat", "👑 Crown", "🎭 Mask"]
        )
        
        # Display corresponding filter image
        if filter_type == "😊 Default Smiley":
            filter_img = create_filter_overlay((100, 100))
        elif filter_type == "🐶 Cartoon Dog":
            filter_img = create_demo_image("cute cartoon dog", (100, 100))
        elif filter_type == "🐱 Cute Cat":
            filter_img = create_demo_image("orange cat", (100, 100))
        else:
            filter_img = create_filter_overlay((100, 100))
        
        st.image(filter_img, caption=f"Current Filter: {filter_type}", width=150)
        
        # Filter parameters
        st.subheader("⚙️ Filter Parameters")
        opacity = st.slider("Opacity", 0.1, 1.0, 0.8, 0.1)
        size_scale = st.slider("Size Scale", 0.5, 2.0, 1.0, 0.1)
        
        st.markdown("### 📱 Technical Features")
        st.markdown("""
        - **Real-time Processing**: 30fps video stream
        - **Low Latency**: WebRTC technology
        - **Auto Detection**: OpenCV face recognition
        - **Multi-person Support**: Process multiple faces simultaneously
        """)

else:  # Creative composition workflow
    # Composition workflow demo mode
    st.header("🔄 Creative Composition Workflow Demo")
    
    # Workflow steps
    st.markdown("### 📋 Complete Workflow Process")
    
    steps_col1, steps_col2, steps_col3 = st.columns(3)
    
    with steps_col1:
        st.markdown("""
        **Step 1: Image Generation 🎨**
        1. Input creative description
        2. AI generates filter image
        3. Automatic optimization and processing
        """)
        
        if st.button("🎨 Start Generating Filter Image"):
            with st.spinner("Generating creative filter..."):
                time.sleep(2)
                demo_filter = create_demo_image("cute cartoon filter", (150, 150))
                st.session_state["selected_overlay_image"] = demo_filter
                st.success("✅ Filter image generated successfully!")
    
    with steps_col2:
        st.markdown("""
        **Step 2: Filter Application 📹**
        1. Start camera
        2. Real-time face detection
        3. Apply AI-generated filter
        """)
        
        if st.button("📹 Start Video Filter"):
            st.info("Camera functionality will be available in the full version")
    
    with steps_col3:
        st.markdown("""
        **Step 3: Effect Display ✨**
        1. Real-time preview effects
        2. Adjust filter parameters
        3. Save best results
        """)
        
        if st.button("✨ View Final Effect"):
            st.balloons()
            st.success("🎉 Creative composition completed!")
    
    st.markdown("---")
    
    # Display current status
    st.subheader("🎯 Current Workflow Status")
    
    status_col1, status_col2 = st.columns(2)
    
    with status_col1:
        st.markdown("**Generated Filter Images:**")
        if st.session_state["selected_overlay_image"]:
            st.image(st.session_state["selected_overlay_image"], width=150)
            st.success("✅ Filter image ready")
        else:
            st.info("No filter image generated yet")
    
    with status_col2:
        st.markdown("**Technical Architecture:**")
        st.markdown("""
        - **AI Models**: Stable Diffusion + LCM
        - **Video Processing**: OpenCV + WebRTC
        - **UI Framework**: Streamlit
        - **Image Processing**: PIL + NumPy
        """)
    
    # Complete functionality description
    with st.expander("🔧 Complete Functionality Description"):
        st.markdown("""
        ### 🎨 AI Image Generation Features
        - **Stable Diffusion**: State-of-the-art text-to-image generation
        - **LCM Scheduler**: Fast generation of high-quality images
        - **Custom Prompts**: Support for detailed creative descriptions
        - **Batch Generation**: Generate multiple variants at once
        
        ### 📹 Real-time Video Processing
        - **WebRTC Technology**: Low-latency video streaming
        - **OpenCV Face Detection**: Precise face position recognition
        - **Real-time Image Composition**: 60fps smooth filter effects
        - **Multi-face Support**: Process multiple people simultaneously
        
        ### 🔄 Workflow Integration
        - **Seamless Connection**: AI generation directly used for video filters
        - **Parameter Sharing**: Generation parameters automatically applied to filters
        - **Real-time Preview**: Instant view of composition effects
        - **One-click Save**: Quick export of final works
        
        ### 🚀 Technical Advantages
        - **GPU Acceleration**: CUDA support for fast processing
        - **Memory Optimization**: Smart caching to save resources
        - **Cross-platform**: Windows, macOS, Linux support
        - **Web Interface**: No installation needed, browser-ready
        """)

# Footer information
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
<p>🎨 AI Creative Studio | Demo Version</p>
<p>Integrated Stable Diffusion + OpenCV + WebRTC Creative Tool</p>
<p>Full functionality requires AI models and camera support</p>
</div>
""", unsafe_allow_html=True)