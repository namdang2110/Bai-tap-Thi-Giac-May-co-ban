import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\Lenna.png", 0)
img = cv2.resize(img, (400,400))

blur = cv2.GaussianBlur(img,(5,5),0)

nguong_thap = 10
nguong_cao = 70

canny = cv2.Canny(blur,nguong_thap,nguong_cao)

cv2.imshow("Anh goc", img)
cv2.imshow("Canny", canny)

cv2.waitKey()
cv2.destroyAllWindows()