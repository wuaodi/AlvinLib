"""
删除文件夹中无标注的xml文件
"""
import os
from xml.etree.ElementTree import parse


def xml_none(dir_path):
    for filename in os.listdir(dir_path):
        doc = parse(dir_path + filename)
        root = doc.getroot()

        if len(root.findall('object')) == 0:
            os.remove(dir_path + filename)


if __name__ == "__main__":
    xml_dir = "new_place\\xml_opt\\"
    xml_none(xml_dir)
