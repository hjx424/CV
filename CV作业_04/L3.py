import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

G1=cv2.imread('D:\\OpenCV\\test\\P1.jpg',cv2.IMREAD_GRAYSCALE)
G2=cv2.imread('D:\\OpenCV\\test\\P2.jpg',cv2.IMREAD_GRAYSCALE)

G12=cv2.GaussianBlur(G1,(5,5),1)
G22=cv2.GaussianBlur(G2,(5,5),1)
G23=cv2.medianBlur(G2,5)

cv2.imshow("G12",G12)
cv2.imshow("G22",G22)
cv2.imshow("G23",G23)
print(G12[0:9,0:9])
print(G22[0:9,0:9])
print(G23[0:9,0:9])


cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L3\\G12.png',G12)
cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L3\\G22.png',G22)
cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L3\\G23.png',G23)
cv2.waitKey(0)
cv2.destroyAllWindows()