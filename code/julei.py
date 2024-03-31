import jieba
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
import jieba
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing  # to normalise existing X
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.cluster.kmeans import KMeansClusterer
from nltk.cluster.util import cosine_distance
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
# jieba分词 精确模式
a=[]

def get_jiebaword():
	# enconding视文本保存的编码而定，utf-8或gbk
    try:
        with open('sourceData/AI_teach.txt', "r", encoding='utf-8') as fr:
            lines = fr.readlines()
    except FileNotFoundError:
        print("no file like this")
    jiebaword = []
    for line in lines:
        line = line.strip('\n')
        # 清除多余的空格
        line = "".join(line.split())
        # 默认精确模式
        seg_list = jieba.cut(line, cut_all=False)
        word = "/".join(seg_list)
        jiebaword.append(word)
    return jiebaword

# 获取停用词表
def get_stopword():
    stopword = []
    try:
        with open('sourceData/StopWord.txt', "r", encoding='utf-8') as fr:
            lines = fr.readlines()
    except FileNotFoundError:
        print("no file like this")
    for line in lines:
        line = line.strip('\n')
        stopword.append(line)
    return stopword
# 去除停用词
def clean_stopword(jiebaword,stopword):
    fw = open('resultData/CleanWords.txt', 'a+',encoding='utf-8')#先把a+改成r
    for words in jiebaword:
        words = words.split('/')
        for word in words:
            if word not in stopword:
                fw.write(word + '\t')
        fw.write('\n')
    fw.close()

# 生成tf-idf矩阵文档
def get_tfidf():
    try:
        with open('resultData/CleanWords.txt', "r", encoding='utf-8') as fr:
            lines = fr.readlines()
    except FileNotFoundError:
        print("no file like this")
    transformer=TfidfVectorizer()
    tfidf = transformer.fit_transform(lines)
    # 转为数组形式
    tfidf_arr = tfidf.toarray()
    return tfidf_arr

# K-means聚类
def get_cluster(tfidf_arr,k):
    # 转为数组形式
    kmeans = KMeansClusterer(num_means=k, distance=cosine_distance)  # 分成k类，使用余弦相似分析
    kmeans.cluster(tfidf_arr)
    # 获取分类
    kinds = pd.Series([kmeans.classify(i) for i in tfidf_arr])
    # print(kinds)
    #先a+改成w
    fw = open('resultData/ClusterText.txt', 'a+', encoding='utf-8')
    for i, v in kinds.items():
        fw.write(str(i) + '\t' + str(v) + '\n')
    fw.close()
# 获取分类文档
def cluster_text():
    index_cluser = []
    try:
        with open('resultData/ClusterText.txt', "r", encoding='utf-8') as fr:
            lines = fr.readlines()
    except FileNotFoundError:
        print("no file like this")
    for line in lines:
        line = line.strip('\n')
        line = line.split('\t')
        index_cluser.append(line)
    # index_cluser[i][j]表示第i行第j列
    try:
        with open('resultData/CleanWords.txt', "r", encoding='utf-8') as fr:
            lines = fr.readlines()
    except FileNotFoundError:
        print("no file like this")
    for index,line in enumerate(lines):
        for i in range(50):
            if str(index) == index_cluser[i][0]:
                # print(index_cluser[i][1])
                fw = open('resultData/cluster' + index_cluser[i][1] + '.txt', 'a+', encoding='utf-8')
                fw.write(line)
    fw.close()
# 获取主题词
def get_title(cluster):
    for i in range(cluster):
        try:
            with open('resultData/cluster' + str(i) + '.txt', "r", encoding='utf-8') as fr:
                lines = fr.readlines()
        except FileNotFoundError:
            print("no file like this")
        all_words = []
        for line in lines:
            line = line.strip('\n')
            line = line.split('\t')
            for word in line:
                all_words.append(word)
        c = Counter()
        for x in all_words:
            if len(x) > 1 and x != '\r\n':
                c[x] += 1
        print('主题' + str(i+1) + '\n词频统计结果：')
        # 输出词频最高的那个词，也可以输出多个高频词
        for (k, v) in c.most_common(5):
            global a
            a.append(k)
            print(k,':',v)

if __name__ == '__main__':
	# 定义聚类的个数
    cluster = 2

    # # 结巴分词
    jiebaword = get_jiebaword()
    # # 获取停用词
    stopword = get_stopword()
    # # ---停用词补充,视具体情况而定---
    stopword.append('<')
    stopword.append('>')
    stopword.append(',')
    i = 0
    for i in range(19):
        stopword.append(str(10+i))
    # ----------------------
    # # 去除停用词
    # clean_stopword(jiebaword,stopword)
    # 获取tfidf矩阵
    tfidf_arr = get_tfidf()
    # ---输出测试---
    # print(tfidf_arr)
    # print(tfidf_arr.shape)
    # -------------
    # K-means聚类
    get_cluster(tfidf_arr,cluster)
    # # 获取分类文件
    cluster_text()
    # # 统计出主题词
    get_title(cluster)


    # 使用T-SNE算法，对权重进行降维，准确度比PCA算法高，但是耗时长
    tsne = TSNE(n_components=2)
    decomposition_data = tsne.fit_transform(tfidf_arr)
    x0, y0 = [], []
    x1, y1 = [], []
    x2, y2 = [], []
    try:
        with open('resultData/ClusterText.txt', "r", encoding='utf-8') as fr:
            lines = fr.readlines()
    except FileNotFoundError:
        print("no file like this")
    for line in lines:
        line = line.strip('\n')
        line = line.split('\t')
        if line[1]=='0':
            num=int(line[0])
            decomposition_data0=decomposition_data[num]
            x0.append(decomposition_data0[0])
            y0.append(decomposition_data0[1])
        if line[1]=='1':
            num=int(line[0])
            decomposition_data0=decomposition_data[num]
            x1.append(decomposition_data0[0])
            y1.append(decomposition_data0[1])
        if line[1]=='2':
            num=int(line[0])
            decomposition_data0=decomposition_data[num]
            x2.append(decomposition_data0[0])
            y2.append(decomposition_data0[1])
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plot0, = plt.plot(x0, y0, 'or', marker='o', markersize=10)
    plot1, = plt.plot(x1, y1, 'og', marker='o', markersize=10)
    plot2, = plt.plot(x2, y2, 'ob', marker='o', markersize=10)
    plt.title('聚类图')
    plt.legend((plot0, plot1, plot2), (a[0], a[1], a[2]))
    plt.show()
    plt.savefig('聚类.png')