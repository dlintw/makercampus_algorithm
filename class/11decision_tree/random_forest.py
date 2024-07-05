from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# 加載數據集
iris = datasets.load_iris()
X = iris.data[:, :2]  # 取前兩個特徵
y = iris.target

# 將數據集分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# 訓練隨機森林模型
forest = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
forest.fit(X_train, y_train)

# 預測
y_pred_forest = forest.predict(X_test)

# 計算準確率
accuracy_forest = accuracy_score(y_test, y_pred_forest)
print(f"隨機森林準確率: {accuracy_forest}")

# 繪製隨機森林中的一棵樹
plt.figure(figsize=(20,10))
plot_tree(forest.estimators_[0], filled=True, feature_names=iris.feature_names[:2], class_names=iris.target_names)
plt.show()
