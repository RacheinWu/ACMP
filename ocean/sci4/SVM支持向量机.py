import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# 读入数据
data = pd.read_csv("data/volcano_with_label.csv")
# print(data.columns)
target = data['类别']
data_train = data.drop(columns=['类别'], axis=1)
# 划分训练集和测试集data.columns
X_train, X_test, label_train, label_test = train_test_split(data_train, target, test_size=0.3)

