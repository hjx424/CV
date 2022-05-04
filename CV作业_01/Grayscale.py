
# 初次接触openCV做的一个图像处理的小程序，同时也是第一次使用python语言写代码，其中可能会有语法不符合规定的地方，请见谅，也会慢慢学习python的使用
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('D:\\OpenCV\\test\\test1.jpg',cv2.IMREAD_GRAYSCALE)# 路径
cv2.imshow('灰度图',img)
#print(img)# 输出矩阵的值
print(img)
cv2.imwrite('D:\\OpenCV\\save\\grayscale01.png',img)#保存灰度图

#  L1
# 前两行平均值
sum1=0

for i in range(len(img[0][:])):
 sum1+=int(img[0][i])+int(img[1][i])

mean1=sum1/(512*2)
ret, thresh1 = cv2.threshold(img, mean1, 255, cv2.THRESH_BINARY)
cv2.imshow('01',thresh1)

cv2.imwrite('D:\\OpenCV\\save\\01.png',thresh1)
# 前两行中位数
arr=[]
for i in range(2):
 for j in range(len(img[0][:])):
  arr.append(img[i][j])

arr.sort()


mean2=int((arr[511])+int(arr[512]))/2
# print(mean2)
ret, thresh2 = cv2.threshold(img, mean2, 255, cv2.THRESH_BINARY)
cv2.imshow('02',thresh2)
cv2.imwrite('D:\\OpenCV\\save\\02.png',thresh2)
#  L2
# 计算整个矩阵平均值
mean3=np.mean(img)
ret, thresh3 = cv2.threshold(img, mean3, 255, cv2.THRESH_BINARY)
# print(mean3)
# cv2.imwrite('D:\\OpenCV\\save\\grayscale01.png',img)#保存灰度图
cv2.imshow('03',thresh3)
cv2.imwrite('D:\\OpenCV\\save\\03.png',thresh3)

# 计算整个矩阵平均数
arr1=[]
for i in range(len(img[:][0])):
 for j in range(len(img[0][:])):
  arr1.append(img[i][j])
arr1.sort()
mean4=(int(arr1[131071])+int(arr1[131072]))/2
ret, thresh4 = cv2.threshold(img, mean4, 255, cv2.THRESH_BINARY)
cv2.imshow('04',thresh4)
cv2.imwrite('D:\\OpenCV\\save\\04.png',thresh4)
# L3 这里我用了图像截取和拼接
img1=img[0:256,:]
img2=img[256:512,:]


ret, thresh5 = cv2.threshold(img1, mean3, 255, cv2.THRESH_BINARY)
# img3=thresh5+img2
img3=np.vstack([thresh5,img2])
cv2.imshow('05',img3)
cv2.imwrite('D:\\OpenCV\\save\\05.png',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
