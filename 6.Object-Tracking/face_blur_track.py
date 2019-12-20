import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=15)
    
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,0,255),5)
        # print(x,y,w,h)

    return face_img

def first_face_rect(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=15)
    
    print(len(face_rects))
    
    if len(face_rects) > 0:
        return face_rects[0]
    tup = (0,0,0,0)
    return tup

def fix_contrast(img):
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:,:,2])

    img_eq = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
    return img_eq

def blur_region(img,rect):
    
    img_blur = img.copy()

    roi = img_blur[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]].copy()
    # roi = cv2.medianBlur(roi,ksize=5)
    roi = cv2.blur(roi,(17,17))

    img_blur[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]] = roi;

    return img_blur

def mouse_callback(event, x, y, flags, params):
    
    global track_feature
    global track_rect
    global tracker2
    global frame
    if event == cv2.EVENT_LBUTTONDOWN:
        track_feature=True
        track_rect = (x,y,40,40)
        tracker2 = cv2.TrackerMedianFlow_create()
        tracker2.init(frame,track_rect)

    if event == cv2.EVENT_RBUTTONDOWN:
        track_feature=False

track_feature = False
track_rect=(0,0,0,0)
cap = cv2.VideoCapture(1)
tracker = cv2.TrackerMedianFlow_create()
tracker2 = cv2.TrackerMedianFlow_create()
ret,frame = cap.read()
# frame = fix_contrast(frame)

rect = first_face_rect(frame)
# roi = frame[y:y+h,x:x+w].copy()
print(rect)
tracker.init(frame,tuple(rect))

cv2.namedWindow("Tracking")
cv2.setMouseCallback("Tracking",mouse_callback)


while True:
    
    ret,frame = cap.read()
    # frame = fix_contrast(frame)

    success,roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))
    
    if track_feature:
        succ,roi2 = tracker2.update(frame)
        (x2,y2,w2,h2) = tuple(map(int,roi2))
        if succ:
            cv2.circle(frame,(x2,y2),25,(0,0,255),4)

    if success:
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        frame = blur_region(frame,(x,y,w,h))
        cv2.putText(frame,"Tracking...",(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
    else:
        cv2.putText(frame,"Lost Tracking!",(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

    cv2.imshow("Tracking",frame)

    if 0xFF & cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
