from calendar import c
import cv2

img = cv2.imread('images/dog.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('images/dog.jpg', 1) # colored
# img = cv2.imread('images/dog.jpg', 0) # gray scaled
cv2.imshow("GrayScale Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()