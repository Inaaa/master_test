import numpy as np
import matplotlib.pyplot as plt


position = np.loadtxt('/mrtstorage/users/chli/real_data/1_lidar_pos.txt')
x = position[:,0]
y = position[:,1]

plt.scatter(x, y, alpha=0.6)
plt.show()