import cv2 as cv
# 1. Calculate the histogram of an image then find out the threshold to segment the image.

img = cv.imread('images/th.JPEG', 0)

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)

cv.imshow('img', img)
cv.imshow('th1', th1)
cv.waitKey(0)
cv.destroyAllWindows()