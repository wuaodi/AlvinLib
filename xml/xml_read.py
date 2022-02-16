"""
读取和修改xml文件
参考链接 https://blog.csdn.net/wsp_1138886114/article/details/86576900
"""

from xml.etree.ElementTree import parse, Element
import os

xml_path = 'new_place\\xml\\'
new_path = 'new_place\\xml_new\\'

for filename in os.listdir(xml_path):
    print(filename)
    doc = parse(xml_path + filename)
    root = doc.getroot()

    # change text of child node
    root.find('folder').text = 'xml'
    root.find('filename').text = filename[0:-4]
    root.find('path').text = xml_path + filename

    # Write back to a file
    doc.write(new_path + filename, xml_declaration=True)

