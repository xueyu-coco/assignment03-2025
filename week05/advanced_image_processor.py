from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self, image_path):
        """初始化图像处理器"""
        self.image = Image.open(image_path)
        self.data = np.array(self.image)
        self.image_path = image_path
    
    def get_dimensions(self):
        """获取图像尺寸"""
        return self.data.shape
    
    def convert_to_grayscale(self):
        """转换为灰度图像"""
        if len(self.data.shape) == 3:
            gray_data = np.mean(self.data, axis=2).astype(np.uint8)
        else:
            gray_data = self.data
        return Image.fromarray(gray_data, 'L')
    
    def adjust_brightness(self, factor=1.5):
        """调整亮度"""
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(factor)
    
    def adjust_contrast(self, factor=1.5):
        """调整对比度"""
        enhancer = ImageEnhance.Contrast(self.image)
        return enhancer.enhance(factor)
    
    def apply_blur(self, radius=2):
        """应用高斯模糊"""
        return self.image.filter(ImageFilter.GaussianBlur(radius))
    
    def crop_center(self, crop_size):
        """从中心裁剪图像"""
        width, height = self.image.size
        new_width, new_height = crop_size
        
        left = (width - new_width) // 2
        top = (height - new_height) // 2
        right = left + new_width
        bottom = top + new_height
        
        return self.image.crop((left, top, right, bottom))
    
    def create_thumbnail(self, size=(128, 128)):
        """创建缩略图"""
        thumb = self.image.copy()
        thumb.thumbnail(size)
        return thumb
    
    def get_color_histogram(self):
        """获取颜色直方图"""
        if self.image.mode == 'RGB':
            r_hist = np.histogram(self.data[:,:,0], bins=256, range=(0, 256))[0]
            g_hist = np.histogram(self.data[:,:,1], bins=256, range=(0, 256))[0]
            b_hist = np.histogram(self.data[:,:,2], bins=256, range=(0, 256))[0]
            return r_hist, g_hist, b_hist
        else:
            return np.histogram(self.data, bins=256, range=(0, 256))[0]
    
    def show_comparison(self, processed_image, title="图像对比"):
        """显示原始图像和处理后图像的对比"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        ax1.imshow(self.image)
        ax1.set_title('原始图像')
        ax1.axis('off')
        
        ax2.imshow(processed_image)
        ax2.set_title('处理后图像')
        ax2.axis('off')
        
        plt.suptitle(title)
        plt.tight_layout()
        plt.show()

# 使用已有的随机图像进行演示
if __name__ == "__main__":
    # 使用之前生成的随机图像
    image_path = "random_image.png"
    
    print("=== 高级图像处理演示 ===")
    processor = ImageProcessor(image_path)
    
    print(f"原始图像尺寸: {processor.get_dimensions()}")
    
    # 1. 灰度转换
    print("\n1. 转换为灰度图像")
    gray_img = processor.convert_to_grayscale()
    gray_img.save("gray_processed.png")
    print("灰度图像已保存")
    
    # 2. 亮度调整
    print("\n2. 调整亮度")
    bright_img = processor.adjust_brightness(1.8)
    bright_img.save("bright_processed.png")
    print("亮度调整图像已保存")
    
    # 3. 对比度调整
    print("\n3. 调整对比度")
    contrast_img = processor.adjust_contrast(2.0)
    contrast_img.save("contrast_processed.png")
    print("对比度调整图像已保存")
    
    # 4. 模糊效果
    print("\n4. 应用模糊效果")
    blur_img = processor.apply_blur(3)
    blur_img.save("blur_processed.png")
    print("模糊图像已保存")
    
    # 5. 中心裁剪
    print("\n5. 中心裁剪")
    crop_img = processor.crop_center((300, 300))
    crop_img.save("crop_processed.png")
    print("裁剪图像已保存")
    
    # 6. 创建缩略图
    print("\n6. 创建缩略图")
    thumb_img = processor.create_thumbnail((64, 64))
    thumb_img.save("thumbnail_processed.png")
    print("缩略图已保存")
    
    # 7. 显示原始图像
    print("\n7. 显示原始图像")
    processor.image.show()
    
    print("\n所有处理完成！检查生成的文件。")