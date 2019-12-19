import numpy as np
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib import cm

def create_color(i):
    x = np.array(cm.tab10(i))[:3]*255
    return tuple(x)

colors=[]

n_markers=10
curr_marker=1
marker_updated=False

for i in range(n_markers):
    colors.append(create_color(i))
    
# print(colors)

road = cv2.imread("../DATA/road_image.jpg")
road_copy = road.copy()
segments = np.zeros(road.shape,dtype=np.uint8)
marker_image = np.zeros(road.shape[:2],dtype=np.int32)

def mouse_callback(event, x, y, flat, param):
    global marker_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(road_copy,(x,y),10,colors[curr_marker],-1)
        cv2.circle(marker_image,(x,y),10,(curr_marker),-1)
        
        marker_updated=True

cv2.namedWindow("Road Image")
cv2.setMouseCallback("Road Image",mouse_callback)


while True:
    
    cv2.imshow("Road Image",road_copy)
    cv2.imshow("Watershed segments",segments)
    
    k = cv2.waitKey(1)
    
    if k==27:
        break
    
    elif k == ord('c'):
        road_copy = road.copy()
        segments = np.zeros(road.shape(),dtype=np.uint8)
        marker_image = np.zeros(road.shape[:2],dtype=np.int32)
        
    elif k>0 and chr(k).isdigit():
        curr_marker = int(chr(k))
        
    
    if marker_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)
        
        segments = np.zeros(road.shape,dtype=np.uint8)
        
        for ci in range(n_markers):
            segments[marker_image_copy==(ci)]=colors[ci]
            
        marker_updated=False
        

cv2.destroyAllWindows()
