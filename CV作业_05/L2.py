import cv2
import numpy as np
import matplotlib.pyplot as plt

G1=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)
G11=cv2.Sobel(G1,cv2.CV_64F,1,0,ksize=3)
G12=cv2.Sobel(G1,cv2.CV_64F,0,1,ksize=3)
G11=cv2.convertScaleAbs(G11)
G12=cv2.convertScaleAbs(G12)

G2=cv2.addWeighted(G11,0.5,G12,0.5,0)
cv2.imshow("G2",G2)
cv2.imwrite('D:\\OpenCV\\save\\homework_5\\L2\\G2.png',G2)
cv2.waitKey(0)
cv2.destroyAllWindows()