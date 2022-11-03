import numpy as np
import cv2

img = cv2.imread('images/dog.jpg')

cv2.imshow("Original", img)
cv2.waitKey(0)

# rotation
rows, cols, _ = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Rotated", dst)
cv2.waitKey(0)
