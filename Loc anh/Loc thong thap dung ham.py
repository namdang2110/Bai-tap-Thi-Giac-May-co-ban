import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\coco.jpg", 0)
#img = cv2.resize(img, (400,400))

blur = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("Anh goc", img)
cv2.imshow("Loc thong thap", blur)

cv2.waitKey()
cv2.destroyAllWindows()