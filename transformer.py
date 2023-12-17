# Make a function that will do the work
import cv2
import numpy as np
import time

def transformer(mat , img):
    pass
# Translational
the=30
#M =np.array([[1,0,50],[0,1,0],[0,0,1]])
# Rotation
M =np.array([[np.cos(the),np.sin(the),0],[np.sin(the),np.cos(the),0],[0,0,1]])
img = cv2.imread("Image_1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# grab the dimensions of the image and calculate the center of the
# image
out_img = np.zeros((img.shape[0]+1000,img.shape[1]+1000))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
       intensity = img[i,j]
       points= np.array([i,j,1])
       processed_points= np.matmul(M,points)
       #print(intensity)
       out_img[int(processed_points[0]),int(processed_points[1])] = intensity 
       
       #print(processed_points)
        #time.sleep(0.1)
cv2.imshow('out_img', out_img)
cv2.waitKey(0)