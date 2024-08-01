import cv2
import numpy as np

img_read=cv2.imread(r"C:\Users\student\Desktop\flower.jpg")

cv2.imshow('rgb flower',img_read)
cv2.waitKey(0)

b,g,r=cv2.split(img_read)
k=np.zeros_like(b)
b=cv2.merge([b,k,k])
g=cv2.merge([k,g,k])
r=cv2.merge([k,k,r])

cv2.imshow('blue',b)
cv2.imshow('red',r)
cv2.imshow('green',g)

cv2.waitKey(0)
cv2.destroyAllWindows()
