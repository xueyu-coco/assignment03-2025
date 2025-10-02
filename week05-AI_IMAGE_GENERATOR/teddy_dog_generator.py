from diffusers import DiffusionPipeline
import torch
from PIL import Image
import os
from datetime import datetime

class TeddyDogGenerator:
    def __init__(self):
        """初始化泰迪犬生成器"""
        print("正在加载 Stable Diffusion 模型...")
        self.pipe = DiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        
        if torch.cuda.is_available():
            self.pipe = self.pipe.to("cuda")
            print("✅ GPU 加速已启用")
        else:
            print("⚠️ 使用 CPU 模式")
        
        print("🐕 TeddyDogGenerator 初始化完成！")
    
    def generate_teddy_dog(self, description="", steps=20, guidance_scale=7.5):
        """生成泰迪犬图像
        
        Args:
            description (str): 泰迪犬的描述
            steps (int): 推理步数
            guidance_scale (float): 引导强度
        
        Returns:
            PIL.Image: 生成的泰迪犬图像
        """
        # 基础提示词 - 专门针对泰迪犬
        base_prompt = "a cute teddy dog, poodle, fluffy curly fur, adorable face, high quality, detailed, soft lighting, photorealistic"
        
        # 组合用户描述
        if description:
            full_prompt = f"{base_prompt}, {description}"
        else:
            full_prompt = base_prompt
        
        print(f"🎨 正在生成泰迪犬: {description if description else '基础泰迪犬'}")
        
        # 生成图像
        with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
            image = self.pipe(
                full_prompt, 
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                negative_prompt="blurry, low quality, distorted, ugly, cartoon"
            ).images[0]
        
        return image
    
    def generate_teddy_dog_variations(self, base_description="", variations=None, steps=20):
        """生成不同变化的泰迪犬
        
        Args:
            base_description (str): 基础描述
            variations (list): 变化列表
            steps (int): 推理步数
        
        Returns:
            list: 生成的图像列表
        """
        if variations is None:
            variations = [
                "brown curly fur, sitting pose",
                "white fluffy coat, playing with toy",
                "black and brown fur, wearing collar",
                "cream colored fur, professional grooming",
                "small size, wearing cute outfit"
            ]
        
        images = []
        for i, variation in enumerate(variations):
            print(f"🐕 生成第 {i+1}/{len(variations)} 只泰迪犬...")
            full_desc = f"{base_description}, {variation}" if base_description else variation
            image = self.generate_teddy_dog(full_desc, steps)
            images.append(image)
        
        return images
    
    def save_teddy_dog(self, image, description="", custom_name=None):
        """保存泰迪犬图像
        
        Args:
            image (PIL.Image): 要保存的图像
            description (str): 描述（用于文件名）
            custom_name (str): 自定义文件名
        
        Returns:
            str: 保存的文件路径
        """
        if custom_name:
            filename = f"{custom_name}.png"
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            desc_part = description.replace(" ", "_").replace(",", "")[:20] if description else "teddy_dog"
            filename = f"teddy_dog_{desc_part}_{timestamp}.png"
        
        image.save(filename)
        print(f"💾 泰迪犬图像已保存: {filename}")
        return filename
    
    def create_teddy_dog_gallery(self, theme_descriptions=None, save_individual=True):
        """创建泰迪犬画廊
        
        Args:
            theme_descriptions (list): 主题描述列表
            save_individual (bool): 是否保存单独的图像
        
        Returns:
            list: 保存的文件路径列表
        """
        if theme_descriptions is None:
            theme_descriptions = [
                "adorable brown teddy dog with curly fur, sitting in garden",
                "white fluffy teddy dog with blue bow, studio portrait",
                "small cream colored teddy dog playing with ball",
                "black teddy dog with professional grooming, elegant pose"
            ]
        
        print(f"🎨 创建泰迪犬画廊 ({len(theme_descriptions)} 个图像)...")
        
        images = []
        saved_files = []
        
        for i, desc in enumerate(theme_descriptions):
            print(f"🐕 生成第 {i+1}/{len(theme_descriptions)} 只泰迪犬...")
            image = self.generate_teddy_dog(desc)
            images.append(image)
            
            if save_individual:
                filename = self.save_teddy_dog(image, desc, f"gallery_teddy_dog_{i+1}")
                saved_files.append(filename)
        
        print("🖼️ 泰迪犬画廊创建完成！")
        return saved_files, images

# 使用示例和演示
if __name__ == "__main__":
    print("=== 🐕 泰迪犬生成器演示 ===\n")
    
    # 创建生成器
    generator = TeddyDogGenerator()
    
    # 单个泰迪犬生成示例
    print("\n1. 生成基础泰迪犬")
    basic_teddy_dog = generator.generate_teddy_dog()
    generator.save_teddy_dog(basic_teddy_dog, custom_name="basic_teddy_dog")
    basic_teddy_dog.show()
    
    print("\n2. 生成特定描述的泰迪犬")
    brown_teddy_dog = generator.generate_teddy_dog("brown curly fur, sitting on grass, happy expression")
    generator.save_teddy_dog(brown_teddy_dog, "brown curly fur, sitting on grass")
    brown_teddy_dog.show()
    
    print("\n3. 生成泰迪犬变化系列")
    variations = [
        "white fluffy teddy dog with pink bow",
        "cream colored teddy dog playing fetch",
        "small black teddy dog wearing sweater"
    ]
    
    variation_images = generator.generate_teddy_dog_variations("cute pose", variations)
    
    # 保存变化系列
    for i, (img, desc) in enumerate(zip(variation_images, variations)):
        generator.save_teddy_dog(img, desc, f"variation_teddy_dog_{i+1}")
        img.show()
    
    print("\n4. 生成泰迪犬画廊")
    gallery_files, gallery_images = generator.create_teddy_dog_gallery()
    
    # 显示画廊图片
    for img in gallery_images:
        img.show()
    
    print(f"\n🎉 演示完成！总共生成了 {2 + len(variations) + len(gallery_files)} 只泰迪犬")
    print("\n💡 提示：泰迪犬是贵宾犬的一种美容造型，以其可爱的圆形外观而得名！")