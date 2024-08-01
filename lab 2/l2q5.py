import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img_bgr=cv.imread(path,0)
img=cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)



plt.subplot(121)
plt.title("original image")
plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.title("contrast stretched image")
plt.imshow(contrast)
plt.xticks([])
plt.yticks([])

plt.show()