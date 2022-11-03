import cv2
import numpy as np

img = cv2.imread('images/dog.jpg')

print("Shape Before Resizing : ", img.shape)

# half of original image height and width
resized_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

print("Shape After Resizing : ", resized_img.shape)

cv2.imshow('window', resized_img)
cv2.waitKey(0)