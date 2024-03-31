import matplotlib.pyplot as plt
import numpy as np
import re
import xlsxwriter
import xlrd
import xlwt
from xlutils.copy import copy
#提取关键字
def get_keys1(i,list_len,keys_list):
    while i < list_len:
        rowdata = keys_list(i)
        i += 1#控制循环次数
        rowdata_keys = rowdata[8].split(';')#分割关键字
        for kes in rowdata_keys:
            p = kes.strip()#清楚关键字空格
            if kes == '':
                continue
            if p not in keys:
                k = 1  # 计算关键字出现次数
                keys.append(p)
                num.append(k)
            else:
                t = 0
                while t < len(keys):
                    if p == keys[t]:
                        num[t] += 1
                        break
                    t += 1
def get_keys2(i,list_len,keys_list):
    while i < list_len:
        rowdata = keys_list(i)
        i += 1#控制循环次数
        rowdata_keys = rowdata[1].split(';')#分割关键字
        for kes in rowdata_keys:
            p = kes.strip()#清楚关键字空格
            if kes == '':
                continue
            if p not in keys:
                k = 1  # 计算关键字出现次数
                keys.append(p)
                num.append(k)
            else:
                t = 0
                while t < len(keys):
                    if p == keys[t]:
                        num[t] += 1
                        break
                    t += 1

#读取表格
data1=xlrd.open_workbook(r"E:\Education\2019年之后.xls")
data2=xlrd.open_workbook('COVID_keys2.xls')

#获取表格的sheets
table1=data1.sheets()[0]
table2=data2.sheets()[0]
#输出行数量
#print(table1.nrows+table2.nrows+table3.nrows+table4.nrows+table5.nrows+table6.nrows+table7.nrows+table8.nrows-8)
#输出列数量
#print(table1.ncols)
#获取第一行数据
row1data=table1.row_values(0)
row2data=table2.row_values(0)
#print(row1data)#['列1', '列2', '列3', '列4']
#print(row1data[0])#列1
x_data=[]
y_data=[]
num=[]#数量
keys= []#关键字
# i=1行循环

# while i<table1.nrows:
#     rowdata = table1.row_values(i)
#     i += 1
#     rowdata_keys=rowdata[8].split(';')
#     for kes in rowdata_keys:
#         p = kes.strip()
#         if kes=='':
#             continue
#         if p not in keys:
#             k=1#计数
#             keys.append(p)
#             num.append(k)
#         else:
#             t=0
#             while t<len(keys):
#                 if p==keys[t]:
#                     num[t]+=1
#                     break
#                 t+=1
# print(len(keys))
# print(len(num))
if __name__=='__main__':
    # 建立对应的表格
    book = xlwt.Workbook()  # 新建工作簿
    sheet = book.add_sheet('Data')  # 如果对同一单元格重复操作会发生overwrite Exception，cell_overwrite_ok为可覆盖
    style = xlwt.XFStyle()  # 新建样式
    font = xlwt.Font()  # 新建字体
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font  # 将style的字体设置为font
    book.save(filename_or_stream='COVID_Allkeys.xls')  # 一定要保存
    data = xlrd.open_workbook('COVID_Allkeys.xls', formatting_info=True)  # 读取各种格式信息
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换，进行编辑操作
    excel_table = excel.get_sheet(0)  # 获得要操作的页

    get_keys1(1, table1.nrows, table1.row_values)
    get_keys2(0, table2.nrows, table2.row_values)

    # #据 Donohue 高低频词分界公
    n=0
    # i=0
    # while i<len(num):
    #     if num[i]==1:
    #         n+=1
    #     i+=1
    m=0
    # T=1/2*(-1+(1+8*n)**0.5)
    #
    # #用孙清兰所研究的高频低频词分界标准
    # D=int(len(num)**0.5)
    # print(D)

#将关键字存入字典并排序
    dic={}
    dic_sort={}
    while m<len(keys):
        # if num[m]==1:
        #     m+=1
        #     continue
        dic[keys[m]]=num[m]
        dic.setdefault(keys[m])
        m+=1
    dic_sort=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print(type(dic_sort))
    print(dic_sort)
    print(len((dic_sort)))

    while n<len(dic_sort):
        excel_table.write(n, 1, dic_sort[n][0])
        excel_table.write(n, 2, dic_sort[n][1])
        n = n + 1
        excel.save('COVID_Allkeys.xls')
    # #获取key值,value值
    # for k, v in dic_sort.items():
    #     print(k, v)
    #     excel_table.write(n, 1, k)
    #     excel_table.write(n, 2, v)
    #     n=n+1
    #     excel.save('Bigdata_keys.xls')


    # print(dic_sort)
    # print(len((dic_sort)))



    # # 这两行代码解决 plt 中文显示的问题
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # i = 0
    # key_s = []
    # num_s = []
    # for dic_sort_one in dic_sort:
    #     # if dic_sort_one[1]<D:
    #     #     break
    #     if dic_sort_one[0]=='人工智能' or dic_sort_one[0]=='人工智能技术'or dic_sort_one[0]=='应用'or dic_sort_one[0]=='影响'or dic_sort_one[0]=='发展':
    #         continue
    #     key_s.append(dic_sort_one[0])
    #     num_s.append(dic_sort_one[1])
    #     i+=1
    #
    # plt.barh(key_s,num_s)
    # plt.tick_params(labelsize=6)
    # plt.title('人工智能高频关键词')
    # plt.savefig("Bigdata_keys.png")
    # plt.show()


