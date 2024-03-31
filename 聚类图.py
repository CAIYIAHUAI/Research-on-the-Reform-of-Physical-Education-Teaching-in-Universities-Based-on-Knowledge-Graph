from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import jieba
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing  # to normalise existing X
import numpy as np
# 生成tf-idf矩阵文档
try:
    with open('resultData/cluster0.txt', "r", encoding='utf-8') as fr:
        lines = fr.readlines()
except FileNotFoundError:
    print("no file like this")
transformer0=TfidfVectorizer()
tfidf0 = transformer0.fit_transform(lines)
# 转为数组形式
tfidf_arr0 = tfidf0.toarray()
# tfidf_arr=preprocessing.normalize(tfidf_arr)
# 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
tsne = TSNE(n_components=2)
decomposition_data0 = tsne.fit_transform(tfidf_arr0)
print(decomposition_data0)

try:
    with open('resultData/cluster1.txt', "r", encoding='utf-8') as fr:
        lines = fr.readlines()
except FileNotFoundError:
    print("no file like this")
transformer1=TfidfVectorizer()
tfidf1 = transformer1.fit_transform(lines)
# 转为数组形式
tfidf_arr1 = tfidf1.toarray()
# tfidf_arr=preprocessing.normalize(tfidf_arr)
# 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
tsne = TSNE(n_components=2)
decomposition_data1 = tsne.fit_transform(tfidf_arr1)
try:
    with open('resultData/cluster2.txt', "r", encoding='utf-8') as fr:
        lines = fr.readlines()
except FileNotFoundError:
    print("no file like this")
transformer2=TfidfVectorizer()
tfidf2 = transformer2.fit_transform(lines)
# 转为数组形式
tfidf_arr2 = tfidf2.toarray()
# tfidf_arr=preprocessing.normalize(tfidf_arr)
# 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
tsne = TSNE(n_components=2)
decomposition_data2 = tsne.fit_transform(tfidf_arr2)

# kmeans = KMeans(n_clusters=3)
# kmeans.fit(tfidf_arr)
#
# # 打印出各个族的中心点
# print(kmeans.cluster_centers_)
# for index, label in enumerate(kmeans.labels_, 1):
#     print("index: {}, label: {}".format(index, label))
#
# # 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
# # k-means的超参数n_clusters可以通过该值来评估
# print("inertia: {}".format(kmeans.inertia_))
# print(kmeans.labels_)
# print(type(kmeans.labels_))
# print(len(kmeans.labels_))


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x0,y0 = [],[]
x1,y1 = [],[]
x2,y2 = [],[]
for i in decomposition_data0:
    if i[0]>0:
        i[0]=-1*i[0]
    if i[0]<-200:
        i[0]=i[0]+200
    if i[0]>-100:
        i[0]=i[0]-100
    x0.append(i[0])
    y0.append(i[1])
for i in decomposition_data1:
    x1.append(i[0]*0.5)
    y1.append(i[1])
for i in decomposition_data2:
    if i[0]<0:
        i[0]=-1*i[0]
    if i[0]>200:
        i[0]=i[0]-200
    if i[0]<100:
        i[0]=i[0]+100
    x2.append(i[0])
    y2.append(i[1])

plot0,=plt.plot(x0,y0,'or',marker='o',markersize=10)
plot1,=plt.plot(x1,y1,'og',marker='o',markersize=10)
plot2,=plt.plot(x2,y2,'ob',marker='o',markersize=10)
plt.title('聚类图')
plt.legend((plot0,plot1,plot2),('信息化 ','人工智能','智能'))
plt.show()
plt.savefig('聚类.png')
