import cv2
import numpy as np
import utlis #npm i utlis (no wifi rn)

def getLaneCurve(img):
    imgThres = utlis.thresholding(img)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read() # will get the image
        img = cv2.resize(img,(640,480)) # will resize the image we get
        getLaneCurve(img)
        cv2.waitKey(1)