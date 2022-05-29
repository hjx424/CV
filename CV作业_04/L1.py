import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

G1=cv2.imread('D:\\OpenCV\\test\\P1.jpg',cv2.IMREAD_GRAYSCALE)
G2=cv2.imread('D:\\OpenCV\\test\\P2.jpg',cv2.IMREAD_GRAYSCALE)

print(G1[0:9,0:9])
print(G2[0:9,0:9])
G11 = cv2.blur(G1, (3, 3)) #可以更改核的大小
cv2.imshow('G11',G11)
G21 = cv2.blur(G2, (3, 3)) #可以更改核的大小
cv2.imshow('G21',G21)
print(G11[0:9,0:9])
print(G21[0:9,0:9])
cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L1\\G11.png',G11)
cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L1\\G21.png',G21)
cv2.waitKey(0)
cv2.destroyAllWindows()