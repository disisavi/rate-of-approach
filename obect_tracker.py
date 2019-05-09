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
        self.update_time()

    def update_time(self):
        self.timeStamp = int(round(time.time() * 1000))
        # print("Time updated for object", self.id, self.timeStamp)


obj_Dict: Dict[int, ObjectDef] = {}
frame_rate: int = -1