import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import math
import os

'''
generate the liDAR data
'''

style.use('ggplot')
matplotlib.use( 'tkagg' )

class lidar():
    def __init__(self):
        self.SLOPE = 15
        self.SUPERELEVATION = 0


    def wgn(self,x, snr):
        for i in range(len(x)):
            snr = 10 ** (snr / 10.0)
            xpower = np.sum(x[i] ** 2) / len(x)
            npower = xpower / snr
            return np.random.randn(len(x)) * np.sqrt(npower)

    def angle_distance(self):
        angle_max = 15
        angle_min = -15
        h = 1.7
        height = []
        x=[]
        dis_x =[]
        dis =[]

        for i in range(15):
            #x.append(i)
            print(i)

            angle = (angle_min+ 2.0*i)* math.pi / 180
            if self.SLOPE != 0:
                if angle <0:
                    dis =1.7 / abs(math.tan(angle) )
                    if dis < 10:
                        dis_x.append(dis)
                        height.append(0.0)
                    else:
                        m=(1.7-10*abs(math.tan(angle)))/(1+abs(math.tan(angle))/math.tan(self.SLOPE*math.pi/180))

                        height.append(m)
                        dis_x.append(m/math.tan(self.SLOPE*math.pi/180)+10)
                else:
                    m = (10*math.tan(angle)+1.7)/(1-math.tan(angle)/math.tan(self.SLOPE*math.pi/180))
                    dis =m/math.tan(self.SLOPE*math.pi/180)+10
                    if dis <40:
                        height.append(m)
                        dis_x.append( dis)
                    else:
                        break

                x.append(i)
            else:
                m =1.7 / abs(math.tan((angle_min+2*i)*math.pi/180))
                dis_x.append(m)

                if m > 40:
                    break
            #if i ==0:
            #    dis.append(dis_x[0])
            #else:
             #   dis.append(dis_x[i] -dis_x[i-1])
            #print("dis= ", dis[i])
            #print("dis_x= ", dis_x[i])

        '''
        plt.figure() 
        #plt.plot(x, height, "y-", linewidth=1, label="dis_x")  # 画图
        plt.plot(dis_x, height, "y-", linewidth=1, label="height")
        #plt.plot(dis_x2, height, "r-", linewidth=1, label="height")
        plt.legend()
        plt.show()
        '''
        print('dis_x', len(dis_x))
        return dis_x


    def points2(self,dis_x,height):
        if os.path.exists("test.txt"):
            os.remove("test.txt")
        f = open ("test.txt","w")
        for i in range(len(dis_x)):
            for j in range(50):
                y = 0.2*( j - 25 )
                x =dis_x[i]
                z =height[i]
                f.write(str(x) + ' ')
                # f.write(' ')
                f.write(str(y) + ' ')
                f.write(str(z))
                f.write('\n')






    def number_of_points(self, dis_x):
        y_max = math.sin(math.pi/8) *dis_x[3]
        y_min = -y_max
        number = np.zeros(len(dis_x))
        alpha = np.zeros(len(dis_x))
        print('alpha', alpha.shape)


        for i in range(len(dis_x)):
            alpha[i] = math.asin(y_max/dis_x[i])*2   ##radian
            number[i] = alpha[i]/math.pi*3*50 ## here define in the beginning ,there are 60 points


        return number,alpha







    def points(self,dis_x,number,alpha):
        if os.path.exists("test_new.txt"):
            os.remove("test_new.txt")
        f = open ("test_new.txt","w")
        angle_min = -15
        h = 1.7
        height = []
        point_x = []
        point_y = []
        point_z = []
        for i in range(len(dis_x)):
            interval =alpha[i]/number[i]
            print('alpha[i]/2  ', alpha/2)
            print('interval', interval)

            for j in np.arange(-alpha[i]/2, alpha[i]/2 , interval):

                y = math.sin(j) * dis_x[i]

                x = math.cos(j) * dis_x[i]

                if y<-2 :
                    z = math.tan(self.SLOPE / 180 * math.pi) * (dis_x[i])

                else:
                    z = math.tan(self.SLOPE/ 180 * math.pi)*(dis_x[i]) + (y+2)*math.tan(self.SUPERELEVATION*math.pi/180)



                point_x.append(x)
                point_y.append(y)
                point_z.append(z)



                f.write(str(x)+' ')
                #f.write(' ')
                f.write(str(y)+' ')
                f.write(str(z))
                f.write('\n')
                #break

        f.close()

        n_x = self.wgn(point_x, 15)
        point_x = point_x + n_x
        n_y = self.wgn(point_y, 15)
        point_y = point_y + n_y
        n_z = self.wgn(point_z, 15)
        point_z = point_z + n_z
        if os.path.exists("test_new_noise.txt"):
            os.remove("test_new_noise.txt")
        f = open ("test_new_noise","w")
        for i in range(len(point_x)):
            f.write(str(point_x[i]) + ' ')
            # f.write(' ')
            f.write(str(point_y[i]) + ' ')
            f.write(str(point_z[i]))
            f.write('\n')

        f.close()
                #print(dis_x[15])




a =lidar()
dis_x = a.angle_distance()
#a.points2(dis_x,height)
#h = a.height(dis_x)
number,alpha = a.number_of_points(dis_x)
a.points(dis_x, number, alpha)
