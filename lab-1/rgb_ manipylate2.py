import cv2
import numpy as np

# playing with rgb color channels

img = cv2.imread('images/dog.jpg')

# eliminating greeen
# making green color 0 usign numpy 3d array
img[:, :, 1] = 0
# only combination of red and blue

cv2.imshow('window', img)
cv2.waitKey(0)

# elimination red
# making red color 0 usign numpy 3d array
img[:, :, 2] = 0
# only combination of green and blue

cv2.imshow('window', img)
cv2.waitKey(0)