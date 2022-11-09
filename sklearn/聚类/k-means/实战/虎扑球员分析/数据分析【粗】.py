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
