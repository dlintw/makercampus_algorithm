import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# 加載數據集
iris = datasets.load_iris()
X = iris.data[:, :2]  # 取前兩個特徵
y = iris.target

# 將數據集分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 訓練決策樹模型
tree = DecisionTreeClassifier(max_depth=3)
tree.fit(X_train, y_train)

# 預測
y_pred = tree.predict(X_test)

# 計算準確率
accuracy = accuracy_score(y_test, y_pred)
print(f"準確率: {accuracy}")

# 繪製決策樹
plt.figure(figsize=(20,10))
plot_tree(tree, filled=True, feature_names=iris.feature_names[:2], class_names=iris.target_names)
plt.show()
