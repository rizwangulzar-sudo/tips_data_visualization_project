# importing libraries pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
df = sns.load_dataset('tips')
print(df.head())

sns.barplot(x='day', y='total_bill', data=df)
plt.show()