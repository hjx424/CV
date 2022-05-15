import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径
cv2.imshow('灰度图',img)

print(img)# 输出矩阵
cv2.imwrite('D:\\OpenCV\\save\\grayscale01.png',img)#保存灰度图

# 获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]

# 创建图像
#result =np.zeros((height,width),np.uint8)

# 图像像灰度反转

img5=img
for w in range(width):
    for h in range(height):
        img5[w][h]=img5[w][h]-20

cv2.imshow('down',img5)
print(img5)

cv2.imwrite('D:\\OpenCV\\save\\down.png',img5)#保存
cv2.waitKey(0)
cv2.destroyAllWindows()