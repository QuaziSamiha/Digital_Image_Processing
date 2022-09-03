import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('images/chessboard.jfif')

cv2.imshow("Original", img)
cv2.waitKey(0)

# Affline Tranformation
rows, cols, ch = img.shape
pts1 = np.float32([[150, 150], [150, 150], [150, 150], [150, 150]])
pts2 = np.float32([[0, 125], [125, 125], [125, 0], [0, 0]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (100, 100))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
