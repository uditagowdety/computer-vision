#iterative global image thresholding

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path=r"C:\Users\student\PycharmProjects\220962410_Udita\images\gray.png"
img=cv.imread(path,0)

hist,bins=np.histogram(img.flatten(),256,[0,256])

plt.bar(bins[:-1],hist, width=1, color="gray")
plt.show()

height,width=img.shape
binary_img=np.zeros_like(img, dtype=np.uint8)
episodes=10
tolerance=0.5

threshold=np.mean(img)
print(threshold)

# for i in range(height):
#     for j in range(width):
#         if img[i][j] >= init_threshold:
#             binary_img[i][j] = 255
#         else:
#             binary_img[i][j] = 0
#
# cv.imshow("initial threshold image", binary_img)
# cv.waitKey(0)

for episode in range(episodes):
    # for i in range(height):
    #     for j in range(width):
    #         if img[i][j]>=threshold:
    #             binary_img[i][j]=255
    #         else:
    #             binary_img[i][j]=0

    binary_img = np.where(img >= threshold, 255, 0).astype(np.uint8)

    foreground=img[img>=threshold]
    background=img[img<threshold]

    mean_fore=np.mean(foreground)
    mean_back=np.mean(background)

    new_threshold=(mean_fore+mean_back)/2

    if new_threshold-threshold<tolerance:
        print(f"converged after {episode} episodes")
        cv.imshow("iterative threshold image", binary_img)
        cv.waitKey(1000)
        break

    threshold=new_threshold

    cv.imshow("iterative threshold image", binary_img)
    cv.waitKey(1000)