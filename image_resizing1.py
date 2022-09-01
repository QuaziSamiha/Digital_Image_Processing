import cv2
import numpy as np

img = cv2.imread('images/dog.jpg')

print("Shape Before Resizing : ", img.shape)

img_resized = cv2.resize(img, (350, 300))

print("Shape After Resizing : ", img_resized.shape)

cv2.imshow("window", img_resized)
cv2.waitKey(0)
