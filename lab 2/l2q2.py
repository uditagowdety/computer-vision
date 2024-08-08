import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img_rgb=cv.imread(path)
img=cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)
img_asfloat=img.astype(np.float32)
c=255/(np.log(1+np.max(img_asfloat)))
log=c*np.log(1+img_asfloat)

log=np.array(log,dtype=np.uint8)
newpath=r"C:\Users\student\PycharmProjects\220962410_Udita\images\log_flower.jpg"
cv.imwrite(newpath,log)

titles=["original image", "log transformed image"]
images=[img, log]

plt.subplot(121)
plt.title(titles[0])
plt.imshow(images[0])
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.title(titles[1])
plt.imshow(images[1])
plt.xticks([])
plt.yticks([])

plt.show()