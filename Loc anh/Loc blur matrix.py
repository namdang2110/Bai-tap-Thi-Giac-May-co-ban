import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\coco.jpg", 0)
img = cv2.resize(img, (400,400))

def tichchap(img, matran):
    w, h = img.shape
    img_new = np.zeros([h, w])
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            temp = ( img[i - 1, j - 1] * matran[0, 0] + img[i - 1, j] * matran[0, 1] + img[i - 1, j + 1] * matran[0, 2]\
                   + img[i, j - 1]     * matran[1, 0] + img[i, j] * matran[1, 1] + img[i, j + 1]     * matran[1, 2]\
                   + img[i + 1, j - 1] * matran[2, 0] + img[i + 1, j]     * matran[2, 1] + img[i + 1, j + 1] * matran[2, 2] )
            img_new[i, j] = temp 
            img_new = img_new.astype(np.uint8)
    return img_new

blur = np.array((
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
), dtype=float)

loctrungbinh = tichchap(img, blur)

cv2.imshow("Anh goc", img)
cv2.imshow("Blur", loctrungbinh)

cv2.waitKey()
cv2.destroyAllWindows()