import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径

cv2.imshow('gray',img)
# 获取图像高度和宽度
height = img.shape[0]
width = img.shape[1]

# 创建图像
#result =np.zeros((height,width),np.uint8)

# 图像像灰度反转
img2=255-img
cv2.imshow('reverse',img2)
cv2.imwrite('D:\\OpenCV\\save\\reverse.png',img2)#保存

img3=img
for i in range(width):
    for j in range(height):
        img3[i][j]=img3[i][j]+20
cv2.imshow('light',img3)
print(img3)
cv2.imwrite('D:\\OpenCV\\save\\light.png',img3)#保存



cv2.waitKey(0)
cv2.destroyAllWindows()