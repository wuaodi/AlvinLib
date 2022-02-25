import math
import os
from xml.etree.ElementTree import parse

import numpy as np
from tqdm import tqdm
import numpy


# theta逆时针为正(x轴向右，y轴向下的坐标定义下)
def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc
    yoff = yp - yc
    cosTheta = math.cos(theta)
    sinTheta = math.sin(theta)
    pResx = cosTheta * xoff + sinTheta * yoff
    pResy = - sinTheta * xoff + cosTheta * yoff
    return xc + pResx, yc + pResy


# roLabelImg定义的angle为顺时针正，所以加负号
def addRotatedShape(cx, cy, w, h, angle):
    p0x, p0y = rotatePoint(cx, cy, cx - w / 2, cy - h / 2, -angle)
    p1x, p1y = rotatePoint(cx, cy, cx + w / 2, cy - h / 2, -angle)
    p2x, p2y = rotatePoint(cx, cy, cx + w / 2, cy + h / 2, -angle)
    p3x, p3y = rotatePoint(cx, cy, cx - w / 2, cy + h / 2, -angle)
    points = [(p0x, p0y), (p1x, p1y), (p2x, p2y), (p3x, p3y)]
    return points


def readXML(dir, filename, name_map):
    doc = parse(dir + filename)
    root = doc.getroot()
    bbox_info = []
    obj_nums = [0,0,0,0,0,0,0,0,0]
    for element in root.findall('object'):
        name = element.find('name').text
        name = name_map[name]
        # 统计各类别目标的数量
        if name == "solar-panel":
            obj_nums[0] += 1
        elif name == "track-field":
            obj_nums[1] += 1
        elif name == "highway-bridge":
            obj_nums[2] += 1
        elif name == "waterway-bridge":
            obj_nums[3] += 1
        elif name == "ship":
            obj_nums[4] += 1
        elif name == "overpass":
            obj_nums[5] += 1
        elif name == "storage-tank":
            obj_nums[6] += 1
        elif name == "airplane":
            obj_nums[7] += 1
        elif name == "windmill":
            obj_nums[8] += 1
        else:
            pass
        robndbox = element.find('robndbox')
        cx = robndbox.find('cx').text
        cy = robndbox.find('cy').text
        w = robndbox.find('w').text
        h = robndbox.find('h').text
        angle = robndbox.find('angle').text
        one_bbox = [name, cx, cy, w, h, angle]
        bbox_info.append((one_bbox))
    return bbox_info, obj_nums


def writeTXT(dir, xml_name, bbox_info):
    with open(dir + xml_name.split(".")[0] + '.txt', 'a') as f:
        f.write('imagesource:GF\n')
        f.write('gsd:None\n')
        for i in bbox_info:
            name = i[0]
            cx = float(i[1])
            cy = float(i[2])
            w = float(i[3])
            h = float(i[4])
            angle = float(i[5])
            points = addRotatedShape(cx, cy, w, h, angle)
            one_dota_info = str(float(round(points[0][0]))) + str(' ') + str(float(round(points[0][1]))) + str(' ') + \
                            str(float(round(points[1][0]))) + str(' ') + str(float(round(points[1][1]))) + str(' ') + \
                            str(float(round(points[2][0]))) + str(' ') + str(float(round(points[2][1]))) + str(' ') + \
                            str(float(round(points[3][0]))) + str(' ') + str(float(round(points[3][1]))) + str(' ') + \
                            name + ' 0'
            f.write(one_dota_info + '\n')


if __name__ == "__main__":
    # 配置
    xml_dir_path = "opt3951final_xml\\"
    txt_dir_path = "opt3951final_dota\\"
    name_map = {
        "Solar panel": "solar-panel",           "Track Field": "track-field",   "Highway Bridge": "highway-bridge",
        "Waterway Bridge":  "waterway-bridge",  "Ship": "ship",                 "Overpass": "overpass",
        "Storage Tank": "storage-tank",         "Airplane": "airplane",         "Windmill": "windmill",
    }

    # 执行
    obj_nums_all = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for filename in tqdm(os.listdir(xml_dir_path)):
        bbox_info, obj_nums = readXML(xml_dir_path, filename, name_map)  # 读取xml文件中的信息
        writeTXT(txt_dir_path, filename, bbox_info)  # 讲xml中的信息进行转换，并以DOTA格式写入txt文档
        obj_nums = np.array(obj_nums)
        obj_nums_all = np.array(obj_nums_all)
        obj_nums_all += obj_nums
    print(obj_nums_all)
