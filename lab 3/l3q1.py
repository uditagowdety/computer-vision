#good old histogram equalisation
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img=cv.imread(path,0)

hist,bins=np.histogram(img.flatten(),256,[0,256])

cdf=hist.cumsum()
cdf_normal=cdf*float(hist.max()/cdf.max())

plt.subplot(131)
plt.imshow(img,cmap="gray")

plt.subplot(132)
plt.plot(cdf_normal, color="b")
plt.hist(img.flatten(), 256,[0,256], color="r")
plt.xlim([0,256])

plt.subplot(133)
equ=cv.equalizeHist(img)
plt.imshow(equ, cmap="gray")
plt.show()