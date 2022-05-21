import cv2  # opencv读取的格式是BGR
import math
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径  # 0 表示灰度图

height=img.shape[0]
width=img.shape[1]

img1=(img-np.min(img))/(np.max(img)-np.min(img))

for i in range(height):
    for j in range(width):
            img1[i][j] = math.log(1.0 + img1[i][j])


#
cv2.imshow('01',img1)
cv2.normalize(img1, img1, 0, 255, cv2.NORM_MINMAX)
cv2.imwrite('D:\\OpenCV\\save\\homework_3\\L2\\P4.png',img1)
plt.hist(img1.ravel(),256)
plt.savefig('D:\\OpenCV\\save\\homework_3\\L2\\H4.png') # 在show之前使用
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()