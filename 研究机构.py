import xlrd
import xlwt
from xlutils.copy import copy
import re
import pandas as pd

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
    rowdata=table1.row_values(i)
    if '' in rowdata[7] and len(rowdata[7])<3:
        no=no+1
        continue
    else:
        if '1.'in rowdata[7]:
            p=re.sub('1. ','',rowdata[7])
            if '大学' in p:
                addr=p.split('大学')
                p=addr[0]+'大学'
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
            else:
                if '学院' in p:
                    addr = p.split('学院')
                    p = addr[0] + '学院'
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
                else:
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
        else:
            p = rowdata[7].strip()  # 清楚关键字空格
            if '大学' in p:
                addr = p.split('大学')
                p = addr[0] + '大学'
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
            else:
                if '学院' in p:
                    addr = p.split('学院')
                    p = addr[0] + '学院'
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
                else:
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
#学校名字
# print(name)
#学校出现次数
# print(num)


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
dic_sort=dict(dic_sort)
print(type(dic_sort))
print(dic_sort)
print(len((dic_sort)))

df = pd.DataFrame.from_dict(dic_sort,orient='index')
df.to_csv('research_insitution.csv',encoding='gbk')