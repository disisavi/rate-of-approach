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
    frame_rate = get_frame_rate()
    if object.old_area is None or object.old_area == 0:
        object.rate_of_approach = -1
    else:
        dela = object.new_area - object.old_area
        relChange = dela / object.old_area
        object.rate_of_approach = relChange * frame_rate
        if object.rate_of_approach != 0:
            object.timetoCollision = relChange / frame_rate
            if object.id is 1:
                print(object.id, object.rate_of_approach, object.timetoCollision)
    # print("DEBUG D3 -- Delta ends", object.id)


def showImage(frame):
    cv2.imshow('image', frame)


def getCountours(debug=False, boundingBoxMode=False):
    if not boundingBoxMode:
        for k, v in obj_Dict.items():
            # print("ID ", k)
            frame = v.frame
            x, y, _ = frame.shape
            if x == 0 or y == 0:
                v.rate_of_approach = 0
                break
            image = copy.copy(frame)
            frame = cv2.blur(frame, (1, 1))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.Canny(frame, 100, 200)
            # image = copy.copy(frame)

            contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            area = -1
            index = -1
            for (i, c) in enumerate(contours):
                area_frame = c[:, 0, :]
                temp_area = calc_area(area_frame)
                if temp_area > area:
                    area = temp_area
                    index = i

            if area > -1:
                v.old_area = v.new_area
                v.new_area = area
                calc_delta(v)
            if debug:
                if v.id == 1:
                    # sift = cv2.xfeatures2d.SIFT_create()
                    # (kps, descs) = sift.detectAndCompute(image, None)
                    # print("# kps: {}, descriptors: {}".format(len(kps), descs.shape))
                    cv2.drawContours(image, contours, index, (0, 255, 0), 1)
                    showImage(image)
    else:
        for k, v in obj_Dict.items():
            frame = v.frame
            x, y, _ = frame.shape
            area = x * y
            v.old_area = v.new_area
            v.new_area = area
            calc_delta(v)
            if debug:
                if v.id == 1:
                    showImage(frame)
