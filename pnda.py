import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

data1 = pd.read_csv('C:/Users/HP/Downloads/Customer.csv', header=0)

pd.set_option('display.expand_frame_repr', False)
print(data1.head(10))
data2 = pd.read_csv('C:/Users/HP/Downloads/Customer.csv', header=0, index_col=0)
print(data2.head())
print(data1.describe())
print(data1.iloc[0])
print(data2.loc["CG-12520"])
print(data1.iloc[0:5:2])
print(sns.distplot(data2.Age))

plt.show()
print(sns.distplot(data2.Age, kde=False))
plt.show()
print(sns.distplot(data2.Age, kde=False,color="red"))
plt.show()
iris=sns.load_dataset("iris")
print(iris.head())