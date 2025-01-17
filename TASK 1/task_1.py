# -*- coding: utf-8 -*-
"""TASK 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fyMOOzlGKBgIxR1rHBl_E_kj6BbBMOtC

# **Libraries**
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

"""# **Dataset and it's information**"""

data=pd.read_csv('iris.csv')

data.head()

data.shape

data.info()

data['Species'].unique()

data.describe()

"""# **Data Cleaning**"""

data=data.iloc[:,1:]

data.isnull().sum()

le= LabelEncoder()

data['Species']= le.fit_transform(data['Species'])
data.head()

# 'setosa' == 0, 'versicolor' == 1, 'virginica' == 2
data['Species'].unique()

"""# **Training and Testing**"""

x=data.drop(columns=['Species'])
y=data['Species']

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.3)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")