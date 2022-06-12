import math

import cv2
import numpy as np
import matplotlib.pyplot as plt

G1=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)
height,width=G1.shape[:2]

def imrotate(image, b):
    b = -math.radians(b % 360)  # 将角度化为弧度
    n = np.size(image, 0)
    m = np.size(image, 1)

    nn=n
    nm=m
    img = np.zeros((nn, nm), dtype=np.uint8)
    center = (n/2, m/2)



    def inmap(x, y):
       return True if x >= 0 and x < n and y >= 0 and y < m else False



    for x in range(nn):
        for y in range(nm):
            x0 = (x-center[0])*math.cos(-b)+(y-center[1])*math.sin(-b)+center[0]
            y0 = -1*(x-center[0])*math.sin(-b)+(y-center[1])*math.cos(-b)+center[1]
            # 将坐标对齐
            x0 = x0-(nn-n)/2
            y0 = y0-(nm-m)/2
            # 双线性内插值
            i = int(x0)
            j = int(y0)
            u = x0 - i
            v = y0 - j
            if inmap(i, j):
                f1 = (1-u)*(1-v)*image[i][j]
                img[x][y] += f1
                if inmap(i, j+1):
                    f2 = (1-u)*v*image[i][j+1]
                    img[x][y] += f2
                if inmap(i+1, j):
                    f3 = u*(1-v)*image[i+1][j]
                    img[x][y] += f3
                if inmap(i+1, j+1):
                    f4 = u*v*image[i+1][j+1]
                    img[x][y] += f4
    cv2.imshow("G21",img)
    cv2.imwrite('D:\\OpenCV\\save\\homework_6\\L2\\G21.png',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


b=45
imrotate(G1, b)
