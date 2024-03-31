
import xlrd
import xlwt
from xlutils.copy import copy
#提取关键字
def get_keys(i,list_len,keys_list):
    while i < list_len:
        rowdata = keys_list(i)
        i += 1#控制循环次数
        rowdata_keys = rowdata[5].split(',')#分割关键字
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
data0=xlrd.open_workbook(r"C:\Users\15390\Desktop\分词后数据.xls")
data2=xlrd.open_workbook(r"C:\Users\15390\Desktop\积极情绪分词后数据.xls")
data1=xlrd.open_workbook(r"C:\Users\15390\Desktop\消极情绪分词后数据.xls")
data4=xlrd.open_workbook(r"C:\Users\15390\Desktop\好评最多.xls")
data5=xlrd.open_workbook(r"C:\Users\15390\Desktop\差评最多分词后数据.xls")


#获取表格的sheets
table1=data1.sheets()[0]

row1data=table1.row_values(0)

x_data=[]
y_data=[]
num=[]#数量
keys= []#关键字

if __name__=='__main__':
    # 建立对应的表格
    book = xlwt.Workbook()  # 新建工作簿
    sheet = book.add_sheet('Data')  # 如果对同一单元格重复操作会发生overwrite Exception，cell_overwrite_ok为可覆盖
    style = xlwt.XFStyle()  # 新建样式
    font = xlwt.Font()  # 新建字体
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font  # 将style的字体设置为font
    book.save(filename_or_stream='DATA2022_keys.xls')  # 一定要保存
    data = xlrd.open_workbook('DATA2022_keys.xls', formatting_info=True)  # 读取各种格式信息
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换，进行编辑操作
    excel_table = excel.get_sheet(0)  # 获得要操作的页

    get_keys(1, table1.nrows, table1.row_values)

    # #据 Donohue 高低频词分界公
    n=0

    m=0


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
        excel.save('Keywords_Bad.xls')

