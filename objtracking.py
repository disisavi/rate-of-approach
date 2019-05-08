import sys
import time
from scipy.spatial.distance import cityblock


# tracks all the objects. Need to give it list of objects
class ObjectDef:
    def __init__(self, id, curr_centroid):
        self.id = id
        self.old_centroid = None
        self.curr_centroid = curr_centroid
        self.timeStamp = None
        self.update_time()

    def update_time(self):
        self.timeStamp = int(round(time.time() * 1000))
        # print("Time updated for object", self.id, self.timeStamp)


class ObjTracking:
    def __init__(self):
        self.id_counter = -1
        self.obj_ids = dict()

    def centroid(self, x1, y1, x2, y2):
        return (((x1 + x2) // 2), ((y1 + y2) // 2))

    def get_old_centroids(self):
        return [v.curr_centroid for k, v in obj_Dict.items()]

    def calc_centroid(self, box):
        # frame is the current frame being passed
        firstrun = False
        index = -1
        curr_centroids = self.centroid(box[0], box[1], box[2], box[3])
        old_centroids = self.get_old_centroids()
        if len(old_centroids) == 0:
            old_centroids = [curr_centroids]
            firstrun = True

        min_index = sys.maxsize
        min_cityblock = 200

        for oc_i in range(len(old_centroids)):
            oc = old_centroids[oc_i]
            man_distance = cityblock(curr_centroids, oc)
            # print(box)
            if (man_distance < min_cityblock):
                min_index = oc_i
                min_cityblock = man_distance
                # print("Min Found", min_cityblock)

        if firstrun or min_cityblock < 100:
            if firstrun:
                min_index = self.assign_obj_id()
                objectdef = ObjectDef(min_index, curr_centroids)
                obj_Dict[min_index] = objectdef

            # print("DB^^", min_cityblock)
            obj_Dict[min_index].old_centroid = obj_Dict[min_index].curr_centroid
            obj_Dict[min_index].curr_centroid = curr_centroids
            obj_Dict[min_index].update_time()

            index = min_index
            # print("DB!!", index, min_cityblock)
        else:
            index = self.assign_obj_id()
            objectdef = ObjectDef(index, curr_centroids)
            obj_Dict[index] = objectdef

        return index

    def assign_obj_id(self):
        def id_check():
            if self.id_counter < 100:
                self.id_counter += 1
                if len(obj_Dict) > 0:
                    if max(obj_Dict) < self.id_counter:
                        return self.id_counter
                    else:
                        return self.check_for_last_updated()
                else:
                    return self.id_counter
            else:
                return self.check_for_last_updated()
        returnValue = id_check()

        return returnValue

    def check_for_last_updated(self):

        minTime = int(round(time.time() * 1000))
        minkey = 101
        for k, v in obj_Dict.items():
            if v.timeStamp < minTime:
                minTime = v.timeStamp
                minkey = k

        return minkey


#
# obj = ObjTracking()
# obj.calc_centroid([22, 44, 11, 12])
# obj.calc_centroid, [35, 70, 12, 45]
# # print(obj.curr_centroids)
# print(obj.obj_ids)
# # print(obj.old_centroids)
# print("part2")
# obj.calc_centroid([[23, 45, 10, 13], [34, 69, 11, 46], [1, 2, 1, 3]])
# # print(obj.curr_centroids)
# print(obj.obj_ids)
from objectYolo import obj_Dict
