import os
import shutil
import random

train_img_path = "/data/1hhl/car/images/train/"
train_xml_path = "/data/1hhl/car/training-1/xml/"
test_img_path = train_img_path.replace("train", "test")
test_xml_path = '/data/1hhl/car/testxml/xml/'
if not os.path.exists(test_img_path):
    os.makedirs(test_img_path)
if not os.path.exists(test_xml_path):
    os.makedirs(test_xml_path)

all_imgs = os.listdir(train_img_path)
random.shuffle(all_imgs)
ratio = 0.2 #测试集划分比例
test_num = int(len(all_imgs) * ratio)
index_pic = 0

for i in all_imgs:
    if index_pic < test_num:
        i_xml = i.replace(".jpg", ".xml")
        shutil.move(train_img_path+i, test_img_path+i)
        shutil.move(train_xml_path+i_xml, test_xml_path+i_xml)
        index_pic+=1
