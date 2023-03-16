import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\Lenna.png", 0)
img = cv2.resize(img, (400,400))

def hx_robert(img, x, y):
    return ((-1) * img[x , y] + img[x + 1, y + 1])

def hy_robert(img, x, y):
    return ((-1) * img[x, y + 1] + img[x + 1, y])

def robert(img):
    w, h = img.shape
    img_new = np.zeros([h, w])

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            m1 = hx_robert(img, i, j)
            m2 = hy_robert(img, i, j)
            sum = abs(m1) + abs(m2)
            if sum > 255:
                sum = 255
            elif sum < 0:
                sum = 0        
            img_new[i, j] = sum 
            img_new = img_new.astype(np.uint8)
    return img_new

robert = robert(img)

cv2.imshow("Anh goc", img)
cv2.imshow("Robert", robert)

cv2.waitKey()
cv2.destroyAllWindows()