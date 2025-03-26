from pickletools import uint8

import cv2 as cv
import numpy as np


# -------------------- ( 1 ) ----------------------------------
# img = cv.imread("opencv/pic2.jpg")
# blank = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray,(5,5),0)
# canny = cv.Canny(blur,125,175)
# contours, herarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(blank,contours,-1,(0,0,255),1)
# cv.imshow("img", img)
# cv.imshow("blank", blank)
# cv.imshow("gray", gray)
# cv.imshow("canny", canny)
# cv.waitKey(0)

# ----------------------- ( 2 ) -------------------------------------

img = cv.imread("opencv/pic2.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
ret , thre = cv.threshold(gray,125,255,cv.THRESH_BINARY)
contours, herarchy = cv.findContours(thre,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank,contours,-1, (0,0,255),1)
cv.imshow("thre", thre)
cv.imshow("img", img)
cv.imshow("blank", blank)
cv.waitKey(0)