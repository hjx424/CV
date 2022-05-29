import cv2  # opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt  # Matplotlib读取的格式是RGB

def MeanFilter(img, K_size=3):
    h, w = img.shape
    pad = K_size // 2
    out = np.zeros((h + 2 * pad, w + 2 * pad), dtype=np.float)
    out[pad:pad + h, pad:pad + w] = img.copy().astype(np.float)
    tmp = out.copy()
    for y in range(h):
        for x in range(w):

                out[pad + y, pad + x] = np.mean(tmp[y:y + K_size, x:x + K_size])

    out = out[pad:pad + h, pad:pad + w].astype(np.uint8)

    return out


G1=cv2.imread('D:\\OpenCV\\test\\P1.jpg',cv2.IMREAD_GRAYSCALE)
G2=cv2.imread('D:\\OpenCV\\test\\P2.jpg',cv2.IMREAD_GRAYSCALE)

print(G1[0:9,0:9])
print(G2[0:9,0:9])

G1_L2=MeanFilter(G1)
G2_L2=MeanFilter(G2)
cv2.imshow('G1_L2',MeanFilter(G1))
cv2.imshow('G2_L2',MeanFilter(G2))
print(G1_L2[0:9,0:9])
print(G2_L2[0:9,0:9])
cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L2\\G1_L2.png',G1_L2)
cv2.imwrite('D:\\OpenCV\\save\\homework_4\\L2\\G2_L2.png',G2_L2)

cv2.waitKey(0)
cv2.destroyAllWindows()