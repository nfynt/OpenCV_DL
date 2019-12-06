import cv2

# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked=True
        center = (x,y)

    if event == cv2.EVENT_LBUTTONUP:
        clicked=False
        
    if clicked:
        if event == cv2.EVENT_MOUSEMOVE:
            center = (x,y)

        
# Global vars
center = (0,0)
clicked = False


cap = cv2.VideoCapture(0)

cv2.namedWindow("Video");
# Bind draw_rectangle function to mouse cliks
cv2.setMouseCallback("Video",draw_circle)


while True:
    
    ret,frame = cap.read()

    if clicked:
        cv2.circle(frame,center=center,radius=30,color=(0,0,255),thickness=-1)
        
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
   

cap.release()
cv2.destroyAllWindows()
