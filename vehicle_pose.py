import numpy as np
from coordinate_conversion import Trans
import matplotlib.pyplot as plt
import math
import scipy.interpolate as spi

points = np.loadtxt('./data/points2.txt')
a = Trans()
points_new = a.project_map_to_vehicle(points)[:, :3]

points_new = points_new[np.where(abs(points_new[:,1]) <=3)]
points_new = points_new[np.where(abs(points_new[:,0])<=25)]
plt.figure()
x = points_new[:, 0]
y = points_new[:, 1]
z = points_new[:, 2]
plt.scatter(x, y, alpha=0.6)
plt.show

points_new_l = points_new[np.where(points_new[:, 1] <= 0)]
points_new_r = points_new[np.where(points_new[:, 1] > 0)]


"""
X = np.transpose(points_new_l[:, 0])
print(X)
Y = np.transpose(points_new_l[:, 2])
print(Y)

# 进行一阶样条差值
#ipo1 = spi.splrep(X, Y, k=1)  # 源数据点导入，生成参数
print('!!!!!!!!!')
#iy1 = spi.splev(x, ipo1)  # 根据观测点和样条参数，生成插值

# 进行三次样条拟合
ipo3 = spi.splrep(X, Y)  # 源数据点导入，生成参数
iy3 = spi.splev(x, ipo3)  # 根据观测点和样条参数，生成插值


##作图
fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10,12))
ax1.plot(X,Y,label='沪深300')
ax1.plot(x,iy1,'r.',label='插值点')
ax1.set_ylim(Y.min()-10,Y.max()+10)
ax1.set_ylabel('指数')
ax1.set_title('线性插值')
ax1.legend()
ax2.plot(X,Y,label='沪深300')
ax2.plot(x,iy3,'b.',label='插值点')
ax2.set_ylim(Y.min()-10,Y.max()+10)
ax2.set_ylabel('指数')
ax2.set_title('三次样条插值')
ax2.legend()

"""








point = np.loadtxt("./data/one_motion_state_xy.txt")
n = point.shape[0]
point = np.hstack((point, np.ones((n, 1))))
point_new = a.project_map_to_vehicle(point)[:, :2]
print("!!!!!!!!!!!")
p = np.mean(point_new, axis=0)
print(p)





def one_point():
    points_r = np.loadtxt('./data/points_r_2.txt')
    points_l = np.loadtxt('./data/points_l_2.txt')
    points = np.vstack((points_l,points_r))
    a = Trans()
    points_new = a.project_map_to_vehicle(points)[:, :3]

    plt.figure()
    x = points_new[:, 0]
    y = points_new[:, 1]
    z = points_new[:, 2]
    plt.scatter(x, y, alpha = 0.6)
    plt.show

    point = np.loadtxt("./data/one_motion_state_xy.txt")
    n = point.shape[0]
    point = np.hstack((point, np.ones((n, 1))))
    point_new = a.project_map_to_vehicle(point)[:, :2]
    print("!!!!!!!!!!!")
    p = np.mean(point_new,axis=0)
    print(p)

#one_point()


# than(theta) = 0.052
theta = math.atan(0.055)*180/math.pi
theta1 = math.atan(0.0477)*180/math.pi
theta2 = math.atan(0.01)*180/math.pi
print(theta,theta1, theta2)






'''
b = []
for i in arange(a):
    if a[i, 0] ==
    
'''