import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('D:\\OpenCV\\test\\test1.jpg')# 路径
# i


b,g,r=cv2.split(img)
cv2.imshow('blue',b)
cv2.imwrite('D:\\OpenCV\\save\\blue.png',b)#保存
cv2.imshow('green',g)
cv2.imwrite('D:\\OpenCV\\save\\green.png',g)#保存
cv2.imshow('red',r)
cv2.imwrite('D:\\OpenCV\\save\\red.png',r)#保存

#ii
img1=cv2.imshow('com',cv2.merge([b,cv2.subtract(g,20),cv2.add(r,20)]))
cv2.imwrite('D:\\OpenCV\\save\\com.jpg',img1)#保存


# Iii
img2=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径
img3=42*np.log(1.0+img2)
img3=np.uint8(img3+0.5) # uint8图片数据
cv2.imshow('log',img3)
cv2.imwrite('D:\\OpenCV\\save\\log.png',img3)#保存
# Iv
lut=np.zeros(256,dtype=np.float32)
for i in range(256):
    lut[i]= 0.00000005*i**4.0
img4=cv2.LUT(img2,lut)
img4=np.uint8(img4+0.5)
cv2.imshow('gmma',img4)
cv2.imwrite('D:\\OpenCV\\save\\gmma.png',img4)#保存



cv2.waitKey(0)
cv2.destroyAllWindows()