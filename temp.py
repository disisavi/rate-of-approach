import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy

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
        image = copy.copy(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame,(7,7),0)
        # ret, frame = cv2.threshold(frame, 10, 255, 0)
        showImage(frame)
        edge = cv2.Canny(frame,100,200)
        showImage(edge)
        # imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for (i, c) in enumerate(contours):
                tl = c[:,0,:] 
                print("i = ",i,"  ",tl.shape, "- Area -- ", area(tl))

        
        print(len(contours))
        cv2.drawContours(image, contours, -1, (255,0,0), 2)
        showImage(image)


image = cv2.imread("test.jpg")
getCountours(image)

