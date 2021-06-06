# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:02:40 2021

@author: YDD
"""

from PIL import Image
import numpy as np
import cv2

a = np.array(Image.open(r"G:\大三下\Python\实验4\csu.jpg"))
b =[255,255,255]-a
im  =Image.fromarray(b.astype( 'uint8' ))
im.save(r"G:\大三下\Python\实验4\csu_new0.jpg")

image_gray = np.array(Image.open(r"G:\大三下\Python\实验4\csu.jpg").convert('L'))
result1 = 255-image_gray
result2 = (100/255)*image_gray + 150
result3 = 255*(a/255)**2
im  =Image.fromarray(result1.astype( 'uint8' ))
im.save(r"G:\大三下\Python\实验4\csu_new1.jpg")
im  =Image.fromarray(result2.astype( 'uint8' ))
im.save(r"G:\大三下\Python\实验4\csu_new2.jpg")
im  =Image.fromarray(result3.astype( 'uint8' ))
im.save(r"G:\大三下\Python\实验4\csu_new3.jpg")

#加入高斯噪声,黑白图
noise = np.random.normal(0, 0.5, image_gray.shape) #产生噪声
new_image_gray = image_gray + noise #加入噪声
img_mean = cv2.blur(new_image_gray, (5,5)) #均值滤波
im  =Image.fromarray(img_mean.astype( 'uint8' ))
im.save(r"G:\大三下\Python\实验4\img_mean.jpg") #保存图像
