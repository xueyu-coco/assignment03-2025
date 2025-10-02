from PIL import Image
import numpy as np
import os

class ImageProcessor:
    def __init__(self, image_path):
        """初始化图像处理器
        
        Args:
            image_path (str): 图像文件路径
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图像文件不存在: {image_path}")
        
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.data = np.array(self.image)
    
    def get_dimensions(self):
        """获取图像尺寸
        
        Returns:
            tuple: (height, width, channels) 或 (height, width) 对于灰度图像
        """
        return self.data.shape
    
    def convert_to_grayscale(self):
        """转换为灰度图像
        
        Returns:
            PIL.Image: 灰度图像对象
        """
        if len(self.data.shape) == 3:
            # 彩色图像，计算灰度值
            gray_data = np.mean(self.data, axis=2).astype(np.uint8)
        else:
            # 已经是灰度图像
            gray_data = self.data
        
        return Image.fromarray(gray_data, 'L')
    
    def resize_image(self, new_size):
        """调整图像尺寸
        
        Args:
            new_size (tuple): (width, height)
        
        Returns:
            PIL.Image: 调整尺寸后的图像
        """
        return self.image.resize(new_size)
    
    def crop_image(self, box):
        """裁剪图像
        
        Args:
            box (tuple): (left, top, right, bottom)
        
        Returns:
            PIL.Image: 裁剪后的图像
        """
        return self.image.crop(box)
    
    def rotate_image(self, angle):
        """旋转图像
        
        Args:
            angle (float): 旋转角度（度）
        
        Returns:
            PIL.Image: 旋转后的图像
        """
        return self.image.rotate(angle, expand=True)
    
    def apply_blur(self, radius=2):
        """应用模糊效果
        
        Args:
            radius (int): 模糊半径
        
        Returns:
            PIL.Image: 模糊后的图像
        """
        from PIL import ImageFilter
        return self.image.filter(ImageFilter.GaussianBlur(radius))
    
    def adjust_brightness(self, factor):
        """调整亮度
        
        Args:
            factor (float): 亮度因子 (0.0-2.0, 1.0为原始亮度)
        
        Returns:
            PIL.Image: 调整亮度后的图像
        """
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(factor)
    
    def save_processed_image(self, image, output_path):
        """保存处理后的图像
        
        Args:
            image (PIL.Image): 要保存的图像
            output_path (str): 输出文件路径
        """
        image.save(output_path)
        print(f"图像已保存到: {output_path}")

# 示例使用代码
if __name__ == "__main__":
    # 检查是否有现有的图像文件可以测试
    test_images = ["random_image.png", "1_random_image.png", "test_image.png"]
    image_path = None
    
    for img in test_images:
        if os.path.exists(img):
            image_path = img
            break
    
    if image_path is None:
        print("没有找到测试图像，先创建一个随机图像...")
        # 创建一个测试图像
        from PIL import Image
        import numpy as np
        
        # 创建随机图像
        data = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
        test_img = Image.fromarray(data, 'RGB')
        image_path = "test_image.png"
        test_img.save(image_path)
        print(f"测试图像已创建: {image_path}")
    
    # 使用ImageProcessor处理图像
    try:
        processor = ImageProcessor(image_path)
        
        print(f"原始图像尺寸: {processor.get_dimensions()}")
        
        # 转换为灰度图像
        gray_image = processor.convert_to_grayscale()
        processor.save_processed_image(gray_image, "gray_output.png")
        
        # 调整尺寸
        resized_image = processor.resize_image((200, 200))
        processor.save_processed_image(resized_image, "resized_output.png")
        
        # 调整亮度
        bright_image = processor.adjust_brightness(1.5)
        processor.save_processed_image(bright_image, "bright_output.png")
        
        # 应用模糊
        blurred_image = processor.apply_blur(3)
        processor.save_processed_image(blurred_image, "blurred_output.png")
        
        print("图像处理完成！")
        
    except Exception as e:
        print(f"处理图像时出错: {e}")