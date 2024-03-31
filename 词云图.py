import xlrd
import wordcloud

#读取表格
# data1=xlrd.open_workbook('tu3.xls')
# data1=xlrd.open_workbook('AI_teach_keys.xls')
data1=xlrd.open_workbook(r"C:\Users\15390\Desktop\分词后数据.xls")
# data1=xlrd.open_workbook('1.xls')
#获取表格的sheets
table1=data1.sheets()[0]
#输出行数量
#print(table1.nrows)
c=table1.nrows
#输出列数量
#print(table1.ncols)
d=table1.ncols
#获取第一行数据
row1data=table1.row_values(0)
dic={}
# for i in range(1,c-1):
#     rowdata = table1.row_values(i)
#     dic[rowdata[0]]=rowdata[d-1]
# rowdata1=table1.row_values(0)
# print(rowdata1)
# rowdata2=table1.row_values(c-1)
# print(rowdata2)
# for i in range(1,d-1):
#     dic[rowdata1[i]] = rowdata2[i]

for i in range(0,209):
    rowdata = table1.row_values(i)
    dic[rowdata[1]] = rowdata[2]
#

# for i in range(0,c-1):
#     rowdata = table1.row_values(i)
#     dic[rowdata[1]] = rowdata[2]
#     dic[rowdata[6]] = rowdata[7]
# rowdata = table1.row_values(c-1)
# dic[rowdata[1]] = rowdata[2]
print(dic)
# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(
    width=1200,
    height=600,
    background_color='white',
    font_path='msyh.ttc',
    font_step=1,
    min_font_size=4,
    max_font_size=None,
    max_words=500,
    stopwords={},
    scale=3,
    prefer_horizontal=1,
    relative_scaling=0.6,
    mask=None,
    contour_width = 1,
    contour_color = 'steelblue')
# w.generate('从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')

w.generate_from_frequencies(dic)
w.to_file('output2-poem.png')

