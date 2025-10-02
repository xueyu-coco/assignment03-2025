from diffusers import DiffusionPipeline
import torch
from PIL import Image
import os
from datetime import datetime

class CartoonDogGenerator:
    def __init__(self):
        """初始化卡通狗狗生成器"""
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
        
        print("🎨 CartoonDogGenerator 初始化完成！")
    
    def generate_cartoon_dog(self, description="", steps=20, guidance_scale=7.5):
        """生成卡通风格狗狗图像
        
        Args:
            description (str): 狗狗的描述
            steps (int): 推理步数
            guidance_scale (float): 引导强度
        
        Returns:
            PIL.Image: 生成的卡通狗狗图像
        """
        # 基础提示词 - 专门针对卡通风格狗狗
        base_prompt = "cartoon style dog, anime style, cute cartoon puppy, animated character, colorful, bright colors, Disney style, kawaii, adorable expression"
        
        # 组合用户描述
        if description:
            full_prompt = f"{base_prompt}, {description}"
        else:
            full_prompt = base_prompt
        
        print(f"🎨 正在生成卡通狗狗: {description if description else '基础卡通狗狗'}")
        
        # 负面提示词，避免现实主义风格
        negative_prompt = "realistic, photorealistic, real photo, dark, scary, ugly, blurry, low quality"
        
        # 生成图像
        with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
            image = self.pipe(
                full_prompt, 
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                negative_prompt=negative_prompt
            ).images[0]
        
        return image
    
    def generate_brown_cartoon_dogs(self, variations=None, steps=20):
        """生成不同姿势的棕色卡通狗狗
        
        Args:
            variations (list): 变化列表
            steps (int): 推理步数
        
        Returns:
            list: 生成的图像列表
        """
        if variations is None:
            variations = [
                "brown cartoon puppy sitting, big eyes, happy smile",
                "brown cartoon dog running, playful expression, tongue out",
                "brown cartoon puppy sleeping, peaceful, curled up",
                "brown cartoon dog playing with ball, excited, jumping",
                "brown cartoon puppy wearing hat, cute accessories"
            ]
        
        images = []
        for i, variation in enumerate(variations):
            print(f"🐕 生成第 {i+1}/{len(variations)} 只棕色卡通狗狗...")
            image = self.generate_cartoon_dog(variation, steps)
            images.append(image)
        
        return images
    
    def generate_cartoon_dog_collection(self, color="brown", styles=None, steps=20):
        """生成不同风格的卡通狗狗合集
        
        Args:
            color (str): 主要颜色
            styles (list): 风格列表
            steps (int): 推理步数
        
        Returns:
            list: 生成的图像列表和描述
        """
        if styles is None:
            styles = [
                f"{color} cartoon puppy, chibi style, super cute",
                f"{color} cartoon dog, Disney animation style, friendly",
                f"{color} cartoon puppy, anime style, big sparkly eyes",
                f"{color} cartoon dog, Pixar style, 3D cartoon look",
                f"{color} cartoon puppy, kawaii style, pastel colors"
            ]
        
        images = []
        descriptions = []
        
        for i, style in enumerate(styles):
            print(f"🎨 生成第 {i+1}/{len(styles)} 种风格的{color}卡通狗狗...")
            image = self.generate_cartoon_dog(style, steps)
            images.append(image)
            descriptions.append(style)
        
        return images, descriptions
    
    def save_cartoon_dog(self, image, description="", custom_name=None):
        """保存卡通狗狗图像
        
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
            desc_part = description.replace(" ", "_").replace(",", "")[:20] if description else "cartoon_dog"
            filename = f"cartoon_dog_{desc_part}_{timestamp}.png"
        
        image.save(filename)
        print(f"💾 卡通狗狗图像已保存: {filename}")
        return filename
    
    def create_brown_cartoon_dog_showcase(self):
        """创建棕色卡通狗狗展示
        
        Returns:
            list: 保存的文件路径列表
        """
        print("🎨 创建棕色卡通狗狗展示...")
        
        # 主要的棕色卡通狗狗
        main_dog = self.generate_cartoon_dog("cute brown cartoon puppy, big eyes, sitting, cartoon animation style, colorful background")
        main_file = self.save_cartoon_dog(main_dog, custom_name="main_brown_cartoon_dog")
        main_dog.show()
        
        # 不同姿势的棕色卡通狗狗
        pose_images = self.generate_brown_cartoon_dogs()
        pose_files = []
        
        for i, img in enumerate(pose_images):
            filename = self.save_cartoon_dog(img, custom_name=f"brown_cartoon_dog_pose_{i+1}")
            pose_files.append(filename)
            img.show()
        
        # 不同风格的棕色卡通狗狗
        style_images, style_descriptions = self.generate_cartoon_dog_collection("brown")
        style_files = []
        
        for i, (img, desc) in enumerate(zip(style_images, style_descriptions)):
            filename = self.save_cartoon_dog(img, desc, f"brown_cartoon_dog_style_{i+1}")
            style_files.append(filename)
            img.show()
        
        all_files = [main_file] + pose_files + style_files
        print(f"✨ 棕色卡通狗狗展示完成！生成了 {len(all_files)} 张图片")
        
        return all_files

# 使用示例和演示
if __name__ == "__main__":
    print("=== 🎨 卡通狗狗生成器演示 ===\n")
    print("专门生成：卡通动画、棕色的、小狗")
    
    # 创建生成器
    generator = CartoonDogGenerator()
    
    # 生成主要的棕色卡通小狗
    print("\n1. 生成主要的棕色卡通小狗")
    main_cartoon_dog = generator.generate_cartoon_dog("cute brown cartoon puppy, big round eyes, happy expression, sitting pose, anime style")
    generator.save_cartoon_dog(main_cartoon_dog, custom_name="main_brown_cartoon_puppy")
    main_cartoon_dog.show()
    
    # 生成不同表情的棕色卡通小狗
    print("\n2. 生成不同表情的棕色卡通小狗")
    expressions = [
        "brown cartoon puppy, happy smile, wagging tail",
        "brown cartoon puppy, sleepy eyes, yawning",
        "brown cartoon puppy, excited expression, jumping"
    ]
    
    expression_images = []
    for i, expr in enumerate(expressions):
        print(f"生成表情 {i+1}: {expr}")
        img = generator.generate_cartoon_dog(expr)
        generator.save_cartoon_dog(img, custom_name=f"brown_cartoon_expression_{i+1}")
        expression_images.append(img)
        img.show()
    
    # 创建完整的棕色卡通狗狗展示
    print("\n3. 创建棕色卡通狗狗完整展示")
    showcase_files = generator.create_brown_cartoon_dog_showcase()
    
    print(f"\n🎉 演示完成！")
    print(f"总共生成了 {1 + len(expressions) + len(showcase_files)} 只卡通风格的棕色小狗")
    print("\n✨ 特色：")
    print("- 🎨 卡通动画风格")
    print("- 🤎 棕色主题")
    print("- 🐕 可爱小狗")
    print("- 😊 多种表情和姿势")
    print("- 🌈 明亮色彩")