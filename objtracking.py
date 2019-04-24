from scipy.spatial.distance import cityblock


# The code theoretically calculates centroids and reassigns centroids to object IDs
# object IDs are calculated but deallocation and *proper* assignment is a work in progress and not fully complete if you take a look ay it
# x1,y1,x2,y2 are the bounding box coordinate values
# read at your own risk (sleep deprived untested code)
class ObjTracking:
    def __init__(self):
        self.obj_list = []
        self.old_centroids = []
        self.curr_centroids = []
        self.id_counter = -1
        self.obj_ids = dict
        {}

    def centroid(x1, y1, x2, y2):
        return ((x1 + x2) // 2, (y1 + y2) // 2)

    def calc_centroid(self, obj_list):
        #what is frame in the below statement?
        for box in frame:
            self.curr_centroids.append(centroid(box.x1, box.y1, box.x2, box.y2))
            old_centroids = get_old_centroids()
            min_cityblock = sys.maxsize
            min_index = sys.maxsize
        for oc_i in len(self.curr_centroids):
            oc = self.curr_centroids[oc_i]
            for cc_i in len(old_centroids):
                cc = old_centroids[cc_i]
                if (cityblock(cc, oc) < min_cityblock):
                    min_cityblock = cityblock(cc, oc)
                    min_index = cc_i
            if (min_index != -1):
                self.curr_centroids[oc_i] = old_centroids[min_index].obj_id
            else:
                self.obj_ids[self.assign_obj_id()] = self.curr_centroid[oc_i]
        old_centroids = self.curr_centroids

    def assign_obj_id(self, count=0):

        def id_check():
            if (self.id_counter < 100):
                self.id_counter += 1
                if self.check_if_free(self.id_counter):
                    return self.id_counter
                else:
                    self.assign_obj_id(count)
            else:
                self.id_counter = 0
                if self.check_if_free(self.id_counter):
                    return self.id_counter
                else:
                    self.assign_obj_id(count)

        count += 1
        return id_check()

    def check_if_free(self, id):
        if self.obj_ids.get(id, -1) == -1:
            return True
        return False
