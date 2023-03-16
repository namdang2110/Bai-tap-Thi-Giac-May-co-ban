import cv2

def highpass(img, sigma):
    return img - cv2.GaussianBlur(img, (0,0), sigma) + 127

img = cv2.imread("C:\\Users\\Admin\\Pictures\\coco.jpg", 0)
locthongcao = highpass(img, 3)

cv2.imshow("Anh goc", img)
cv2.imshow("Loc thong cao", locthongcao)

cv2.waitKey()
cv2.destroyAllWindows()