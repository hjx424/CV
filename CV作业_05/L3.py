import cv2
import numpy as np
import matplotlib.pyplot as plt

G1=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)
G13 = cv2.Laplacian(G1,cv2.CV_64F)
G13 = cv2.convertScaleAbs(G13)
cv2.imshow("G13",G13)
cv2.imwrite('D:\\OpenCV\\save\\homework_5\\L3\\G13.png',G13)
cv2.waitKey(0)
cv2.destroyAllWindows()