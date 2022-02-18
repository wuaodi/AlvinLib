"""
读取和删除xml子节点
参考链接 https://blog.csdn.net/wsp_1138886114/article/details/86576900
"""

from xml.etree.ElementTree import parse, Element
import os


# 删除xml文件中某个标注类别
def xml_remove(xml_path, category):
    doc = parse(xml_path)
    root = doc.getroot()

    # remove the specified category
    for element in root.findall('object'):
        if element.find('name').text == category:
            root.remove(element)

    # Write back to a file
    doc.write(xml_path, xml_declaration=True)


if __name__ == "__main__":
    xml_dir = 'new_place\\xml_opt\\'
    for filename in os.listdir(xml_dir):
        print(filename)
        xml_path = xml_dir + filename
        xml_remove(xml_path, 'Ship')  # 删除xml文件中的ship类

