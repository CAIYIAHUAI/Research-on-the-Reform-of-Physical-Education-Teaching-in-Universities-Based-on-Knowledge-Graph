import xlrd
import xlwt
from xlutils.copy import copy
import re

#读取表格
data1=xlrd.open_workbook(r"E:\Education\biao1运行文件.xls")
#获取表格的sheets
table1=data1.sheets()[0]
#输出行数量
print(table1.nrows)
#输出列数量
# print(table1.ncols)
#获取第一行数据
row1data=table1.row_values(0)


p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
avers=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
aver=[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]

print(len(p))
for i in range(1,table1.nrows):
    rowdata=table1.row_values(i)
    if '2021' in rowdata[4] and '页数' in rowdata[10]:
        p[0]=p[0]+1
        n=re.findall(r'\d+', rowdata[10])
        avers[0] = int(n[0])+avers[0]
    if '2020' in rowdata[4] and '页数' in rowdata[10]:
        p[1]=p[1]+1
        n=re.findall(r'\d+', rowdata[10])
        avers[1] = int(n[0])+avers[1]
    if '2019' in rowdata[4] and '页数' in rowdata[10]:
        p[2]=p[2]+1
        n=re.findall(r'\d+', rowdata[10])
        avers[2] = int(n[0])+avers[2]

    if '2018' in rowdata[4] and '页数' in rowdata[10]:
        p[3] = p[3] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[3] = int(n[0]) + avers[3]

    if '2017' in rowdata[4] and '页数' in rowdata[10]:
        p[4] = p[4] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[4] = int(n[0]) + avers[4]

    if '2016' in rowdata[4] and '页数' in rowdata[10]:
        p[5] = p[5] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[5] = int(n[0]) + avers[5]

    if '2015' in rowdata[4] and '页数' in rowdata[10]:
        p[6] = p[6] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[6] = int(n[0]) + avers[6]

    if '2014' in rowdata[4] and '页数' in rowdata[10]:
        p[7] = p[7] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[7] = int(n[0]) + avers[7]

    if '2013' in rowdata[4] and '页数' in rowdata[10]:
        p[8] = p[8] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[8] = int(n[0]) + avers[8]

    if '2012' in rowdata[4] and '页数' in rowdata[10]:
        p[9] = p[9] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[9] = int(n[0]) + avers[9]

    if '2011' in rowdata[4] and '页数' in rowdata[10]:
        p[10] = p[10] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[10] = int(n[0]) + avers[10]

    if '2010' in rowdata[4] and '页数' in rowdata[10]:
        p[11] = p[11] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[11] = int(n[0]) + avers[11]
    if '2009' in rowdata[4] and '页数' in rowdata[10]:
        p[12] = p[12] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[12] = int(n[0]) + avers[12]
    if '2008' in rowdata[4] and '页数' in rowdata[10]:
        p[13] = p[13] + 1
        n = re.findall(r'\d+', rowdata[10])
        avers[13] = int(n[0]) + avers[13]

print(p)
print(f'sum_p:{sum(p)}')
print(avers)
print(f'sum_avers{sum(avers)}')
for i in range(0,len(avers)):
    aver[i]=avers[i]/p[i]
    print('%.2f'%aver[i])



