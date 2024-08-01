import cv2

img=cv2.imread(r"C:\Users\student\Desktop\flower.jpg")
cv2.imshow('rgb flower',img)
cv2.waitKey(0)

rot_img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotated flower',rot_img)
cv2.waitKey(0)
