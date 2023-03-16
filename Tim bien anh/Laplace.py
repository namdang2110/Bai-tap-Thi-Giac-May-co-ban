import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Pictures\\Lenna.png", 0)
img = cv2.resize(img, (400,400))

def h2(img, x, y):
    return ((-1) * img[x - 1, y - 1] + (-1) * img[x - 1, y] + (-1) * img[x - 1, y + 1]
            + (-1) * img[x, y - 1] + 8 * img[x, y] + (-1) * img[x, y + 1]
            + (-1) * img[x + 1, y - 1] + (-1) * img[x + 1, y] + (-1) * img[x + 1, y + 1])

def laplace(img):
    w, h = img.shape
    img_new = np.zeros([h, w])

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            sum = h2(img, i, j)
            if sum > 255:
                sum = 255
            elif sum < 0:
                sum = 0        
            img_new[i, j] = sum 
            img_new = img_new.astype(np.uint8)
    return img_new

laplace = laplace(img)

cv2.imshow("Anh goc", img)
cv2.imshow("Laplace", laplace)

cv2.waitKey()
cv2.destroyAllWindows()