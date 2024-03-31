import jieba
import jieba.analyse
import xlrd
import xlwt
from xlutils.copy import copy

#读取表格
# data1=xlrd.open_workbook(r"C:\Users\15390\Desktop\2022年全国大学生数据分析大赛赛题\题目B：餐饮服务评价情感倾向分析\data\data.xls")
data1=xlrd.open_workbook(r"C:\Users\15390\Desktop\分词后数据.xls")
#获取表格的sheets
table1=data1.sheets()[0]
#获取第一行数据
row1data=table1.row_values(0)

#第一步：分词，这里使用结巴分词全模式
# text = '''智能教育是人工智能时代的教育转型。它不仅具有教育基础设施的信息化、智能化,而且注重教育理念与教育方式的整体转型。智能教育的目的是构建一种新型的教育生态,为教育提供精准服务。智慧课堂是在开启智能教育的基础上,改革教学手段,发展生命课堂,提升学生综合素养,把现代信息技术恰到好处地运用于教育教学中,促进新时代的教育事业快速发展。 '''
# fenci_text = jieba.cut(text)
#print("/ ".join(fenci_text))

#第二步：去停用词
#这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
# stopwords = {}.fromkeys([ line.rstrip() for line in open('stopwords.txt') ])
# final = ""
# for word in fenci_text:
#     if word not in stopwords:
#         if (word != "。" and word != "，") :
#             final = final + " " + word
# print(final)

#第三步：提取关键词
# a=jieba.analyse.extract_tags(text, topK = 5, withWeight = True, allowPOS = ())
# b=jieba.analyse.extract_tags(text, topK = 6,   allowPOS = ())
# print(a)
# print(b)
#text 为待提取的文本
#topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
# withWeight:是否一并返回关键词权重值，默认值为False。
# allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。
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
    i=1
    while i<table1.nrows:
        text=table1.row_values(i)[5]
        fenci_text = jieba.cut(text)
        a = jieba.analyse.extract_tags(text, topK=6, allowPOS=())
        # t=jieba.analyse.extract_tags(text, topK = 6, withWeight = True, allowPOS = ())
        # print(t)
        c=[]
        for b in a:
            c.append(b)
            c.append(';')
        excel_table.write(i, 1, c)
        i+=1
        excel.save('DATA2022_keys.xls')
print('finish')