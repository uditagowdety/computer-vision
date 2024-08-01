import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path=r"C:\Users\student\PycharmProjects\220962410_Udita\lab 2\star.jpg"
img_bgr=cv.imread(path)
img=cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
img_gray=cv.imread(path,0)

blurred=cv.GaussianBlur(img_gray,(21,21),0)
(minval,maxval,minloc,maxloc)=cv.minMaxLoc(img_gray)

copied=img.copy()
cv.circle(copied, maxloc,50, (0, 0, 255), 2)

cv.imshow("brightest spot",copied)
cv.waitKey(0)
