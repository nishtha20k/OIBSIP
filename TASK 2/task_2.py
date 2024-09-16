# -*- coding: utf-8 -*-
"""TASK 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fyMOOzlGKBgIxR1rHBl_E_kj6BbBMOtC

# **Libraries**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# **Data Analysis**"""

data = pd.read_csv("unemployment.csv")

data.head()

data.shape

data.info()

data.describe()

data.columns

data.columns = data.columns.str.strip()

data.isnull().sum()

plt.figure(figsize=(12, 8))

avg_unemployment = data.groupby(['Region', 'Date'])['Estimated Unemployment Rate (%)'].mean().reset_index()
pivot_data = avg_unemployment.pivot(index='Date', columns='Region', values='Estimated Unemployment Rate (%)')
pivot_data.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis')

plt.title('Average Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Average Estimated Unemployment Rate (%)')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

"""This bar plot represents the average estimated unemployment rate over time across various regions in India.

**Key Observations:**
1. **Peak Unemployment Periods**: The unemployment rate peaked notably in April 2020 and again in May 2020, which likely corresponds to the economic impact of the COVID-19 pandemic during the national lockdown in India. The sharp increase in unemployment during these months is clearly visible.

2. **Regional Variation**: The variation in the height of the bars for different dates indicates fluctuations in the average unemployment rate. Some regions, represented by specific colors, consistently contribute more to the overall unemployment rate.
"""

pivot_data = data.pivot(index='Date', columns='Region', values='Estimated Labour Participation Rate (%)')
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_data, cmap='YlGnBu', linewidths=0.5, linecolor='gray', annot=False)
plt.title('Heatmap of Labour Participation Rate Over Time by Region')
plt.xlabel('Region')
plt.ylabel('Date')
plt.show()

"""The heatmap visualizes the labor participation rate over time across different regions. Based on the color gradient, the key observations include:

1. **Regional Variations**: There are noticeable differences in labor participation rates among regions. Some regions consistently have higher participation rates (indicated by darker blue shades), while others have lower rates (lighter colors).

2. **Temporal Trends**: Over time, certain regions show fluctuations in labor participation, possibly influenced by external factors such as economic conditions or policy changes. For example, there are visible dips (lighter colors) in certain regions around specific dates, which might correlate with significant events like the COVID-19 pandemic.
"""

plt.figure(figsize=(12, 8))
sns.scatterplot(x='Estimated Employed', y='Estimated Unemployment Rate (%)', hue='Region', data=data)
plt.title('Employment vs. Unemployment Rate by Region')
plt.xlabel('Estimated Employed')
plt.ylabel('Estimated Unemployment Rate (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.show()