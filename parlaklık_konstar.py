#import required packages
import cv2
import numpy as np
#Read image
image = cv2.imread("kedi.jpg")

new_image = np.zeros(image.shape, image.dtype)

contrast = 3.0
bright = 2

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        for c in range(image.shape[2]):
            new_image[y,x,c] = np.clip(contrast*image[y,x,c] +bright, 0, 255)

cv2.imshow(image)

cv2.imshow(new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()