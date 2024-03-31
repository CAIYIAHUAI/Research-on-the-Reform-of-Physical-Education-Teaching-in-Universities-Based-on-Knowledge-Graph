analysis = pd.read_excel(r"C:\Users\Yihuai Cai\Desktop\最终.xlsx")
analysis.head()

analysis = analysis.drop(columns=['文物采样点','纹饰','类型','颜色','总含量'])
print(analysis.shape)
analysis.head()

#表面风化数字化
for i in range(67):
    if  analysis.iloc[i,0] == '无风化':
        analysis.iloc[i,0] = 0
    elif analysis.iloc[i,0] == '风化':
        analysis.iloc[i,0] = 1

analysis.head()

result = pd.DataFrame()

result.shape[1]

analysis = analysis.astype('float64')
for i in range(1, 15):
    print(i)
    analysis.iloc[:, i] += 5
    #     analysis = np.array(analysis)
    prediction = np.around(model1.predict(analysis))
    print('add5%:')
    # 转为Dataframe
    prediction = pd.DataFrame(prediction)
    prediction.insert(2, '类型', 0)
    # 把第3列变成中文类型
    for j in range(67):
        if prediction.iloc[j, 0] == 0.0:
            prediction.iloc[j:, 2] = '高钾'
        else:
            prediction.iloc[j:, 2] = '铅钡'
    # 丢掉其他列，只保留中文类型那一列
    prediction = prediction.drop(columns=[0, 1])
    # 将结果插入result
    result.insert(result.shape[1], '类型', prediction.iloc[:, 0], allow_duplicates=True)
    #     print(prediction)

    #     analysis = pd.DataFrame(analysis)
    analysis.iloc[:, i] -= 5
    analysis.iloc[:, i] += 10
    #     analysis = np.array(analysis)
    prediction = np.around(model1.predict(analysis))
    print('add10%:')
    # 转为Dataframe
    prediction = pd.DataFrame(prediction)
    prediction.insert(2, '类型', 0)
    # 把第3列变成中文类型
    for k in range(67):
        if prediction.iloc[k, 0] == 0.0:
            prediction.iloc[k:, 2] = '高钾'
        else:
            prediction.iloc[k:, 2] = '铅钡'
    # 丢掉其他列，只保留中文类型那一列
    prediction = prediction.drop(columns=[0, 1])
    # 将结果插入result
    result.insert(result.shape[1], '类型', prediction.iloc[:, 0], allow_duplicates=True)
    #     print(prediction)
    #     analysis = pd.DataFrame(analysis)
    analysis.iloc[:, i] -= 10
    analysis.iloc[:, i] += 50
    #     analysis = np.array(analysis)
    prediction = np.around(model1.predict(analysis))
    print('add20%:')
    # 转为Dataframe
    prediction = pd.DataFrame(prediction)
    prediction.insert(2, '类型', 0)
    # 把第3列变成中文类型
    for l in range(67):
        if prediction.iloc[l, 0] == 0.0:
            prediction.iloc[l:, 2] = '高钾'
        else:
            prediction.iloc[l:, 2] = '铅钡'
    # 丢掉其他列，只保留中文类型那一列
    prediction = prediction.drop(columns=[0, 1])
    # 将结果插入result
    result.insert(result.shape[1], '类型', prediction.iloc[:, 0], allow_duplicates=True)
    #     print(prediction)
    #     analysis = pd.DataFrame(analysis)
    analysis.iloc[:, i] -= 50

result.to_excel(r"C:\Users\Yihuai Cai\Desktop\敏感性临时.xlsx")