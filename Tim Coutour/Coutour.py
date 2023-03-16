import cv2 as cv

img = cv.imread("C:\\Users\\Admin\\Pictures\\bien_so_xe.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (255,0,0), 3)

cv.imshow("anh ket qua",img)

cv.waitKey(0)
cv.destroyAllWindows()