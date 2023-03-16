import cv2
import numpy as np

anhgoc	= cv2.imread("C:\\Users\\Admin\\Pictures\\planet_glow-1.jpg")
anhxam = cv2.cvtColor(anhgoc, cv2.COLOR_BGR2GRAY)
lammoanh = cv2.medianBlur(anhxam, 5)
img = cv2.Canny(lammoanh,100,150)

circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
circles	= np.uint16(np.around(circles))

for	i in circles[0,:]:
	cv2.circle(anhgoc,(i[0],i[1]),i[2],(0,255,0),6)
	cv2.circle(anhgoc,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("Tim duong tron", anhgoc)
cv2.waitKey()
cv2.destroyAllWindows()