import pandas as pd
import numpy as np
from sklearn import tree
import graphviz

clas = pd.read_excel(r"C:\Users\Yihuai Cai\Desktop\数据处理结果.xlsx",sheet_name=0)
clas

y = clas.iloc[:,1]
y.head()

for idx,value in y.items():
    if value == '高钾':
        y[idx] = 1
    if value == '铅钡':
        y[idx] = 0
y

x = clas.iloc[:,5:-1]
x = x.fillna(0)
x

x = np.array(x)
x

y = np.array(y)
y = y.astype('int64')
y

dot_data = tree.export_graphviz(clf, out_file=None,
                     filled=True,    rounded=True,
                     )
graph = graphviz.Source(dot_data)
graph
