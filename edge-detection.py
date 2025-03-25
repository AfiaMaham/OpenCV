import cv2 as cv
import numpy as np
img = cv.imread("opencv/boston.jpg")
resize = cv.resize(img,(500,400))
gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
# --------------- (1) laplacian ------------
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))

# ------------(2) sobel------------
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combine = cv.bitwise_or(sobelx,sobely)
cv.imshow("combine",combine)

cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)

cv.imshow("lap",lap)
cv.imshow("resize",resize)
cv.waitKey(0)