"""
@version: 1.0
@author: jack-liu
@file: interpolation.py
@time: 2020/5/11 18:29
"""

"""
opencv 的差值
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.uint8(np.random.randint(0, 255, (5, 5)))

# 声明一个新的维度
new_shape = (512, 512)
# 产生2行3列的图形
plt.subplot(231)
plt.title('SRC image')
plt.imshow(img, cmap='seismic')
plt.yticks([])
plt.xticks([])

plt.subplot(232)
plt.title('INTER_NEAREST')
resized = cv2.resize(img, new_shape, interpolation=cv2.INTER_NEAREST)
plt.imshow(resized, cmap='seismic')
plt.yticks([])
plt.xticks([])

plt.subplot(233)
plt.title('INTER_LINEAR')
resized = cv2.resize(img, new_shape, interpolation=cv2.INTER_LINEAR)
plt.imshow(resized, cmap='seismic')
plt.yticks([])
plt.xticks([])

plt.subplot(234)
plt.title('INTER_AREA')
resized = cv2.resize(img, new_shape, interpolation=cv2.INTER_AREA)
plt.imshow(resized, cmap='seismic')
plt.yticks([])
plt.xticks([])

plt.subplot(235)
plt.title('INTER_CUBIC')
resized = cv2.resize(img, new_shape, interpolation=cv2.INTER_CUBIC)
plt.imshow(resized, cmap='seismic')
plt.yticks([])
plt.xticks([])

plt.subplot(236)
plt.title('INTER_LANCZOS4')
resized = cv2.resize(img, new_shape, interpolation=cv2.INTER_LANCZOS4)
plt.imshow(resized, cmap='seismic')
plt.yticks([])
plt.xticks([])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')

plt.show()
