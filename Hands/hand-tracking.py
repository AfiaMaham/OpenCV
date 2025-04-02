import cv2 as cv
import mediapipe as mp
import time

mpHands = mp.solutions.hands
mpDraw  =mp.solutions.drawing_utils
hand = mpHands.Hands()
cap = cv.VideoCapture(0)
ctime = 0
ptime = 0
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result = hand.process(imgRGB)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            for id,lms in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lms.x*w), int(lms.y*h)
                if id == 0:
                    cv.circle(img,(cx,cy),30,(255,0,0),cv.FILLED)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(img,str(int(fps)),(30,40),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),5)

    cv.imshow("Camera", img)
    if cv.waitKey(1) & 0xff == ord("a"):
        break
