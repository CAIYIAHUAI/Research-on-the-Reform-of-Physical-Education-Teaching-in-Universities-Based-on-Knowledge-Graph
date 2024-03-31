import xlrd
import xlwt
from xlutils.copy import copy
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#读取表格
# data1=xlrd.open_workbook('AI_teach.xls')
data1=xlrd.open_workbook(r"C:\Users\15390\Desktop\分词后数据.xls")
#获取表格的sheets
table1=data1.sheets()[0]
#获取第一行数据
row1data=table1.row_values(0)

#读取表格
# data2=xlrd.open_workbook('1.xls')
data2=xlrd.open_workbook(r"C:\Users\15390\Desktop\2.xls")
#获取表格的sheets
table2=data2.sheets()[0]
#获取第一行数据
row2data=table2.row_values(0)
keys=[]
nums=[]
leixing=[]
for i in range(table2.nrows):
    row2data = table2.row_values(i)
    keys.append(row2data[1])
    nums.append(row2data[2])
    leixing.append(row2data[3])
for i in range(0,table2.nrows):
    row2data = table2.row_values(i)
    keys.append(row2data[5])
    nums.append(row2data[6])
    leixing.append(row2data[7])
keys.pop(-1)
nums.pop(-1)
leixing.pop(-1)
print(len(leixing))
G=nx.Graph()#创建什么都没有的空图，图的名称为G
i=0
while i<len(keys):
    j=0
    # print(i,j)
    if leixing[i]=='T':
        a=keys[i]
        while j<len(keys):
            if leixing[j]=='O':
                b=keys[j]
                m=1
                while m < table1.nrows:
                    row1data = table1.row_values(m)
                    m += 1
                    if a in row1data[4] and b in row1data[4]:
                        G.add_edges_from([(a, b)])
                        # print(rowdata[8])
                        # print(a, b)
                        break
                    if a in row1data[5] and b in row1data[5]:
                        G.add_edges_from([(a, b)])
                        break
            if leixing[j]=='M':
                b=keys[j]
                m=1
                while m < table1.nrows:
                    row1data = table1.row_values(m)
                    m += 1
                    if a in row1data[4] and b in row1data[4]:
                        G.add_edges_from([(a, b)])
                        # print(rowdata[8])
                        # print(a, b)
                        break
                    if a in row1data[5] and b in row1data[5]:
                        G.add_edges_from([(a, b)])
                        break
            j+=1
    i+=1
for i in range(len(nums)):
    nums[i]=nums[i]*10+1000
# print(keys)
# print(nums)
carac = pd.DataFrame({ 'ID':keys, 'myvalue':nums})
# print(carac)
G.nodes()
carac= carac.set_index('ID')
print(carac)
carac=carac.reindex(G.nodes())
carac['myvalue']=pd.Categorical(carac['myvalue'])
carac['myvalue'].cat.codes
nx.draw(G, with_labels=True,pos = nx.spring_layout(G) ,cmap=plt.cm.Set1,edge_color='grey',node_color='skyblue',width=1,node_size=carac['myvalue'],font_size=15)#node_size=carac['myvalue']
plt.title('大数据相关关键字网络图')
plt.show()
# plt.savefig("wangluotu.png")
# node_color=carac['myvalue'].cat.codes,