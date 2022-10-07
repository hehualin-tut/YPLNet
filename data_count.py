import os
import xml.etree.ElementTree as ET

# xml_path = "/home/user/kemove/data/annotations/test/"
xml_path = "/data/1hhl/RDD2022/Japan/train/annotations/xmls/"
xml_files = os.listdir(xml_path)
txt_path='/data/1hhl/RDD2022/rdd6/Japan/labels/train/'
txt_files=os.listdir(txt_path)
classes1 = {"D00":0, "D10":0, "D20":0, "D40":0}
classes2 = {"0":0, "1":0, "2":0, "3":0}

#xml_files
for i in xml_files:
    tree = ET.parse(os.path.join(xml_path, i))
    root = tree.getroot()
    for object in root.findall("object"):
        label = object.find('name').text
        if label in classes1:
            classes1[label]+=1
print(classes1)

#txt_files
for i in txt_files:
    in_file = open(txt_path + i, 'r')
    lines = in_file.readlines()
    for j in range(len(lines)):
        if lines[j][0] in classes2:
              classes2[lines[j][0]]+=1
print(classes2)





