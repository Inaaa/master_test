import numpy as np
import os

f = open("/home/cc/Desktop/motion_state.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法

f2 = open("/home/cc/Desktop/motion_state2.txt",'w')
f3 = open("/home/cc/Desktop/motion_state_xy.txt",'w')
while line:

    #print(line, end = '')    # 在 Python 3 中使用
    time = line.split(",", 7)[2]
    x = line.split(",", 11)[5:11]

    print(time)
    if time > "1571220343" and time < "1571220376":
        f2.write(time+' '+str(x)+'\n')
        f3.write(line.split(",", 7)[5]+' '+line.split(",", 7)[6] +'\n')
        print("!!!!!!!!!!!")

    line = f.readline()


f.close()
f2.close()