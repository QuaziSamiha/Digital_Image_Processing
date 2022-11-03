import cv2
import numpy as np

# creating an image usign numpy
img = np.zeros((512, 512, 3))

# ractangle
cv2.rectangle(img, pt1=(100, 100), pt2=(300, 300),
              color=(255, 0, 0), thickness=3)
# filled ractangle
# cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness=-1)

# circle
# cv2.circle(img, center=(100, 400), radius=40, color=(0, 0, 255), thickness=3)
# filled circle
cv2.circle(img, center=(100, 400), radius=40, color=(0, 0, 255), thickness=-1)

# line
cv2.line(img, pt1=(0, 0), pt2=(512, 512), color=(0, 255, 0), thickness=2)

# text
cv2.putText(img, org=(400, 350), fontScale=1, color=(255, 200), thickness=1,
            lineType=cv2.LINE_AA, text='hello', fontFace=cv2.FONT_ITALIC)

cv2.imshow("Created Black Image", img)
cv2.waitKey(0)
