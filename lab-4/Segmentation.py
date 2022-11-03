import cv2

img = cv2.imread('images/dog.jpg')

print('original shape : ', img.shape)

resized_img = cv2.resize(img, (350, 200))

cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.imshow('resized image', resized_img)
cv2.waitKey(0)