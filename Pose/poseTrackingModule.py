import cv2 as cv
import mediapipe as mp
import time

class PoseDetector():
    def __init__(self,mode=False,modelComp=1,smooth=True,enableSeg=False,smoothSeg=True,minCon=0.5,traCon=0.5):
        self.mode = mode
        self.modelComp = modelComp
        self.smooth = smooth
        self.enableSeg = enableSeg
        self.smoothSeg = smoothSeg
        self.minCon = minCon
        self.traCon = traCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.modelComp,self.smooth,self.enableSeg,self.smoothSeg,self.minCon,self.traCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self,img,draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.result = self.pose.process(imgRGB)
        if self.result.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.result.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self,img,draw=True):
        lmsList = []
        poseLandmarks = self.result.pose_landmarks
        for id, lms in enumerate(poseLandmarks.landmark):
            h,w,c = img.shape
            cx, cy = int(lms.x*w), int(lms.y*h)
            lmsList.append([id,cx,cy])
            if draw:
                cv.circle(img,(cx,cy),3,(255,0,0),cv.FILLED)
        return lmsList
def main():
    cap = cv.VideoCapture(0)
    ctime = 0
    ptime = 0
    lmsList = []
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmsList = detector.findPosition(img)
        if len(lmsList) != 0:
            print(lmsList[0])
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv.putText(img,str(int(fps)),(10,50),cv.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)

        cv.imshow("Video", img)
        if cv.waitKey(1) & 0xff == ord("a"):
            break

if __name__ == "__main__":
    main()