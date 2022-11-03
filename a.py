import numpy as np
import cv2

img = np.zeros((512, 512, 1))
img.fill(255)
cv2.circle(img, center=(100, 400), radius=40, color=(0, 0, 255), thickness=-1)

cv2.imshow("Created Black Image", img)
cv2.waitKey(0)
