import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\coco.jpg", 0)

kernel = np.ones((3,3),np.float32)/9
blur = cv2.filter2D(img,-1,kernel)

cv2.imshow("Anh goc", img)
cv2.imshow("Blur", blur)

cv2.waitKey()
cv2.destroyAllWindows()