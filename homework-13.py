# ДЗ. Убрать из данных iris часть точек (на которых мы обучаемся) и убедиться, что на предсказание влияют только опорные вектора

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.svm import SVC

iris = sns.load_dataset("iris")

print(iris.head())

data = iris[["sepal_length", "petal_length", "species"]]
data_df = data[(data["species"] == "setosa") | (data["species"] == "versicolor")]

X = data_df[["sepal_length", "petal_length"]]
y = data_df["species"]

data_df_setosa = data_df[data_df["species"] == "setosa"]
data_df_versicolor = data_df[data_df["species"] == "versicolor"]

fig, ax = plt.subplots(2, 1, sharex="col", sharey="row")

ax[0].scatter(data_df_setosa["sepal_length"], data_df_setosa["petal_length"])
ax[0].scatter(data_df_versicolor["sepal_length"], data_df_versicolor["petal_length"])

model = SVC(kernel='linear', C=10000)
model.fit(X, y)

print(model.support_vectors_)

data_df_setosa_new = data_df[(data_df["species"] == "setosa") & ((data_df["sepal_length"] == model.support_vectors_[0][0])
                             | (data_df["sepal_length"] == model.support_vectors_[1][0]) | (data_df["sepal_length"] == model.support_vectors_[2][0]))]
data_df_versicolor_new = data_df[(data_df["species"] == "versicolor") & ((data_df["sepal_length"] == model.support_vectors_[0][0])
                             | (data_df["sepal_length"] == model.support_vectors_[1][0]) | (data_df["sepal_length"] == model.support_vectors_[2][0]))]

ax[1].scatter(data_df_setosa_new["sepal_length"], data_df_setosa_new["petal_length"])
ax[1].scatter(data_df_versicolor_new["sepal_length"], data_df_versicolor_new["petal_length"])

model_new = SVC(kernel='linear', C=10000)
model_new.fit(X, y)

print(model_new.support_vectors_)

ax[0].scatter(
    model.support_vectors_[:,0],
    model.support_vectors_[:,1],
    s=400,
    facecolor='none',
    edgecolors='black',
)

ax[1].scatter(
    model.support_vectors_[:,0],
    model.support_vectors_[:,1],
    s=400,
    facecolor='none',
    edgecolors='black',
)

x1_p = np.linspace(min(data_df["sepal_length"]),
                   max(data_df["sepal_length"]), 100)
x2_p = np.linspace(min(data_df["petal_length"]),
                   max(data_df["petal_length"]), 100)

X1_p, X2_p = np.meshgrid(x1_p, x2_p)

X_p = pd.DataFrame(
    np.vstack([X1_p.ravel(), X2_p.ravel()]).T,
    columns=["sepal_length", "petal_length"]
)

y_p = model.predict(X_p)

X_p["species"] = y_p

X_p_setosa = X_p[X_p["species"] == "setosa"]
X_p_versicolor = X_p[X_p["species"] == "versicolor"]

ax[0].scatter(X_p_setosa["sepal_length"], X_p_setosa["petal_length"], alpha=0.4)
ax[0].scatter(X_p_versicolor["sepal_length"], X_p_versicolor["petal_length"], alpha=0.4)


X_p_new = pd.DataFrame(
    np.vstack([X1_p.ravel(), X2_p.ravel()]).T,
    columns=["sepal_length", "petal_length"]
)

y_p_new = model_new.predict(X_p_new)

X_p_new["species"] = y_p_new

X_p_setosa_new = X_p_new[X_p_new["species"] == "setosa"]
X_p_versicolor_new = X_p_new[X_p_new["species"] == "versicolor"]

ax[1].scatter(X_p_setosa_new["sepal_length"], X_p_setosa_new["petal_length"], alpha=0.4)
ax[1].scatter(X_p_versicolor_new["sepal_length"], X_p_versicolor_new["petal_length"], alpha=0.4)

plt.show()

# Верхняя картинка показывает предсказание модели в случае полного набора данных iris.
# Нижняя картинка показывает предсказание модели в случае обрезанного набора данных iris 
# (оставлена только малая часть точек, включающая опорные вектора для полного набора данных).
# Опорные вектора в обоих случаях совпадают. Из рисунка видно, что предсказания модели также совпадают.