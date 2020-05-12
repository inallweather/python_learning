"""
@version: 1.0
@author: jack-liu
@file: init_canvas.py
@time: 2020/5/11 19:37
"""

import numpy as np
import cv2

# def init_canvas(width, height, color=(255, 255, 255)):
#     canvas = np.ones((width, height, 3), dtype='uint8')
#     canvas[:] = color
#     # print(canvas, '----', color)
#     return canvas
#
#
# canvas = init_canvas(200, 400, (125, 40, 255))
#
# cv2.imshow('image', canvas)
#
# img = np.ones((300, 300, 3), dtype='uint8')
# img *= 125
#
# img_g, img_b, img_r = cv2.split(canvas)
# color = (100, 20, 50)
#
# img_g *= color[0]
# img_b *= color[1]
# img_r *= color[2]
#
# imgg = cv2.merge([img_g, img_b, img_r])
# cv2.imshow('color', imgg)
#
# # print(img_b, img_g, img_r)
#
# cv2.imshow('white', img)


# def init_canvas(width, height, color=(255, 255, 255)):
#     canvas = np.ones((width, height, 3), dtype='uint8')
#     chanel_b, chanel_g, chanel_r = cv2.split(canvas)
#     chanel_b *= color[0]
#     chanel_g *= color[1]
#     chanel_r *= color[2]
#     return cv2.merge([chanel_b, chanel_g, chanel_r])


# def init_canvas(width, height, color=(255, 255, 255)):
#     canvas = np.ones((width, height, 3), dtype='uint8')
#     canvas[:, :, 0] = color[0]
#     canvas[:, :, 1] = color[1]
#     canvas[:, :, 2] = color[2]
#     return canvas

# def init_canvas(width, height, color=(255, 255, 255)):
#     canvas = np.ones((width, height, 3), dtype='uint8')
#     canvas[:] = color
#     return canvas
#
#
# canvas = init_canvas(300, 300, (125, 40, 100))
#
# cv2.imshow('Color', canvas)

ls = np.arange(27).reshape(3, 3, 3)
print(ls)
print('--'*30)
ls[:] = (10, 100, 10)
print(ls)


# cv2.waitKey()
# cv2.destroyAllWindows()
