"""
@version: 1.0
@author: jack-liu
@file: binnary_img.py
@time: 2020/5/11 20:19
"""
import numpy as np
import cv2

cpu = cv2.imread('img/CPU2.png')

if cpu is None:
    print('请查看图片路径')
    exit()

# 阈值下界
lowerb = (142, 142, 142)
# 阈值上界
upperb = (255, 255, 255)

mask = cv2.inRange(cpu, lowerb, upperb)

cv2.imshow('image', mask)

cv2.waitKey()
cv2.destroyAllWindows()
