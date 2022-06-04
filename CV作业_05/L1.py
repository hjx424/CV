import cv2
import numpy as np
import matplotlib.pyplot as plt

G1=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)
G11=cv2.Sobel(G1,cv2.CV_64F,1,0,ksize=3)
G12=cv2.Sobel(G1,cv2.CV_64F,0,1,ksize=3)
G11=cv2.convertScaleAbs(G11)
G12=cv2.convertScaleAbs(G12)
cv2.imshow("G11",G11)
cv2.imshow("G12",G12)


A1=cv2.imread('D:\\OpenCV\\test\\A.png',cv2.IMREAD_GRAYSCALE)

A11=cv2.Sobel(A1,cv2.CV_64F,1,0,ksize=3)
A12=cv2.Sobel(A1,cv2.CV_64F,0,1,ksize=3)
A11=cv2.convertScaleAbs(A11)
A12=cv2.convertScaleAbs(A12)
cv2.imshow("A11",A11)
cv2.imshow("A12",A12)

cv2.imwrite('D:\\OpenCV\\save\\homework_5\\L1\\G11.png',G11)
cv2.imwrite('D:\\OpenCV\\save\\homework_5\\L1\\G12.png',G12)
cv2.imwrite('D:\\OpenCV\\save\\homework_5\\L1\\A11.png',A11)
cv2.imwrite('D:\\OpenCV\\save\\homework_5\\L1\\A12.png',A12)


cv2.waitKey(0)
cv2.destroyAllWindows()