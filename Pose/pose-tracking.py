import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
ctime = 0
ptime = 0
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
        poseLandmarks = result.pose_landmarks
        for id, lms in enumerate(poseLandmarks.landmark):
            h,w,c = img.shape
            cx, cy = int(lms.x*w), int(lms.y*h)
            if id == 0:
                cv.circle(img,(cx,cy),3,(255,0,0),cv.FILLED)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(img,str(int(fps)),(10,50),cv.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)

    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xff == ord("a"):
        break