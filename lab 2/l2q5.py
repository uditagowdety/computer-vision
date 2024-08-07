import cv2 as cv
import numpy as np

path=r"C:\Users\udita\PycharmProjects\cv\study.jpeg"
img=cv.imread(path,0)

t_lower=140


rows, cols=img.shape

for i in range(rows):
    for j in range(cols):
        if img[i,j]>t_lower:
            img[i,j]=255
        else:
            img[i,j]=0
cv.imshow("gray slicing",img)
cv.waitKey(0)
