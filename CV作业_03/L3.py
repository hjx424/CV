import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',0)# 路径  # 0 表示灰度图
'''
equ1=cv2.equalizeHist(img)
cv2.imshow('P12',equ1)
'''
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
P11=clahe.apply(img)
cv2.imshow('P11',P11)
cv2.imwrite('D:\\OpenCV\\save\\homework_3\\L3\\P11.png',P11)

plt.hist(P11.ravel(),256)
plt.savefig('D:\\OpenCV\\save\\homework_3\\L3\\H11.png')
plt.show()

img2=cv2.imread('D:\\OpenCV\\save\\homework_3\\L1\\P2.png',0)
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
P21=clahe.apply(img2)
cv2.imshow('P21',P21)
cv2.imwrite('D:\\OpenCV\\save\\homework_3\\L3\\P21.png',P21)
plt.hist(P21.ravel(),256)
plt.savefig('D:\\OpenCV\\save\\homework_3\\L3\\H21.png')
plt.show()


img3=cv2.imread('D:\\OpenCV\\save\\homework_3\\L1\\P3.png',0)
clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
P31=clahe.apply(img3)
cv2.imshow('P31',P31)
cv2.imwrite('D:\\OpenCV\\save\\homework_3\\L3\\P31.png',P31)
plt.hist(P31.ravel(),256)
plt.savefig('D:\\OpenCV\\save\\homework_3\\L3\\H31.png')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()