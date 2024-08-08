#image negatives
#implement log transform: s=clog(1+r)
#power law transform: s=cr^g
#contrast stretching (point1, point2, decide which intensities to be stretched)
#gray level slicing
#bright spot detection
import cv2 as cv
import matplotlib.pyplot as plt

path=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
img=cv.imread(path)
img_rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
neg=abs(255-img_rgb)
cv.imwrite(r"C:\Users\student\PycharmProjects\220962410_Udita\images\neg_flower.jpg", neg)

titles=["original image", "negative image"]
images=[img_rgb, neg]

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