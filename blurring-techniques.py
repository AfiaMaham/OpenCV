import cv2 as cv

img = cv.imread("opencv/boston.jpg")
resized = cv.resize(img, (530,400))
averageBlur = cv.blur(resized,(5,5))
gaussianBlur = cv.GaussianBlur(resized,(5,5),0)
medianBlur = cv.medianBlur(resized,5)
bilateralBlur = cv.bilateralFilter(resized,5,20,30)
cv.imshow("resized",resized)
cv.imshow("averageBlur",averageBlur)
cv.imshow("gaussianBlur",gaussianBlur)
cv.imshow("medianBlur",medianBlur)
cv.imshow("bilateralBlur",bilateralBlur)



cv.waitKey(0)