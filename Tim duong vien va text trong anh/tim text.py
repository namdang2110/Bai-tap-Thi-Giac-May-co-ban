import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\text.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = cv2.Sobel(gray, -1, 1,0, ksize=3, scale=1)
y = cv2.Sobel(gray, -1, 0,1, ksize=3, scale=1)

absx= cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)
sobel = cv2.addWeighted(absx, 0.5, absy, 0.5,0)

ret, thresh = cv2.threshold(sobel, 127, 255, 0)

kernel = np.ones((19,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)

contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#findcoutours(anh nguon, che do truy xuat duong vien, phuong phap xap xi duong vien)

for i in contours:
    x,y,w,h = cv2.boundingRect(i)
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('sobel', sobel)
cv2.imshow('threshold', thresh)
cv2.imshow('opening', opening)
cv2.imshow('ket qua', img)

cv2.waitKey(0)
cv2.destroyAllWindows()