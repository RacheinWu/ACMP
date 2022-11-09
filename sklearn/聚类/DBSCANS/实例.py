from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 数据预处理
# scaler = StandardScaler()
# X_scaler = scaler.fit_transform(X)

dbscan = DBSCAN(eps=0.123, min_samples=2)  # eps：radius半径距离，在r范围的radius region 的点进行分析；min_samples：最小样本数
# cluster = dbscan.fit_predict(X_scaler)  # 开始预测

# 可视化
# plt.scatter(X[:, 0], X[:, 1], c=cluster, cmap="plasma")
# plt.xlabel("")
# plt.ylabel("")
