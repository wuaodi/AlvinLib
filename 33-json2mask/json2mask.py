import os
import json
import numpy as np
from PIL import Image, ImageDraw


# 定义类别到颜色的映射关系
color_map = {
    "solar": (255, 0, 0),  # 红色
    "sensor": (0, 255, 0),  # 绿色
    "nozzle": (0, 0, 255),  # 蓝色
    "cabin": (0, 0, 255)  # 蓝色
}

def convert_json_to_masks(json_folder, output_folder):
    # 遍历文件夹中的JSON文件
    for filename in os.listdir(json_folder):
        if filename.endswith(".json"):
            # 读取JSON文件
            json_path = os.path.join(json_folder, filename)
            with open(json_path, "r") as f:
                data = json.load(f)
            
            # 解析JSON内容
            shapes = data["shapes"]
            
            # 获取原始图像的大小
            image_width = data["imageWidth"]
            image_height = data["imageHeight"]
            
            # 创建空白掩码图像
            mask_image = Image.new("RGB", (image_width, image_height))
            draw = ImageDraw.Draw(mask_image)
            
            # 绘制形状掩码
            for shape in shapes:
                label = shape["label"]
                points = shape["points"]
                
                # 获取类别对应的颜色
                color = color_map.get(label)
                
                # 绘制多边形
                # 将每个点的坐标从数组形式转换为元组形式
                points_tuple = [(int(point[0]), int(point[1])) for point in points]
                draw.polygon(points_tuple, fill=color)
            
            # 保存掩码图像
            output_path = os.path.join(output_folder, filename.replace(".json", ".png"))
            mask_image.save(output_path)
            print("Saved mask image:", output_path)


# 指定JSON文件夹和输出文件夹的路径
json_folder = "json"
output_folder = "mask"

# 转换JSON标注为掩码标注
convert_json_to_masks(json_folder, output_folder)