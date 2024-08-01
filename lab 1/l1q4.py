import cv2

img=cv2.imread(r"C:\Users\student\Desktop\flower.jpg")

img=cv2.rectangle(img, (50,10),(400,300),(0,0,255), 2)
cv2.imshow('rectangle', img)
cv2.waitKey(0)