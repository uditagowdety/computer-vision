import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img_bgr=cv.imread(path)
img=cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

gamma=0.5
gamma_corr=np.array(255*(img/255)**gamma, dtype=np.uint8)
cv.imwrite(r"C:\Users\student\PycharmProjects\220962410_Udita\images\gamma_flower.jpg",gamma_corr)

plt.subplot(121)
plt.title("original image")
plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.title("gamma transformed image")
plt.imshow(gamma_corr)
plt.xticks([])
plt.yticks([])

plt.show()