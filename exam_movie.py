import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
de = pd.read_csv(r'C:\Users\HP\Desktop\Matter\python\machinelearning\Movie_collection_train.csv', header=0)
pd.set_option('display.expand_frame_repr', False)
print(de.head())
print(de.shape)
print(de.describe())
#Missing values in Time_taken
#negative skewness in Marketin_expense or outliers and Twitter_hashtags
"""
 print(sns.jointplot(x='Budget',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Marketin_expense',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Production_expense',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Multiplex_coverage',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Movie_length',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Lead_ Actor_Rating',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Lead_Actress_rating',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Director_rating',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Producer_rating',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Critic_rating',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Trailer_views',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Time_taken',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Twitter_hastags',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Avg_age_actors',y='Collection',data=de))
plt.show()
print(sns.jointplot(x='Num_multiplex',y='Collection',data=de))
plt.show()
#Time_taken, Twitter_hastags,Avg_age_actors have outliers

print(de.info())
print(np.percentile(de.Marketin_expense,[99])[0])
uv=np.percentile(de.Marketin_expense,[99])[0]
print(de[(de.Marketin_expense>uv)])
print(de.Marketin_expense[(de.Marketin_expense > uv*3)])

t=de.Marketin_expense[(de.Marketin_expense>uv*3)]=uv*3
print(t)
print(de[(de.Marketin_expense>uv)])
print(de.info())
print(de.describe())
print("/n")
print(np.percentile(de.Twitter_hastags,[99])[0])
ub=np.percentile(de.Twitter_hastags,[99])[0]
print(de[(de.Twitter_hastags>ub)])
print(de.Twitter_hastags[(de.Twitter_hastags > ub*3)])

l=de.Twitter_hastags[(de.Twitter_hastags>ub*3)]=ub*3
print(l)
print(de[(de.Twitter_hastags>ub)])
print(de.describe())

print(np.percentile(de.Time_taken,[1])[0])
lv=np.percentile(de.Time_taken,[1])[0]
da=de[(de.Time_taken<lv)]
print(da)
de.Time_taken[(de.Time_taken< 0.3*lv)]=0.3*lv
dte=de[de.Time_taken<lv]
print(dte)

print(de.describe())


print(np.percentile(de.Avg_age_actors,[1])[0])
lv=np.percentile(de.Avg_age_actors,[1])[0]
da=de[(de.Avg_age_actors<lv)]
print(da)
de.Avg_age_actors[(de.Avg_age_actors< 0.3*lv)]=0.3*lv
dte=de[de.Avg_age_actors<lv]
print(dte)

print(de.describe())

print(de.info())
de.Time_taken=de.Time_taken.fillna(de.Time_taken.mean())
print(de.info())
"""
print(sns.jointplot(x="Marketin_expense",y="Collection",data=de))
plt.show()
de.Marketin_expense=np.log(1+de.Marketin_expense)
print(sns.jointplot(x="Marketin_expense",y="Collection",data=de))
plt.show()
del de['MPAA_film_rating']