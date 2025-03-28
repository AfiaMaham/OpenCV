import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("opencv/pic1.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb,cv.COLOR_BGR2RGB)
cv.imshow("img",img)
plt.imshow(rgb)
plt.show()
# cv.imshow("gray",gray)
# cv.imshow("hsv", hsv)
# cv.imshow("lab",lab)
cv.imshow("rgb",rgb)
cv.imshow("bgr",bgr)

cv.waitKey(0)
