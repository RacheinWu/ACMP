import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn .tree import DecisionTreeClassifier
import graphviz
import matplotlib.pyplot as plt

# 读入数据
data = pd.read_csv("data/volcano_with_label.csv")
# print(data.columns)
target = data['类别']
data_train = data.drop(columns=['类别'], axis=1)
# 划分训练集和测试集data.columns
X_train, X_test, label_train, label_test = train_test_split(data_train, target, test_size=0.3)

# print(X_train)
# print(label_test)

# 建立模型
clf = DecisionTreeClassifier(criterion="entropy")
model = clf.fit(X_train, label_train)
score = clf.score(X_test, label_test)
print(score)


feature_names = ['GR', 'TH', 'U', 'K', 'Pe', 'CNL', 'DEN']
dot_data = tree.export_graphviz(model, out_file=None,
                                feature_names=feature_names,
                                class_names=target,
                                filled=True, rounded=True,
                              special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("岩石")