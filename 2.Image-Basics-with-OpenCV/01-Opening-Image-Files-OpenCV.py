import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    
    #instead of 27 we can use ord('q') for any other key press event
    if cv2.waitKey(1) & 0xFF == 27:
        break;
        
cv2.destroyAllWindows()