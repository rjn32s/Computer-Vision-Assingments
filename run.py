import cv2

import numpy as np
import math

Image=cv2.imread("Image_1.png") 
angle=60
anglerad=(math.pi*angle)/180
# Rotation
# Mat=([math.cos(anglerad),math.sin(anglerad),0] ,
#      [-math.sin(anglerad),math.cos(anglerad),0] ,
#      [0,0,1])
# Affine
# Mat=([[ 0.5, 0,  5],
#         [0.1,  0.5,5],
#         [0,0,  1]])
# Homography
# Mat=([[ 20, 0,  0],
#         [0.1,  20,0],
#         [0.01,0.01,  10]])
# Translational
pixel_value_tx =50
pixel_value_ty  = 40
Mat=([[1, 0,  pixel_value_tx],
        [0, 1,pixel_value_ty],
        [0,0,  1]])

s=Image.shape

s

##Bring The Origin To Center
trans=([1,0,s[0]/2] ,
       [0,1,s[1]/2] ,
       [0,0,1])

outx=np.zeros([s[0],s[1]])
outy=np.zeros([s[0],s[1]])

for i in range(0,s[0]):
    for j in range(0,s[1]):
        new=(np.dot(Mat,[j,i,1]))
        outx[i,j]=new[0]/new[2]
        outy[i,j]=new[1]/new[2]

minoutx = np.min(outx)
minouty = np.min(outy)
maxoutx = np.max(outx)
maxouty = np.max(outy)

f=np.zeros(([int(maxouty+abs(minouty)+2),int(maxoutx+abs(minoutx)+4),3]))

for i in range(0,s[0]):
    for j in range(0,s[1]):
        f[(int(outy[i,j]+abs(minouty)+1)),(int(outx[i,j]+abs(minoutx)+1)),0]=Image[i,j,0]
        f[(int(outy[i,j]+abs(minouty)+1)),(int(outx[i,j]+abs(minoutx)+1)),1]=Image[i,j,1]
        f[(int(outy[i,j]+abs(minouty)+1)),(int(outx[i,j]+abs(minoutx)+1)),2]=Image[i,j,2]

cv2.imwrite("OUTPUT_IMG.png", f)


cv2.imshow("OUTPUT",f)
cv2.waitKey(0)
