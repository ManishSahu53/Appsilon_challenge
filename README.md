# Appsilon_challenge
## Overview
1. **Create training dataset**

Since dataset was not given, I used google image search as source of dataset. I search Cary type in google image search and downloaded ~300 images of each category. I used Firefox addon to download all images at bulk.

2. **Deep Neural Network Architecture**

Since object dectection and recognition is standard problem and SOTA architecture exist. So I prefer to use YOLOv3 architecture for object detection and recognition.

3. **Creating Labels**

I used pre-trained YOLOv3 architecture to generate bounding boxes around cars and assigned with suitable class there after. This eliminated my time to manually drawing bounding boxes

4. **Training Network**

I used 6 six categories with ~1800 labeled bounding boxes datasets.

5. **Training Hardware**

Training YOlOv3 is GPU extensive task. I don't have a GPU pc so I used google's Colab to train my network. It comes with 12 GB of GPU with latest Nvidia GPU.


## Trained model
1. Weights - https://drive.google.com/file/d/1YKvLkQjYgF7rlaejk07DhBtQZE9rhpUL/view?usp=sharing
2. Results - https://drive.google.com/drive/folders/1rfAqpni8vORZtWAbQNNnxlTg5GC11V_D?usp=sharing
3. Yolo Git - https://github.com/ManishSahu53/YoloV3
4. Yolo-pre-trained Weights - wget https://pjreddie.com/media/files/darknet53.conv.74
5. Colab - https://colab.research.google.com/drive/1wnnWwtzdP-FN6rlSr5LbjQ_UuU2dvcRQ

## How to Run
1. Clone this repo and Yolo Git - https://github.com/ManishSahu53/YoloV3
2. Download weights from https://drive.google.com/file/d/1YKvLkQjYgF7rlaejk07DhBtQZE9rhpUL/view?usp=sharing
3. Paste [car_classes.txt](https://github.com/ManishSahu53/Appsilon_challenge/blob/master/car_classes.txt) present in this repo and paste it in model_data folder present in [yolo repo](https://github.com/ManishSahu53/YoloV3)

```
python test.py --image path_folder_image --model model.h5 --classes model_data/car_classes.txt --output path_folder_output
```
