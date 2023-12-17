from PIL import Image
import numpy as np
a = Image.open("scene1.row3.col2.ppm") # left image
a1 = Image.open("scene1.row3.col3.ppm") # right image

######
n = 15
n1 = np.ceil(n/2)
a = np.float32(a)
a1 = np.float32(a1)

b = a.shape
print(b)