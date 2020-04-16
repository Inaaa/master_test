import numpy as np
import os

def get_motion():

    f = open("./data/motion_state.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法

    f2 = open("./data/motion_state2.txt",'w')
    f3 = open("./data/motion_state_xy.txt",'w')
    while line:

        #print(line, end = '')    # 在 Python 3 中使用
        time = line.split(",", 7)[2]
        x = line.split(",", 12)[5:12]
        #print(x)

        #print(time)
        if time > "1571220343" and time < "1571220376":
            f2.write(time+','+x[0]+','+x[1]+','+x[3]+','+x[4]+','+x[5]+','+x[6]+'\n')

            f3.write(line.split(",", 7)[5]+' '+line.split(",", 7)[6] +'\n')
            #print("!!!!!!!!!!!")

        line = f.readline()


    f.close()
    f2.close()

def get_one_motion():
    f = open("./data/motion_state2.txt")  # 返回一个文件对象
    f2 = open("./data/one_motion_state.txt", 'w')
    f3 = open("./data/one_motion_state_xy.txt", 'w')


    line = f.readline()  # 调用文件的 readline()方法
    while line:

        # print(line, end = '')    # 在 Python 3 中使用
        time = line.split(",", 2)[0]
        #x = line.split(",", 11)[5:11]


        #print(time[0:11])
        if time[0:11] == "15712203563":
            f2.write(line)
            f3.write(line.split(",", 7)[1]+' '+line.split(",", 7)[2] +'\n')

            print(line)

        line = f.readline()

    f.close()

get_motion()
get_one_motion()