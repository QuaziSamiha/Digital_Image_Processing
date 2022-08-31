import cv2
import numpy as np

# how to read an image

img = cv2.imread("images/dog.jpg")

print("Image Type : " , type(img))
print("Shape : " , img.shape)

cv2.imshow("window", img)
cv2.waitKey(0)