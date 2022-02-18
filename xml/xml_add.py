"""
将一个xml文件中的某个类别的标注（一个节点），添加到另一个xml文件中
"""

import os
from xml.etree.ElementTree import parse


def xml_add(xml_from_path, xml_to_path, category):
    doc_from = parse(xml_from_path)
    doc_to = parse(xml_to_path)
    root_from = doc_from.getroot()
    root_to = doc_to.getroot()

    # 从xml_from获取category类别标注的节点, 添加到xml_to
    for element in root_from.findall('object'):
        if element.find('name').text == category:
            root_to.append(element)

    # Write back to a file
    doc_to.write(xml_to_path, xml_declaration=True)


if __name__ == "__main__":
    xml_from_dir = 'new_place\\xml_sar\\'
    xml_to_dir = 'new_place\\xml_opt\\'

    for filename in os.listdir(xml_from_dir):
        xml_from_path = xml_from_dir + filename
        # xml_to_path = xml_to_dir + filename
        xml_to_path = xml_to_dir + 'opt' + filename[3:]
        # if filename in os.listdir(xml_to_dir):
        if 'opt' + filename[3:] in os.listdir(xml_to_dir):
            xml_add(xml_from_path, xml_to_path, 'Ship')
            os.remove(xml_from_path)
