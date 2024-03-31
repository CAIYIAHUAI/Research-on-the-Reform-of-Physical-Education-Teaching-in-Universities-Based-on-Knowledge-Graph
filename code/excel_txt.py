import xlrd

def strs(row):
    values = "";
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i]) + ","
    return values

# 打开文件
data = xlrd.open_workbook("AI_teach.xls")
sqlfile = open("sourceData/AI_teach.txt", "a", encoding='utf-8') # 文件读写方式是追加

table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(0)  # 某一行数据
# 打印出行数列数
print(nrows)
print(ncols)
print(colnames)
for ronum in range(1, nrows):
    row = table.row_values(ronum)
    values = row[8]+row[10] # 调用函数，将行数据拼接成字符串

    sqlfile.writelines(values + "\r") #将字符串写入新文件
sqlfile.close() # 关闭写入的文件