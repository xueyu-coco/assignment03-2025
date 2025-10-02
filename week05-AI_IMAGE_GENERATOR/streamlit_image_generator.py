import streamlit as st
from diffusers import DiffusionPipeline
import torch
from PIL import Image
import io
import time

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
            st.success("✅ GPU acceleration enabled")
        else:
            st.warning("⚠️ Using CPU mode, generation will be slower")
        return pipe
    except Exception as e:
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
        st.error(f"Image generation failed: {e}")
        return None

def main():
    # Title and description
    st.title("🎨 AI Image Generator")
    st.markdown("### Transform text descriptions into beautiful images using Stable Diffusion")
    
    # Sidebar settings
    with st.sidebar:
        st.header("⚙️ Generation Settings")
        
        # Preset prompts
        preset_prompts = {
            "Select preset...": "",
            "Beautiful Landscape": "a beautiful landscape with mountains, lakes, and trees, golden hour lighting",
            "Cute Animal": "a cute fluffy kitten playing in a garden, soft lighting, adorable",
            "Sci-fi Scene": "futuristic cityscape with flying cars, neon lights, cyberpunk style",
            "Art Portrait": "portrait of a person, artistic style, detailed, professional lighting",
            "Cartoon Style": "cartoon style illustration, colorful, friendly, animated character"
        }
        
        selected_preset = st.selectbox("Choose preset prompt:", list(preset_prompts.keys()))
        
        # Advanced settings
        st.subheader("🔧 Advanced Settings")
        steps = st.slider("Generation steps", min_value=10, max_value=50, value=20, 
                         help="More steps usually produce better quality but take longer")
        guidance_scale = st.slider("Guidance scale", min_value=1.0, max_value=20.0, value=7.5, step=0.5,
                                 help="Controls how closely AI follows the prompt")
        
        # GPU status display
        st.subheader("💻 System Status")
        if torch.cuda.is_available():
            st.success(f"GPU: {torch.cuda.get_device_name(0)}")
            st.info(f"CUDA Version: {torch.version.cuda}")
        else:
            st.warning("GPU unavailable, using CPU")
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Input Description")
        
        # Main prompt
        if selected_preset != "Select preset...":
            default_prompt = preset_prompts[selected_preset]
        else:
            default_prompt = "a beautiful landscape with mountains"
            
        prompt = st.text_area(
            "Image description (prompt):", 
            value=default_prompt,
            height=100,
            help="Describe in detail what image you want to generate, including style, colors, composition, etc."
        )
        
        # Negative prompt
        negative_prompt = st.text_area(
            "Negative prompt (content to avoid):",
            value="blurry, low quality, distorted, ugly",
            height=60,
            help="Describe what you don't want to appear in the image"
        )
        
        # Generate button
        generate_button = st.button("🎨 Generate Image", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("🖼️ Generation Result")
        
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
            
            status_text.text("Generating image...")
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
                    info_placeholder.info(f"✅ Generation complete! Time: {generation_time:.2f}s")
                    
                    # Prepare download
                    img_buffer = io.BytesIO()
                    image.save(img_buffer, format='PNG')
                    img_data = img_buffer.getvalue()
                    
                    # Download button
                    download_placeholder.download_button(
                        label="📥 Download Image",
                        data=img_data,
                        file_name=f"ai_generated_{int(time.time())}.png",
                        mime="image/png",
                        use_container_width=True
                    )
            
            # Clear progress display
            progress_bar.empty()
            status_text.empty()
    
    elif generate_button and not prompt.strip():
        st.warning("⚠️ Please enter an image description")
    
    # Usage instructions
    with st.expander("📖 Usage Instructions"):
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
    
    # Example gallery
    with st.expander("🖼️ Example Gallery"):
        st.markdown("Here are some example prompts for generation:")
        
        example_cols = st.columns(3)
        examples = [
            ("Landscape", "sunset over mountains, golden hour, peaceful lake reflection"),
            ("Animal", "cute red panda eating bamboo, soft fur, adorable eyes"),
            ("Art", "abstract art, colorful geometric shapes, modern style")
        ]
        
        for i, (title, example_prompt) in enumerate(examples):
            with example_cols[i]:
                st.markdown(f"**{title}**")
                st.code(example_prompt, language=None)

if __name__ == "__main__":
    main()