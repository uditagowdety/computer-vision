#canny edge detection

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#step 1: read the grayscale image
# path=r"C:\Users\student\PycharmProjects\220962410_Udita\images\grayflower.jpg"
path=r"C:\Users\student\Downloads\sticks.png"

img=cv.imread(path,0)

#step 2: filter out noise with a gaussian blur
gaussian_filter=np.array([[1,2,1],
                          [2,4,2],
                          [1,2,1]])/16
blurred_img=cv.filter2D(img,-1,gaussian_filter)

plt.imshow(blurred_img,cmap="gray")
plt.title("blurred image")
plt.show()

edges = cv.Canny(blurred_img, threshold1=100, threshold2=200)

# Display the result
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')
plt.show()

#step 3.1: compute the x and y gradients using sobel operators
sobel_x=np.array([[1,0,-1],
                  [2,0,-2],
                  [1,0,-1]])

sobel_y=np.array([[1,2,1],
                  [0,0,0],
                  [-1,-2,-1]])

grad_x=cv.filter2D(blurred_img,-1,sobel_x)
grad_y=cv.filter2D(blurred_img,-1,sobel_y)

#step 3.2: calculate the gradient magnitude and angle
grad_mag=np.sqrt(grad_x**2+grad_y**2)
grad_angle=np.arctan2(grad_y,grad_x)*180.0/np.pi
grad_angle[grad_angle<0]+=180

plt.imshow(grad_mag,cmap="gray")
plt.title("gradient magnitudes")
plt.show()

plt.imshow(grad_angle, cmap="gray")
plt.title("Gradient Angles")
plt.show()

#step 4: thin the edges with non-max suppression
def non_max(magnitude, angle):
    height, width=magnitude.shape
    output=np.zeros_like(magnitude, dtype=np.uint8)
    angle=angle*np.pi/180.0

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Determine the direction of the gradient
            q = 255
            r = 255
            if (0 <= angle[i, j] < np.pi / 8) or (15 * np.pi / 8 <= angle[i, j] <= 2 * np.pi):
                q = magnitude[i, j + 1]
                r = magnitude[i, j - 1]
            elif (np.pi / 8 <= angle[i, j] < 3 * np.pi / 8):
                q = magnitude[i + 1, j - 1]
                r = magnitude[i - 1, j + 1]
            elif (3 * np.pi / 8 <= angle[i, j] < 5 * np.pi / 8):
                q = magnitude[i + 1, j]
                r = magnitude[i - 1, j]
            elif (5 * np.pi / 8 <= angle[i, j] < 7 * np.pi / 8):
                q = magnitude[i - 1, j - 1]
                r = magnitude[i + 1, j + 1]

            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                output[i, j] = magnitude[i, j]
            else:
                output[i, j] = 0

    return output


nms_img = non_max(grad_mag, grad_angle)

plt.imshow(nms_img, cmap="gray")
plt.title("Non-Max Suppression")
plt.show()

#step 5: double thresholding
def double_thresholding(image, low_threshold, high_threshold): #error somewhere here
    strong = 255
    weak = 75
    strong_edges = (image >= high_threshold)
    weak_edges = ((image >= low_threshold) & (image < high_threshold))

    result = np.zeros_like(image, dtype=np.uint8)
    result[strong_edges] = strong
    result[weak_edges] = weak

    return result


low_threshold = np.percentile(nms_img, 25)  # Example: 25th percentile of gradient magnitudes
high_threshold = np.percentile(nms_img, 75)  # Example: 75th percentile of gradient magnitudes

thresholded_img = double_thresholding(nms_img, low_threshold, high_threshold)

plt.imshow(thresholded_img, cmap="gray")
plt.title("Thresholded Image")
plt.show()

print("Thresholded Image min:", np.min(thresholded_img))
print("Thresholded Image max:", np.max(thresholded_img))

#step 6: hysteresis
def edge_tracking_by_hysteresis(image):
    height, width = image.shape
    strong = 255
    weak = 75

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if image[i, j] == weak:
                # Check if weak edge is connected to strong edge
                if ((image[i + 1, j] == strong) or (image[i - 1, j] == strong) or
                        (image[i, j + 1] == strong) or (image[i, j - 1] == strong) or
                        (image[i + 1, j + 1] == strong) or (image[i - 1, j - 1] == strong) or
                        (image[i + 1, j - 1] == strong) or (image[i - 1, j + 1] == strong)):
                    image[i, j] = strong
                else:
                    image[i, j] = 0

    return image


final_edges = edge_tracking_by_hysteresis(thresholded_img)

#step 7: show the final edges
import matplotlib.pyplot as plt

# Display the edge-detected image
plt.imshow(final_edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')
plt.show()
