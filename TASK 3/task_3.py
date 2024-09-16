# -*- coding: utf-8 -*-
"""TASK 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fyMOOzlGKBgIxR1rHBl_E_kj6BbBMOtC

# **Libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

"""# **Data Extraction and Analysis**"""

df = pd.read_csv('car_data.csv')

df.head()

df.shape

df.info()

df.describe().style.format(precision=2)

df.isnull().sum()

df.duplicated().sum()

numerical_columns = ['Year', 'Selling_Price', 'Present_Price', 'Driven_kms', 'Owner']
numerical_df = df[numerical_columns]
correlation_matrix = numerical_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (Numerical Columns)')
plt.show()

print(df['Fuel_Type'].value_counts())

print(df['Selling_type'].value_counts())

print(df['Transmission'].value_counts())

"""# **Data Cleaning**"""

df = df.drop_duplicates()
df.duplicated().sum()

# Encoding "Fuel_Type" Column
df.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)
# Encoding "Seller_Type" Column
df.replace({'Selling_type':{'Dealer':0,'Individual':1}},inplace=True)
# Encoding "Transmission" Column
df.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

"""# **Model**"""

X = df.drop(['Car_Name','Selling_Price'],axis=1)
Y = df['Selling_Price']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R-squared:', r2)

new_car = [[2022, 20000, 0, 1, 1, 0, 0]]  # Example new car data
predicted_price = model.predict(new_car)
print('Predicted Selling Price:', predicted_price[0])