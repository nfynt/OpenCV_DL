import cv2
import numpy as np

empty_img = np.zeros(shape=(512,512,3),dtype=np.int8)

cntr=0;


while True:
    start_x = 50*cntr
    start_y = 50*cntr
    col = [np.random.randint(10,200),np.random.randint(10,150),np.random.randint(10,190)]
    if cntr==0:
        frame = np.copy(empty_img)
        #cv2.rectangle(empty_img,pt1=(start_x,start_y),pt2=(512 - start_x, 512 - start_y),color=col,thickness=10)
    else:
        frame = cv2.rectangle(frame,pt1=(start_x,start_y),pt2=(512 - start_x, 512 - start_y),color=col,thickness=10)
    
    cv2.circle(frame,center=(256,256),radius=10*cntr,color=(135,np.random.randint(50,150),50),thickness=5)
    
    cntr += 1
    if cntr==4:
        cntr=0
    
    #font = cv2.FONT_HERSHEY_DUPLEX
    #cv2.putText(empty_img,text=str(cntr),org=(10,40),fontFace=font,fontScale=1,color=(255,20,25),thickness=2,lineType=cv2.LINE_AA)

    
    cv2.imshow("anim",frame)
   # cv2.waitKey(100)
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break

cv2.destroyAllWindows()