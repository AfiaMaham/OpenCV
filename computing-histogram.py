import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

blank = np.zeros((300,300),np.uint8)
img = cv.imread("opencv/boston.jpg")
resize = cv.resize(img,(300,300))
# gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
circle = cv.circle(blank.copy(),(30,30),60,[256],cv.FILLED)
masked = cv.bitwise_and(resize,resize,mask=circle)


# hist = cv.calcHist([gray],[0],mask,[256],(0,256))
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([resize],[i],circle,[256],[0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
plt.show()

# cv.imshow("gray",gray)
cv.imshow("masked", masked)
cv.waitKey(0)


