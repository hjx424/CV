import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径  # 0 表示灰度图

plt.hist(img.ravel(),256)

plt.savefig('D:\\OpenCV\\save\\homework_3\\L1\\H1.png') # 在show之前使用

plt.show()

width=img.shape[0]
height=img.shape[1]

img1=img
img1=cv2.multiply(img1,2)
'''
for i in range(width):
    for j in range(height):
        img1[i][j]=cv2.multiply(img[i][j],2)
'''

cv2.imshow('P2',img1)
cv2.imwrite('D:\\OpenCV\\save\\homework_3\\L1\\P2.png',img1)
plt.hist(img1.ravel(),256)
plt.savefig('D:\\OpenCV\\save\\homework_3\\L1\\H2.png') # 在show之前使用
plt.show()

img2=img
for i in range(width):
    for j in range(height):
        img2[i][j]=0.5*img[i][j]

cv2.imshow('P3',img2)
cv2.imwrite('D:\\OpenCV\\save\\homework_3\\L1\\P3.png',img2)
plt.hist(img2.ravel(),256)
plt.savefig('D:\\OpenCV\\save\\homework_3\\L1\\H3.png') # 在show之前使用
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()