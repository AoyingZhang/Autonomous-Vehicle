import cv2
import numpy as np
import utlis #npm i utlis (no wifi rn)

def getLaneCurve(img):

    imgCopy = img.copy()

    imgThres = utlis.thresholding(img)

    h, w, c = img.shape
    points = utlis.valTrackbars() # must adjust once we can build the car and then adjust the portions we care about
    imgWarp = utlis.warpImg(imgThres, points, w, h)
    imgWarpPoints = utlis.drawPoints(imgCopy, points)

    cv2.imshow('Thres', imgThres)
    cv2.imshow('Warp', imgWarp)
    cv2.imshow('Warp Points', imgWarpPoints)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    intialTracbarVals = [110,208,0,480]
    utlis.initializeTrackbars(intialTracbarVals)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter = 0
        
        success, img = cap.read() # will get the image
        img = cv2.resize(img,(480,240)) # will resize the image we get
        getLaneCurve(img)
        cv2.waitKey(1)