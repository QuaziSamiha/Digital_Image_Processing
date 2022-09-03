import imp
import numpy as np
import cv2

img = np.zeros((512, 512, 3))

while True:

    cv2.imshow('window', img)

# only way to close the window to press x 
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows