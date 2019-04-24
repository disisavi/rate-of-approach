from scipy.spatial.distance import cityblock
#The code theoretically calculates centroids and reassigns centroids to object IDs
#object IDs are calculated but deallocation and *proper* assignment is a work in progress and not fully complete if you take a look ay it
#x1,y1,x2,y2 are the bounding box coordinate values
#read at your own risk (sleep deprived untested code)
class ObjTracking:
	def __init__(self):
		self.obj_list=[]
		self.old_centroids=[]
		self.curr_centroids=[]
		self.id_counter=-1
		self.obj_ids=dict{}
	
	def centroid(x1,y1,x2,y2):
		return ((x1+x2)//2,(y1+y2)//2)

	def calc_centroid(obj_list):
		for box in frame:
			curr_centroids.append(centroid(box.x1,box.y1,box.x2,box.y2))
			old_centroids=get_old_centroids()
			min_cityblock=sys.maxsize
			min_index=sys.maxsize
		for oc_i in len(curr_centroids):
			oc=curr_centroids[oc_i]
			for cc_i in len(old_centroids):
				cc=old_centroids[cc_i]
				if(cityblock(cc,oc)<min_cityblock):
					min_cityblock=cityblock(cc,oc)
					min_index=cc_i
			if(min_index!=-1):
				curr_centroids[oc_i]=old_centroids[min_index].obj_id
			else:
				self.obj_ids[assign_obj_id()]=curr_centroid[oc_i]
		old_centroids=curr_centroids

	def assign_obj_id():
		if(self.id_counter<100):
			self.id_counter+=1
			return self.id_counter
		else:
			for i in range(1,100):
				if(obj_ids.get(i,-1)==-1):
					obj_ids[i]=1
					return i

			
		
				
