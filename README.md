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

