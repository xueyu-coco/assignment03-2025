from diffusers import DiffusionPipeline
import torch
from PIL import Image
import os
from datetime import datetime

class TeddyGenerator:
    def __init__(self):
        """初始化泰迪熊生成器"""
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
        
        print("🧸 TeddyGenerator 初始化完成！")
    
    def generate_teddy(self, description="", steps=20, guidance_scale=7.5):
        """生成泰迪熊图像
        
        Args:
            description (str): 泰迪熊的描述
            steps (int): 推理步数
            guidance_scale (float): 引导强度
        
        Returns:
            PIL.Image: 生成的泰迪熊图像
        """
        # 基础提示词
        base_prompt = "a cute teddy bear, high quality, detailed, soft lighting"
        
        # 组合用户描述
        if description:
            full_prompt = f"{base_prompt}, {description}"
        else:
            full_prompt = base_prompt
        
        print(f"🎨 正在生成: {full_prompt}")
        
        # 生成图像
        with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
            image = self.pipe(
                full_prompt, 
                num_inference_steps=steps,
                guidance_scale=guidance_scale
            ).images[0]
        
        return image
    
    def generate_multiple_teddies(self, descriptions, steps=20):
        """批量生成多个泰迪熊
        
        Args:
            descriptions (list): 描述列表
            steps (int): 推理步数
        
        Returns:
            list: 生成的图像列表
        """
        images = []
        for i, desc in enumerate(descriptions):
            print(f"🧸 生成第 {i+1}/{len(descriptions)} 个泰迪熊...")
            image = self.generate_teddy(desc, steps)
            images.append(image)
        return images
    
    def save_teddy(self, image, description="", custom_name=None):
        """保存泰迪熊图像
        
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
            # 基于时间和描述生成文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            desc_part = description.replace(" ", "_").replace(",", "")[:20] if description else "teddy"
            filename = f"teddy_{desc_part}_{timestamp}.png"
        
        image.save(filename)
        print(f"💾 泰迪熊图像已保存: {filename}")
        return filename
    
    def create_teddy_gallery(self, descriptions, save_individual=True):
        """创建泰迪熊画廊
        
        Args:
            descriptions (list): 描述列表
            save_individual (bool): 是否保存单独的图像
        
        Returns:
            list: 保存的文件路径列表
        """
        print(f"🎨 创建泰迪熊画廊 ({len(descriptions)} 个图像)...")
        
        images = self.generate_multiple_teddies(descriptions)
        saved_files = []
        
        if save_individual:
            for i, (image, desc) in enumerate(zip(images, descriptions)):
                filename = self.save_teddy(image, desc, f"gallery_teddy_{i+1}")
                saved_files.append(filename)
        
        print("🖼️ 泰迪熊画廊创建完成！")
        return saved_files

# 使用示例和演示
if __name__ == "__main__":
    print("=== 🧸 泰迪熊生成器演示 ===\n")
    
    # 创建生成器
    generator = TeddyGenerator()
    
    # 单个泰迪熊生成示例
    print("\n1. 生成基础泰迪熊")
    basic_teddy = generator.generate_teddy()
    generator.save_teddy(basic_teddy, custom_name="basic_teddy")
    basic_teddy.show()
    
    print("\n2. 生成带描述的泰迪熊")
    brown_teddy = generator.generate_teddy("brown fur, sitting, wearing a red bow tie")
    generator.save_teddy(brown_teddy, "brown fur, sitting, wearing a red bow tie")
    brown_teddy.show()
    
    print("\n3. 生成泰迪熊画廊")
    teddy_descriptions = [
        "white fluffy teddy bear with blue eyes",
        "brown teddy bear holding a heart",
        "small teddy bear wearing a hat",
        "vintage teddy bear with patches"
    ]
    
    gallery_files = generator.create_teddy_gallery(teddy_descriptions)
    
    print(f"\n🎉 演示完成！生成了 {len(gallery_files) + 2} 个泰迪熊图像")
    print("生成的文件:")
    for file in ["basic_teddy.png", "teddy_brown_fur_sitting_wear*.png"] + gallery_files:
        print(f"  - {file}")
    
    print("\n💡 提示：你可以尝试不同的描述来生成各种风格的泰迪熊！")