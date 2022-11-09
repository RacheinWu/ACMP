import pandas as pd
from sklearn import tree
from sklearn .tree import DecisionTreeClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import graphviz
import matplotlib.pyplot as plt

# 导入数据集
wine = load_wine()
data = pd.concat([pd.DataFrame(wine.data, columns=wine.feature_names),pd.DataFrame(wine.target)],axis=1)

# 划分训练集和测试集
"""
    train_data 数据集
    train_target 划分的样本结果w
"""
X_train, X_test, Y_train, Y_test = train_test_split(wine.data, wine.target, train_size=0.3)
# 建立模型
clf = DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X_train, Y_train)
score = clf.score(X_test, Y_test)
print(score)

