
'''
road = 125
lane = 255
'''


import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_dir ="./data/frame0001.jpg"
image = Image.open(image_dir)

image = np.array(image)
image2 = image[:,:,1].reshape([800,1200])
x = image[:,:,1]
print(type(x))

#x=np.where( x ==125, x, 0*x)

x = x.reshape([800,1200])


print(np.unique(x))
print("!!!!!!!!!!")
plt.figure()
plt.imshow(x)
plt.show()