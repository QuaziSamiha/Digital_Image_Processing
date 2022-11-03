import numpy as np
import cv2

img = cv2.imread('images/dog.jpg')

cv2.imshow("Original", img)
cv2.waitKey(0)

height, width = img.shape[:2]
# scaling by 2
res_z = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Scaled", res_z)
cv2.waitKey(0)
