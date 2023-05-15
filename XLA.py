# KHAI BÁO CÁC THƯ VIỆN CẦN SỬ DỤNG
import os
import cv2
import matplotlib.pyplot as plt
from skimage import color,data
from skimage.filters import threshold_local
from skimage.filters import threshold_otsu
from PIL import Image as im
import numpy as np
from skimage.filters import try_all_threshold

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

path2=r'C:\Users\NguyenHien\TTXLA\BTAP_CHUONG1\anh.jpg'
image2=plt.imread(path2)
# Chuyển ảnh màu sang ảnh xám bằng hàm rgb2gray
anhxam = color.rgb2gray(image2)
# Sử dụng hàm phân ngưỡng
fig, ax = try_all_threshold(anhxam, verbose=False)
# Hiển thị kết quả.
plt.show()