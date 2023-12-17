import cv2
import numpy as np
ASPECT_RATIO = (500,707)
pts2 = np.float32([[0,0],[ASPECT_RATIO[1],0],[0,ASPECT_RATIO[0]],[ASPECT_RATIO[1],ASPECT_RATIO[0]]])
pointIndex = 0
secondpointIndex = 0
pts = [(0,0),(0,0),(0,0),(0,0)]

secondPts = [(0,0),(0,0),(0,0),(0,0)]
#myWhiteBoard = Camera()
def draw_circle(event,x,y,flags,param):
    img = cv2.imread('Image_1.png')
    global pointIndex
    global pts
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        pts[pointIndex] = (x,y)
        pointIndex = pointIndex + 1
def selectFourPoints():
    img = cv2.imread('Image_1.png')
    global pointIndex
    while(pointIndex != 4):
        cv2.imshow('image',img)
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
            return False
    return True
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

if selectFourPoints():
    print("Point One Selected")
def draw_circle(event,x,y,flags,param):
    img = cv2.imread('OUTPUT_IMG.png')
    global secondpointIndex
    global secondPts
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        secondPts[secondpointIndex] = (x,y)
        secondpointIndex = secondpointIndex + 1
def selectFourPoints():
    img = cv2.imread('OUTPUT_IMG.png')
    global secondpointIndex
    while(secondpointIndex != 4):
        cv2.imshow('image',img)
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
            return False
    return True

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)


if selectFourPoints():
    print("Point Second Selected")


pts1 = np.float32([[pts[0][0],pts[0][1]],[pts[1][0],pts[1][1]],[pts[2][0],pts[2][1]],[pts[3][0],pts[3][1]] ])
pts2 = np.float32([[secondPts[0][0],secondPts[0][1]],[secondPts[1][0],secondPts[1][1]],[secondPts[2][0],secondPts[2][1]],[secondPts[3][0],secondPts[3][1]] ])
#print(pts2)

M = cv2.getPerspectiveTransform(pts1,pts2)
cv2.destroyAllWindows()
print(M)