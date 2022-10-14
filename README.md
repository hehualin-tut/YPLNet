# CRDDC2022
Crowdsensing-based Road Damage Detection Challenge (CRDDC2022)
# Crowdsensing-based Road Damage Detection Challenge 2022 TUT submission
This repository contains source code and trained models fo [Crowdsensing-based Road Damage Detection Challenge](https://crddc2022.sekilab.global/overview/)  that was held as part of 2022 IEEE Big Data conference.

The following are the results of our group in this competition
|          | all countries | India | Japan | Norway | US   |Mean-F1 Score   |
| :------: | :-----------: | ----- | ----- | :-----------: | ---- | :-----------: |
| F1-Score |         0.694      |    0.519   |    0.773   |     0.464   |    0.727  |    0.635   |


Sample predictions:
|                             D00                              |                             D10                              |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="https://user-images.githubusercontent.com/92203298/189850301-5d7382d6-ea01-4aad-a34d-876bb2699bb4.jpg" width="200" height="200" alt="D00"/> | <img src="https://user-images.githubusercontent.com/92203298/189851027-b6cc3800-6524-47eb-adf5-7bd60df18e93.jpg" width="200" height="200" alt="D00"/> |
|                             D20                              |                             D40                              |
| <img src="https://user-images.githubusercontent.com/92203298/189851969-dabd3d40-ea05-4dcd-babe-c4c7fe28e64a.jpg" width="200" height="200" alt="D00"/> | <img src="https://user-images.githubusercontent.com/92203298/189851990-c229a1e2-80a3-4cf2-a860-314f860a8032.jpg" width="200" height="200" alt="D00"/> |

# Table of contents
1.[Prerequisites](https://github.com/hehualin-tut/YPLNet#prerequisites) 


2.[Quick-start](https://github.com/hehualin-tut/YPLNet#Quick-start)


3.[Inference(Detection)](https://github.com/hehualin-tut/YPLNet#Inference(Detection))


4.[Training](https://github.com/hehualin-tut/YPLNet#Training)

  
# Quick-start
1. Clone the road-damage-detection repo into your path:

   ```
   git clone https://github.com/hehualin-tut/YPLNet.git
   ```
# Prerequisites
You need to install:

- [Python3 >= 3.6](https://www.python.org/downloads/)

- Use `requirements.txt` to install required python dependencies

  ```
  # Python >= 3.6 is needed
  cd yolov5-master
  pip3 install -r requirements.txt
  ```
-Note：The experiment is carried out on a TeslaV100 of the Ubuntu18.04 system, If you get a ''CUDA Out of Memory'' error during the training phase, you can try to reduce ''the img-size'' and ''batch-size''.
   
# Inference(Detection)

1.Execute one of the follwoing commands to generate `results.csv`(competition format) and predicated images under `inference/output/`

 
  ```
  python3 detect.py --weights weights/all/32-1280-140.pt --img 1280 --source [your datasets path] --conf-thres 0.09 --iou-thres 0.9999 --agnostic-nms --augment
  ```
  
  ```
  python3 detect.py --weights weights/India/32-1280-140.pt --img 1280 --source [your datasets path] --conf-thres 0.07 --iou-thres 0.9999 --agnostic-nms --augment
  ```

  ```
  python3 detect.py --weights weights/Japan/32-1024-150.pt --img 1024 --source [your datasets path] --conf-thres 0.14 --iou-thres 0.9999 --agnostic-nms --augment
  ```

  ```
  python3 detect.py --weights weights/Norway/32-1280-138.pt --img 1280 --source [your datasets path] --conf-thres 0.10 --iou-thres 0.9999 --agnostic-nms --augment
  ```

  ```
  python3 detect.py --weights weights/US/32-1280-140.pt --img 1280 --source [your datasets path] --conf-thres 0.11 --iou-thres 0.9999 --agnostic-nms --augment
  ```
  
# Training

1.
  For all countries, India, Norway and US, we use weights under different epochs in a training because it saves time. you could run: 

   ```
   python3 train.py --data data/rdd4.yaml --cfg models/yolov5s-psalcfi.yaml --batch-size 32 --img-size 1280 --epoch 140
   ```
  Then, the weights under runs/train/[your project] are processed using the optimizer. Before that, you need to change the ```home_dir``` and ```sub_dir```  in the ```optimizer.py``` to the paths under your own project. Then, you could run this:
  
  ```
   python3 optimizer.py
  ```
  For my own inference results, the epochs corresponding to all countries, India, Norway and US are 140, 140, 138, and 140, respectively.
  
2.  
  For Japan, you could run:
  ```
  python3 train.py --data data/rdd4.yaml --cfg models/yolov5s-psalcfi.yaml --batch-size 32 --img-size 1024 --epoch 150
  ```
visit [yolov5](https://github.com/ultralytics/yolov5) official source code for more training and inference time arguments




















