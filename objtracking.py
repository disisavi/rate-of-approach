import sys
from scipy.spatial.distance import cityblock
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
	
				
