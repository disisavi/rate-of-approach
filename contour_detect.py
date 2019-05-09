import numpy as np
import cv2
import copy


def area(vs):
    x = vs[:, 0]
    y = vs[:, 1]
    area = 0.5 * np.sum(y[:-1] * np.diff(x) - x[:-1] * np.diff(y))
    return np.abs(area)


def showImage(frame):
    cv2.imshow('image', frame)


def getCountours(frame):
    image = copy.copy(frame)
    frame = cv2.blur(frame, (3, 3))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # _, frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # frame =  cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    frame = cv2.Canny(frame, 100, 200)

    contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for (i, c) in enumerate(contours):
        tl = c[:, 0, :]
        # area(tl)
        print("i = ", i, "  ", tl.shape, "- Area -- ", area(tl))
