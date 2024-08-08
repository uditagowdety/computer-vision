#smoothing, sharpening + blur mask, order statistic filter -- median on noise
#gaussian blur
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img=cv.imread(path,0)

box_filter=np.ones((3,3))/9
box_img=cv.filter2D(img,-1,box_filter)

gaussian_filter=np.array([[1,2,1],
                          [2,4,2],
                          [1,2,1]])/16
gaussian_img=cv.filter2D(img,-1,gaussian_filter)
# gaussian_img=cv.GaussianBlur(img, (3,3),0)

sharp_filter=np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
sharp_img=cv.filter2D(img,-1, sharp_filter)

mask=cv.subtract(img, gaussian_img)
unmasked_sharp=cv.add(img, mask)

filter_size = 15
median_img = cv.medianBlur(img, filter_size)

plt.subplot(231)
plt.imshow(img, cmap="gray")

plt.subplot(232)
plt.imshow(box_img, cmap="gray")

plt.subplot(233)
plt.imshow(gaussian_img, cmap="gray")

plt.subplot(234)
plt.imshow(sharp_img, cmap="gray")

plt.subplot(235)
plt.imshow(unmasked_sharp, cmap="gray")

plt.subplot(236)
plt.imshow(median_img, cmap="gray")

plt.show()