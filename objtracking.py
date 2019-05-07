import sys

from scipy.spatial.distance import cityblock
<<<<<<< HEAD
#Old centroids are being updated but new centroids on subsequent runs arre not being updated due to some stupid fault which isn't striking me rn
class ObjTracking:
	def __init__(self):
		self.obj_list=[]
		self.old_centroids=[]
		self.curr_centroids=[]
		self.id_counter=-1
		self.obj_ids=dict()
		self.first=True
	def centroid(self,x1,y1,x2,y2):
		return ((x1+x2)//2,(y1+y2)//2)
	def get_old_centroids(self):
		return self.old_centroids
	def calc_centroid(self,frame):
		#frame is the current frame being passed
		self.curr_centroids=[]
		for box in frame:
			self.curr_centroids.append(self.centroid(box[0],box[1],box[2],box[3]))
			self.old_centroids=self.get_old_centroids()
		if self.first:
			self.first=False
			self.old_centroids=self.curr_centroids
		for oc_i in range(len(self.old_centroids)):
			min_index=sys.maxsize
			min_cityblock=sys.maxsize
			oc=self.old_centroids[oc_i]
			if(len(self.curr_centroids)!=0):
				print(self.curr_centroids)
				for cc_i in range(len(self.curr_centroids)):
					cc=self.curr_centroids[cc_i]
					if(cityblock(cc,oc)<min_cityblock):
						min_cityblock=cityblock(cc,oc)
						min_index=cc_i
			if(min_index!=sys.maxsize):
				#self.curr_centroids[oc_i]=min_index
				#print(oc_i)
				self.obj_ids[min_index]=self.curr_centroids[min_index]
			else:
				print("Enter")
				self.obj_ids[self.assign_obj_id()]=self.old_centroids[oc_i]
		self.old_centroids=self.curr_centroids

	def assign_obj_id(self):
		if(self.id_counter<100):
			self.id_counter+=1
			return self.id_counter
		else:
			for i in range(1,100):
				if(obj_ids.get(i,-1)==-1):
					obj_ids[i]=1
					return i

obj=ObjTracking()
obj.calc_centroid([[22,44,11,12],[35,70,12,45]])
#print(obj.curr_centroids)
print(obj.obj_ids)
#print(obj.old_centroids)
obj.calc_centroid([[23,45,10,13],[34,69,11,46],[1,2,1,3]])
#print(obj.curr_centroids)
print(obj.obj_ids)			
	
				
=======


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
>>>>>>> 8c47e63cfa22c3d78bf258f6278a29d8ba5dcec5
