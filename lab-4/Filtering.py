import cv2

img = cv2.imread('images/dog.jpg')

cv2.imshow('Original Image', img)

cv2.waitKey(0)

cv2.imshow('resized', cv2.resize(img, (200, 200)))
cv2.waitKey(0)
