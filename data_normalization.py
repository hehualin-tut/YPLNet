import os
import xml.etree.ElementTree as ET

def main(img_path, xml_path, txt_path, obj_cls, txt_files):

    if not os.path.exists(txt_path):
        os.makedirs(txt_path)

    all_xml_files = os.listdir(xml_path)
    all_img_files = os.listdir(img_path)

    for i_xml in all_xml_files:
        i_img = i_xml.replace(".xml", ".jpg")
        if i_img not in all_img_files:
            print("缺少对应图片数据", i_img)
        else:
            with open(txt_files, "a") as f1:
                f1.write(img_path+i_img+"\n")
            
            tree = ET.parse(xml_path + i_xml)
            root = tree.getroot()

            size = root.find("size")
            width = int(size.find("width").text)
            height = int(size.find("height").text)

            i_txt = i_xml.replace(".xml", ".txt")

            for _obj in root.iter("object"):
                cls_name = _obj.find("name").text
                if cls_name not in obj_cls:
                    continue
                cls_index_value = obj_cls.index(cls_name)

                bbox = _obj.find("bndbox")
                xmin = float(bbox.find("xmin").text)
                ymin = float(bbox.find("ymin").text)
                xmax = float(bbox.find("xmax").text)
                ymax = float(bbox.find("ymax").text)


                x_center = (xmin + xmax) / (2 * width)
                y_center = (ymin + ymax) / (2 * height)

                norm_width = (xmax - xmin) / width
                norm_height = (ymax - ymin) / height

                with open(txt_path+i_txt, "a") as f2:
                    f2.write(str(cls_index_value) + " " + str(x_center) + " " + str(y_center) + " " + str(norm_width) + " " + str(norm_height) + "\n")


if __name__ == "__main__":
    img_path = "/data/1hhl/car/images/test/"
    xml_path = img_path.replace("images", "annotations")
    txt_path = img_path.replace("images", "labels")
    obj_cls = ['D00', 'D10', 'D20', 'D40']
    txt_files = "/data/1hhl/car/val.txt"
    main(img_path, xml_path, txt_path, obj_cls, txt_files)