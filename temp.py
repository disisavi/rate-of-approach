import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy

def area(vs):
        x=vs[:,0]
        y=vs[:,1]
        area=0.5*np.sum(y[:-1]*np.diff(x) - x[:-1]*np.diff(y))
        return np.abs(area)


def showImage(frame):
        cv2.imshow('image',frame)

def getCountours(frame):
        image = copy.copy(frame)
        frame = cv2.blur(frame,(3,3))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # _, frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # frame =  cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

        frame = cv2.Canny(frame,100,200)

        contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for (i, c) in enumerate(contours):
                tl = c[:,0,:] 
                area(tl)
                # print("i = ",i,"  ",tl.shape, "- Area -- ", area(tl))

        print(len(contours))
        cv2.drawContours(image, contours, -1, (0,255,0), 1)
        showImage(image)


def showVideo(videoName):
        locaiton = '../BDDA/test/camera_videos/'+videoName+'.mp4'
        cap = cv2.VideoCapture(locaiton)
        # cap = cv2.VideoCapture(0)
        if (cap.isOpened()== False): 
                print("Error opening video stream or file")
        while(cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()
                if ret == True:
                        # Display the resulting frame
                        getCountours(frame)

                        # Press Q on keyboard to  exit
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                                break
                else: 
                        break
        
        # When everything done, release the video capture object
        cap.release()
        
        # Closes all the frames
        cv2.destroyAllWindows()


videos = ['515','526','528']
for v in videos:
        showVideo(v)

# TODO:
#         1. Find the exact relation between rate of change of area and rate of approach 
#         2. Histogram equalisation for dark images 
#         3. Extract image from inside object in YOLO