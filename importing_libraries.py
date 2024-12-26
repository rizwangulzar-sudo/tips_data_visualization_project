# importing libraries pandas and matplotlib
import matplotlib.pyplot as plt

import seaborn as sns
df = sns.load_dataset('tips')
print(df.head())

# sns.barplot(x='day', y='total_bill', data=df)
# plt.show()

# creating Scatter Plot
# sns.scatterplot(x='total_bill', y='tip', data=df)
# plt.show()

# creating Line Plot
# sns.lineplot(x='size', y='total_bill', data=df)
# plt.show()

# creating Histogram (Distribution Plot)
# sns.histplot(df['total_bill'], bins=20, kde=True)
# plt.show()

# creating Box Plot
# sns.boxplot(x='day', y='total_bill', data=df)
# plt.show()

# Non-numeric columns ko remove karna
df_numeric = df.select_dtypes(include=['number'])
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm')
plt.show()

# creating Heatmap
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
# plt.show()



