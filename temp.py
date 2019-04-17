import numpy as np
import cv2
import matplotlib.pyplot as plt

def area(vs):
        x=vs[:,0]
        y=vs[:,1]
        area=0.5*np.sum(y[:-1]*np.diff(x) - x[:-1]*np.diff(y))
        return np.abs(area)


def showImage(frame):
        cv2.imshow('image',frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def getCountours(frame):
        print("starting")
        frame = cv2.GaussianBlur(frame,(9,9),0)
        showImage(frame)
        print("meanShiftTime")
        edge = cv2.Canny(frame,100,200)
        showImage(edge)
        # imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(edge, 2, 255, 0)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for (i, c) in enumerate(contours):
                tl = c[:,0,:] 
                print("i = ",i,"  ",tl.shape, "- Area -- ", area(tl))

        
        print(len(contours))
        cv2.drawContours(frame, contours, -1, (0,255,0), 2)
        showImage(frame)


image = cv2.imread("test.jpg")
getCountours(image)

