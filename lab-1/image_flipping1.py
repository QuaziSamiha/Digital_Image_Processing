import cv2

img = cv2.imread("images/dog.jpg")

# flipped vertically
flipped_img = cv2.flip(img, 0)

# flipped horizontally
# flipped_img = cv2.flip(img, 1)

# flipped both horizontal and vertically
# flipped_img = cv2.flip(img, -1)

cv2.imshow("window", flipped_img)
cv2.waitKey(0)
