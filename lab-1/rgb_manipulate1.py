import cv2
import numpy as np

# playing with rgb color channels

img = cv2.imread('images/dog.jpg')

# blue color making 0
img[:, :, 0] = 0 
# only combination of green and red

cv2.imshow('window', img)
cv2.waitKey(0)
