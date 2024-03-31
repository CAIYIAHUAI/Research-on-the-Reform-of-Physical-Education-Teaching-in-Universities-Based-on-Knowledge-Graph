import xlrd
import xlwt
from xlutils.copy import copy
import re

#读取表格
data1=xlrd.open_workbook('AI_teach.xls')
#获取表格的sheets
table1=data1.sheets()[0]
#输出行数量
#print(table1.nrows)
#输出列数量
#print(table1.ncols)
#获取第一行数据
row1data=table1.row_values(0)

name=[]
num=[]
no=0

for i in range(1,table1.nrows):
    rowdata = table1.row_values(i)
    if '' in rowdata[7] and len(rowdata[7])<2:
        no=no+1
        continue
    else:
        if '1' in rowdata[2]:
            p= rowdata[2].split('1')
            p=p[0]
            if p not in name:
                k = 1  # 计算关键字出现次数
                name.append(p)
                num.append(k)
            else:
                t = 0
                while t < len(name):
                    if p == name[t]:
                        num[t] += 1
                        break
                    t += 1

print(name)
print(num)

#将关键字存入字典并排序
dic={}
dic_sort={}
m=0
while m<len(name):
    # if num[m]==1:
    #     m+=1
    #     continue
    dic[name[m]]=num[m]
    dic.setdefault(name[m])
    m+=1
dic_sort=sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(type(dic_sort))
print(dic_sort)
print(len((dic_sort)))








