import xlrd
import xlwt
from xlutils.copy import copy
#读取表格
data1=xlrd.open_workbook('AI_teach.xls')
#获取表格的sheets
table1=data1.sheets()[0]
#获取第一行数据
row1data=table1.row_values(0)

dic={}

if __name__=='__main__':
    book = xlwt.Workbook()  # 新建工作簿
    sheet = book.add_sheet('Data')  # 如果对同一单元格重复操作会发生overwrite Exception，cell_overwrite_ok为可覆盖
    style = xlwt.XFStyle()  # 新建样式
    font = xlwt.Font()  # 新建字体
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font  # 将style的字体设置为font
    book.save(filename_or_stream='qikan.xls')  # 一定要保存
    data = xlrd.open_workbook('qikan.xls', formatting_info=True)  # 读取各种格式信息
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换，进行编辑操作
    excel_table = excel.get_sheet(0)  # 获得要操作的页

    for i in range (1,table1.nrows):
        rowdata=table1.row_values(i)
        qikan=rowdata[3]
        if qikan not in dic:
            dic.update({qikan:1})
        else:
            n=dic.get(qikan,0)
            dic.update({qikan:n+1})
    dic_sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dic_sort)
    print(len(dic_sort))
    n=0
    while n<len(dic_sort):
        print(n)
        excel_table.write(n, 1, dic_sort[n][0])
        excel_table.write(n, 2, dic_sort[n][1])
        n = n + 1
        excel.save('qikan.xls')
