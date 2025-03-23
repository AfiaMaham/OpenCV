import cv2 as cv
import numpy as np

blank = np.zeros([400,400],np.uint8)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,cv.FILLED)
circle = cv.circle(blank.copy(),(200,200),180,(255,255,255),cv.FILLED)
cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)
AND = cv.bitwise_and(rectangle,circle)
cv.imshow("AND",AND)
OR = cv.bitwise_or(rectangle,circle)
cv.imshow("OR",OR)
XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",XOR)
NOT = cv.bitwise_not(XOR)
cv.imshow("NOT",NOT)
cv.waitKey(0)

