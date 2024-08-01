import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img_bgr=cv.imread(path)
img=cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

def scale(val, oldmin, oldmax, newmin, newmax):
    if (0<=val<=oldmin):
        return (newmin/oldmin)*val
    if (oldmin<val<=newmin):
        return((newmax-newmin)/(oldmax-oldmin))*(val-oldmin)+newmin
    else:
        return((255-newmax)/(255-oldmax))*(val-oldmax)+newmin


scale_img=np.vectorize(scale)
contrast=scale_img(img,20,180,0,200)

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