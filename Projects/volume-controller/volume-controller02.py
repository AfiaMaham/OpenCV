import cv2 as cv
import numpy as np
import mediapipe as mp
import time
import handTrackingModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

range = volume.GetVolumeRange()
minVol = range[0]
maxVol = range[1]
ctime = 0
ptime = 0
lmList = []
cap = cv.VideoCapture(0)
detector = htm.handDetector()


while True:
    success, img = cap.read()
    img = detector.findHand(img)
    lmList = detector.findPosition(img,draw=False)

    cv.line(img, (119, 80), (493, 80), (100, 0, 0), 2)
    cv.putText(img, "Volume: ", (119, 120), cv.FONT_HERSHEY_SIMPLEX, 0.6, (100, 0, 0), 2)
    if len(lmList) != 0:
        indx , indy = lmList[8][1], lmList[8][2]
        cv.circle(img, (indx, indy), 15, (0, 255, 0), cv.FILLED)

        vol = int(np.interp(indx,[119, 493],[0,100]))
        cv.putText(img, f"{vol}%", (200, 120), cv.FONT_HERSHEY_SIMPLEX, 0.6, (100, 0, 0), 2)

        pycaw = int(np.interp(indx,  [119, 493],[minVol,maxVol]))
        print(pycaw, vol)
        volume.SetMasterVolumeLevel(pycaw, None)

        if indx >= 119 and indx <= 400:
            cv.circle(img,(indx,80),15,(0,100,0),cv.FILLED)
        elif indx <119:
            cv.circle(img,(119,80),15,(0,100,0),cv.FILLED)
        elif indx>400 and indx <=493:
            cv.circle(img,(indx,80),15,(0,0,100),cv.FILLED)
        elif indx > 493:
            cv.circle(img,(493,80),15,(0,0,100),cv.FILLED)


    else:
        cv.circle(img, (119,80), 15, (0, 100, 0), cv.FILLED)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(img,f"fps: {int(fps)}",(30,40),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,100),2)

    cv.imshow("Camera", img)
    if cv.waitKey(1) & 0xff == ord("a"):
        break