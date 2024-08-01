import cv2

img=cv2.imread(r"C:\Users\student\Desktop\flower.jpg")
cv2.imshow('rgb flower',img)
cv2.waitKey(0)

new_dim=(200,300)
new_img=cv2.resize(img, new_dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow('resized flower',new_img)
cv2.waitKey(0)