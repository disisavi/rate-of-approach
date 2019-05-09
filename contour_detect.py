import numpy as np
import cv2
import copy
from obect_tracker import *


def calc_area(vs):
    x = vs[:, 0]
    y = vs[:, 1]
    area = 0.5 * np.sum(y[:-1] * np.diff(x) - x[:-1] * np.diff(y))
    return np.abs(area)


def calc_delta(object: ObjectDef):
    if object.old_area is None:
        object.rate_of_approach = -1
    else:
        dela = object.new_area - object.old_area
        relChange = dela / object.old_area
        object.rate_of_approach = relChange * frame_rate
        print(object.id, object.rate_of_approach)


def getCountours():
    for k, v in obj_Dict.items():
        # print("ID ", k)
        frame = v.frame
        image = copy.copy(frame)
        frame = cv2.blur(frame, (3, 3))
        # _, frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # frame =  cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

        frame = cv2.Canny(frame, 100, 200)

        contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        max_contour = -1
        area = -1
        for (i, c) in enumerate(contours):
            area_frame = c[:, 0, :]
            temp_area = calc_area(area_frame)
            if temp_area > area:
                area = temp_area

        if area > -1:
            v.old_area = v.new_area
            v.new_area = area
            calc_delta(v)
