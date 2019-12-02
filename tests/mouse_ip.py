import cv2
import numpy as np

def draw_circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,100,20),-1)

img = np.zeros((512,512,3),np.uint8)

# pts = np.array([[100,100],[200,100],[150,50]],np.int8)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(npimg,[pts],True,(0,0,255),5)

cv2.namedWindow("mouse_input")
cv2.setMouseCallback("mouse_input",draw_circle)

while True:
    cv2.imshow("mouse_input",img)

    k = cv2.waitKey(1) & 0xFF

    if k==27:
        break

    if k == ord('s'):
        cv2.imwrite("temp.jpg",img)

cv2.destroyAllWindows()