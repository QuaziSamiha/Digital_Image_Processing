import cv2
import numpy as np

# how to read an image

img = cv2.imread("images/dog.jpg")

print("Image Type : " , type(img))
print("Shape : " , img.shape)

cv2.imshow("window", img)
cv2.waitKey(0)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("window", img_gray)
cv2.waitKey(0)