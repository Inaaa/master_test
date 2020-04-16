

# -*- coding: UTF-8 -*-
# 程序功能是为了完成判断文件中是否有重复句子
# 并将重复句子打印出来

res_list = []
# f = open('F:/master/master-work/code_of_graduate/LTP_data/raw_plain.txt','r')
f = open('./data/points_r.txt', 'r')
f2 = open("./data/points_r_2.txt",'w')
res_dup = []
index = 0
#file_dul = open('F:/master/master-work/code_of_graduate/chu_li_shuju/ldc-weibo-train-dul.txt', 'w')
for line in f.readlines():
    index = index + 1
    if line in res_list:
        temp_str = ""
        temp_str = temp_str + str(index)  # 要变为str才行
        temp_line = ''.join(line)
        temp_str = temp_str + temp_line
        # 最终要变为str类型
        #file_dul.write(temp_str);  # 将重复的存入到文件中
    else:
        res_list.append(line)
        f2.write(line)

print(len(res_list))



f.close()
f2.close()