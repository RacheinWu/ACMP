import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

data = pd.read_excel('data/水质2000个.xls')
data = data.drop(0)

# 数据预处理
from sklearn.preprocessing import StandardScaler
data_transform = StandardScaler().fit_transform(data)

data_transform = pd.DataFrame(data=data, columns=list(data.columns))

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
plt.style.use('ggplot')

X = data_transform[['COD', 'DO']]

# 绘制特征1与特征2的散点图
data_transform.plot(x='COD',y='DO',kind='scatter')
plt.show()

# DBSCANS
dbscans = DBSCAN(eps=0.075, min_samples=6)
cluster = dbscans.fit_predict(X)

# 可视化
plt.scatter(x = X.iloc[:,0], y = X.iloc[:,1], c=cluster, cmap="rainbow")
plt.xlabel("COD")
plt.ylabel("DO")
plt.show()

# kmeans
# num_clusters = 5
# kmeans = KMeans(n_clusters=num_clusters, random_state=1)
# kmeans.fit(X)
#
# # 聚类结果标签
# data_transform['cluster'] = kmeans.labels_
# # 聚类中心
# centers = kmeans.cluster_centers_
#
# # 绘制散点图
# plt.scatter(x = X.iloc[:,0], y = X.iloc[:,1], c = data_transform['cluster'], s=50, cmap='rainbow')
# plt.scatter(centers[:,0], centers[:,1], c='k', marker = '*', s = 180)
# plt.xlabel('COD')
# plt.ylabel('DO')
# # 图形显示
# plt.show()