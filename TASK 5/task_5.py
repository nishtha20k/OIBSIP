# -*- coding: utf-8 -*-
"""TASK 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fyMOOzlGKBgIxR1rHBl_E_kj6BbBMOtC

# **Libraries**
"""

import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

"""# **Dataset, it's cleaning and analysis**"""

df = pd.read_csv('Advertising.csv')
df

df = df.drop(["Unnamed: 0"],axis=1)
df

df.size

df.shape

df.info()

df.isnull().sum()

df.describe()

sns.heatmap(df.corr(),annot=True)

"""# **Model Training and Testing**"""

x = df.iloc[:, 0:3]
y = df.iloc[:, -1]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)

from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

from sklearn import metrics

print('Mean Absolute Error: ', metrics.mean_absolute_error(y_pred, y_test))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_pred, y_test)))
print('R-Squared: ', metrics.r2_score(y_pred, y_test))

act_pred = pd.DataFrame({'Actual':y_test.values.flatten(), 'Predict':y_pred.flatten()})
act_pred