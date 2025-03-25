import cv2 as cv
import numpy as np

img = cv.imread("opencv/boston.jpg")
resized = cv.resize(img,(550,450))
blank = np.zeros((resized.shape[0],resized.shape[1]),np.uint8)

b, g, r = cv.split(resized)
cv.imshow("resized",resized)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("b",blue)
cv.imshow("g",green)
cv.imshow("r",red)
merged = cv.merge((b,g,r))
# cv.imshow("merged",merged)
cv.waitKey(0)