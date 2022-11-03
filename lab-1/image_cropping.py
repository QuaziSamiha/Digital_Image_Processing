import cv2
import numpy as np

# how to read an image

img = cv2.imread("images/dog.jpg")

# height axis , width axis
cropped_img = img[100:300, 200:500]

cv2.imshow("window", cropped_img)
cv2.waitKey(0)

# origin starts from left top (0,0)
cropped_img2 = img[0:300, 0:200]
cv2.imshow("from Origin Height 300 and Width 200", cropped_img2)
cv2.waitKey(0)
