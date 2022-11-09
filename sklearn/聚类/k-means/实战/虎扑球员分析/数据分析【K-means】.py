import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 从data数据集中读取
players = pd.read_excel('data/data.xls')


# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
plt.style.use('ggplot')

# 绘制得分与命中率的散点图
players.plot(x='罚球命中率',y='命中率',kind='scatter')
plt.show()

# 选择最好的K值（多少类）
X = players[['罚球命中率', '命中率']]
K = range(1, int(np.sqrt(players.shape[0])))
res = []
for k in K:
    SSE = []
    kmeans = KMeans(n_clusters=k, random_state=10)
    kmeans.fit(X)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    for label in set(labels):
        SSE.append(np.sum(np.sum((players[['罚球命中率', '命中率']].loc[labels == label,]-centers[label,:]) **2)))
    res.append(np.sum(SSE))

# 绘制K的个数与res的关系
plt.plot(K, res, 'b*-')
plt.xlabel('聚类个数')
plt.ylabel('簇内离差平方和')
plt.title('选择最优的聚类个数')
plt.show()

#调用sklearn的库函数
num_clusters = 6
kmeans = KMeans(n_clusters=num_clusters, random_state=1)
kmeans.fit(X)

# 聚类结果标签
players['cluster'] = kmeans.labels_
# 聚类中心
centers = kmeans.cluster_centers_

# 绘制散点图
plt.scatter(x = X.iloc[:,0], y = X.iloc[:,1], c = players['cluster'], s=50, cmap='rainbow')
plt.scatter(centers[:,0], centers[:,1], c='k', marker = '*', s = 180)
plt.xlabel('罚球命中率')
plt.ylabel('命中率')
# 图形显示
plt.show()
