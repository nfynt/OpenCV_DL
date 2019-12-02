import cv2
import numpy as np

def mouse_draw(events, x, y, flag, param):
    if events == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),25,(0,255,0),5)


img = cv2.imread("../DATA/dog_backpack.jpg")

cv2.namedWindow("image")
cv2.setMouseCallback("image",mouse_draw)

while True:
    cv2.imshow("image",img)

    k = cv2.waitKey(1) & 0xFF

    if k==27:
        break
    elif k==ord('s'):
        cv2.imwrite("snap.jpg",img)

cv2.destroyAllWindows()