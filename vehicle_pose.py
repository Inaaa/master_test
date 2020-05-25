import numpy as np
from coordinate_conversion import Trans
import matplotlib.pyplot as plt
import math
import scipy.interpolate as spi

def vehicle_pose():
    points = np.loadtxt('./data/points2.txt')
    a = Trans()
    points_new = a.project_map_to_vehicle(points)[:, :3]

    points_new = points_new[np.where(abs(points_new[:,1]) <=3)]
    points_new = points_new[np.where(abs(points_new[:,0])<=10)]
    #points_new = points_new[np.where(points_new[:, 0] <= 35)]
    #points_new = points_new[np.where(points_new[:, 0] > -5)]

    plt.figure()
    x = points_new[:, 0]
    y = points_new[:, 1]
    z = points_new[:, 2]
    plt.scatter(x, y, alpha=0.6)
    plt.show

    #points_new2 = points_new[np.where(abs(points_new[:,1]) <=3)]
    points_new2 = points_new[np.where(points_new[:,0]>10)]

    plt.figure()
    x_2 = points_new2[:, 0]
    y_2 = points_new2[:, 1]
    z_2 = points_new2[:, 2]
    plt.scatter(x_2, y_2, alpha=0.6)
    plt.show

    points_new_l = points_new[np.where(points_new[:, 1] <= 0)]
    points_new_r = points_new[np.where(points_new[:, 1] > 0)]

    return x, z, y_2, z_2

def Least_squares(x,y):
    x_ = x.mean()
    y_ = y.mean()
    m = np.zeros(1)
    n = np.zeros(1)
    k = np.zeros(1)
    p = np.zeros(1)
    for i in np.arange(len(x)):
        k = (x[i]-x_)* (y[i]-y_)
        m += k
        p = np.square( x[i]-x_ )
        n = n + p
    a = m/n
    b = y_ - a* x_
    return a,b

'''
point = np.loadtxt("./data/one_motion_state_xy.txt")
n = point.shape[0]
point = np.hstack((point, np.ones((n, 1))))
point_new = a.project_map_to_vehicle(point)[:, :2]
print("!!!!!!!!!!!")
p = np.mean(point_new, axis=0)
print(p)
'''




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

# than(theta) = 0.052
#theta = math.atan(0.055)*180/math.pi
#theta1 = math.atan(0.0477)*180/math.pi
#theta2 = math.atan(0.01)*180/math.pi
#print(theta,theta1, theta2)

if __name__ == '__main__':
    x, z, y_2, z_2 = vehicle_pose()
    a, b = Least_squares(x, z)
    print(a, b)
    y1 = a * x + b
    plt.figure(figsize=(10, 5), facecolor='w')
    plt.plot(x, z, 'ro', lw=2, markersize=6)
    plt.plot(x, y1, 'r-', lw=2, markersize=6)
    plt.grid(b=True, ls=':')
    plt.xlabel(u'X', fontsize=16)
    plt.ylabel(u'Y', fontsize=16)
    plt.show()

    print("road slope = ", a*100)

    a, b = Least_squares(y_2, z_2)
    print(a, b)
    z1 = a * y_2 + b
    plt.figure(figsize=(10, 5), facecolor='w')
    plt.plot(y_2, z_2, 'ro', lw=2, markersize=6)
    plt.plot(y_2, z1, 'r-', lw=2, markersize=6)
    plt.grid(b=True, ls=':')
    plt.xlabel(u'X', fontsize=16)
    plt.ylabel(u'Y', fontsize=16)
    plt.show()

    #print("road slope = ", a)



