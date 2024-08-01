import cv2

img_gray=cv2.imread(r'C:\Users\student\Desktop\flower.jpg',1)

cv2.imshow('grayscale image',img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite(r'C:\Users\student\Desktop\grayflower.jpg',img_gray)