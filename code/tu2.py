import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.cluster.kmeans import KMeansClusterer
from nltk.cluster.util import cosine_distance
from collections import Counter

a=[26,31,31,32,34,24,37,98,173,532]
a2019=[0,0,0,0]
a2018=[0,0,0,0]
a2017=[0,0,0,0]
a2016=[0,0,0,0]
a2015=[0,0,0,0]
a2014=[0,0,0,0]
a2013=[0,0,0,0]
a2012=[0,0,0,0]
a2011=[0,0,0,0]
a2010=[0,0,0,0]
with open('resultData/ClusterText.txt', "r", encoding='utf-8') as fr:
    lines = fr.readlines()
for line in lines:
    line = line.strip('\n')
    line = line.split('\t')
    if int(line[0])<a[9]:#2019
        if line[1]=='0':
            a2019[0]=a2019[0]+1
        elif line[1]=='1':
            a2019[1]=a2019[1]+1
        elif line[1]=='2':
            a2019[2]=a2019[2]+1
        else:
            a2019[3]=a2019[3]+1

    if int(line[0])<a[9]+a[8] and int(line[0])>=a[9]:#2018
        if line[1]=='0':
            a2018[0]=a2018[0]+1
        elif line[1]=='1':
            a2018[1]=a2018[1]+1
        elif line[1]=='2':
            a2018[2]=a2018[2]+1
        else:
            a2018[3]=a2018[3]+1

    if int(line[0])<a[9]+a[8]+a[7] and int(line[0])>=a[9]+a[8]:#2017
        if line[1]=='0':
            a2017[0]=a2017[0]+1
        elif line[1]=='1':
            a2017[1]=a2017[1]+1
        elif line[1]=='2':
            a2017[2]=a2017[2]+1
        else:
            a2017[3]=a2017[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6] and int(line[0])>=a[9]+a[8]+a[7]:#2016
        if line[1]=='0':
            a2016[0]=a2016[0]+1
        elif line[1]=='1':
            a2016[1]=a2016[1]+1
        elif line[1]=='2':
            a2016[2]=a2016[2]+1
        else:
            a2016[3]=a2016[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6]+a[5] and int(line[0])>=a[9]+a[8]+a[7]+a[6]:#2015
        if line[1]=='0':
            a2015[0]=a2015[0]+1
        elif line[1]=='1':
            a2015[1]=a2015[1]+1
        elif line[1]=='2':
            a2015[2]=a2015[2]+1
        else:
            a2015[3]=a2015[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6]+a[5]+a[4] and int(line[0])>=a[9]+a[8]+a[7]+a[6]+a[5]:#2014
        if line[1]=='0':
            a2014[0]=a2014[0]+1
        elif line[1]=='1':
            a2014[1]=a2014[1]+1
        elif line[1]=='2':
            a2014[2]=a2014[2]+1
        else:
            a2014[3]=a2014[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3] and int(line[0])>=a[9]+a[8]+a[7]+a[6]+a[5]+a[4]:#2013
        if line[1]=='0':
            a2013[0]=a2013[0]+1
        elif line[1]=='1':
            a2013[1]=a2013[1]+1
        elif line[1]=='2':
            a2013[2]=a2013[2]+1
        else:
            a2013[3]=a2013[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2] and int(line[0])>=a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]:#2012
        if line[1]=='0':
            a2012[0]=a2012[0]+1
        elif line[1]=='1':
            a2012[1]=a2012[1]+1
        elif line[1]=='2':
            a2012[2]=a2012[2]+1
        else:
            a2012[3]=a2012[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2]+a[1] and int(line[0])>=a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2]:#2011
        if line[1]=='0':
            a2011[0]=a2011[0]+1
        elif line[1]=='1':
            a2011[1]=a2011[1]+1
        elif line[1]=='2':
            a2011[2]=a2011[2]+1
        else:
            a2011[3]=a2011[3]+1

    if int(line[0])<a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2]+a[1]+a[0] and int(line[0])>=a[9]+a[8]+a[7]+a[6]+a[5]+a[4]+a[3]+a[2]+a[1]:#a010
        if line[1]=='0':
            a2010[0]=a2010[0]+1
        elif line[1]=='1':
            a2010[1]=a2010[1]+1
        elif line[1]=='2':
            a2010[2]=a2010[2]+1
        else:
            a2010[3]=a2010[3]+1
print(a2010)
print(a2011)
print(a2012)
print(a2013)
print(a2014)
print(a2015)
print(a2016)
print(a2017)
print(a2018)
print(a2019)
