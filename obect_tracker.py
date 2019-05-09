"""
Contains the Obect defintion and the dictionary of objects which all the other file will need to import to know the dict of objects
"""
import time
from typing import Dict, Any


class ObjectDef:
    def __init__(self, id, curr_centroid):
        self.id = id
        self.old_centroid = None
        self.curr_centroid = curr_centroid
        self.timeStamp = None
        self.old_area = None
        self.new_area = None
        self.delta = None
        self.rate_of_approach = None
        self.frame = None
        self.timetoCollision = None
        self.update_time()

    def update_time(self):
        self.timeStamp = int(round(time.time() * 1000))


obj_Dict: Dict[int, ObjectDef] = {}
frame_rate = -1


def set_frame_rate(rate: float):
    global frame_rate
    frame_rate = rate

def get_frame_rate():
    global frame_rate
    return frame_rate