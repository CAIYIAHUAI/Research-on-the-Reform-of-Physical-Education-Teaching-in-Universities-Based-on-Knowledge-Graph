import jieba.analyse
import xlrd
import xlwt
from xlutils.copy import copy
O=['教育','教师','高等教育','学生','高校','学习者','智慧教育','职业','智能教育','教育领域','职业教育','人才']
T=['人工智能','技术','智能','教学','人才培养','应用','机器人','智慧','变革','创新','知识','信息技术','课程','信息化','实践','大数据','培养','教育信息化','学科','专业','AI','深度学习','智能化','数据','素养','认知','教学模式','个性化','课程体系']
M=['学习','研究','融合','思维']
m=len(O)
n=len(T)
# print(m)
# print(n)
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        a[i].append(0)
# print(a)
# print(len(a))
with open('sourceData/AI_teach.txt', "r", encoding='utf-8') as fr:
    lines = fr.readlines()
    for line in lines:
        text=line
        jieba.load_userdict('sourceData/baoliu.txt')
        fenci_text = jieba.cut(text)
        b = jieba.analyse.extract_tags(text, topK=6, allowPOS=())
        print(b)
        for i in range(0,m):
            if O[i] in b:
                for j in range(0,n):
                    if T[j] in line:
                        a[i][j]=a[i][j]+1

# 建立对应的表格
    book = xlwt.Workbook()  # 新建工作簿
    sheet = book.add_sheet('Data')  # 如果对同一单元格重复操作会发生overwrite Exception，cell_overwrite_ok为可覆盖
    style = xlwt.XFStyle()  # 新建样式
    font = xlwt.Font()  # 新建字体
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font  # 将style的字体设置为font
    book.save(filename_or_stream='tu3.xls')  # 一定要保存
    data = xlrd.open_workbook('tu3.xls', formatting_info=True)  # 读取各种格式信息
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换，进行编辑操作
    excel_table = excel.get_sheet(0)  # 获得要操作的页
    for i in range(0,m):
        excel_table.write(i+1, 0, O[i])
        excel.save('tu3.xls')
    for j in range(0, n):
        excel_table.write(0, j+1, T[j])
        excel.save('tu3.xls')
    for i in range(0,m):
        for j in range(0,n):
            excel_table.write(i+1, j+1, a[i][j])
            excel.save('tu3.xls')



