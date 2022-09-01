import cv2

img = cv2.imread("images/dog.jpg")

img_resized = cv2.resize(img, (500, 300))

# saving the resized image
cv2.imwrite('dog_resized.jpg', img_resized)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.imshow("Resized Image", img_resized)
cv2.waitKey(0)
