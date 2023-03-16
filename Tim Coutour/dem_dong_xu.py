import numpy as np
import cv2

img = cv2.imread("C:\\Users\\Admin\\Pictures\\cois.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11, 11), 0)

canny = cv2.Canny(blur, 30, 150, 3)

dilated = cv2.dilate(canny, (1,1), iterations = 2)

(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)

cv2.imshow("Ket qua", rgb)

print('So dong xu trong hinh : ', len(cnt))

cv2.waitKey(0)
cv2.destroyAllWindows()