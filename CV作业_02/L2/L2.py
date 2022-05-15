import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径

# print(img)# 输出矩阵


print(img.shape)
width=img.shape[0]
height=img.shape[1]
print(width)
print(height)
img1=img
for i in range(width):
    for j in range(height):
        if img1[i][j] < 20:
            img1[i][j]=img1[i][j] + 20
        elif img1[i][j]>=100 and img1[i][j]<=150:
            img1[i][j]=125
        elif img1[i][j]>150:
            img1[i][j]=img1[i][j]-20

cv2.imshow('L2',img1)
cv2.imwrite('D:\\OpenCV\\save\\L2.png',img1)#保存灰度图
cv2.waitKey(0)
cv2.destroyAllWindows()