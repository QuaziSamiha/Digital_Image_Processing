import numpy as np
import cv2

img = cv2.imread('images/dog.jpg')

cv2.imshow("Original", img)
cv2.waitKey(0)

# translation
rows, cols, _ = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Translated", dst)
cv2.waitKey(0)
