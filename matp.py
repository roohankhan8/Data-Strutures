import matplotlib.pyplot as plt
import pandas as pd

# df=pd.Series([1,2,3,4,5,6,7])
df=pd.read_csv('csv/the-heart-failure-prediction-pakistan.csv')
# df.set_index('Age', inplace=True)
# df.plot(kind='bar')
df[df['Age']>50][['Follow.Up', 'Reaction']].plot(kind='bar', stacked=True)
# print(df)
plt.savefig('heart2.png')

'''
kind = 
hist bins, 
bar stacked, 
box
area stacked
scatter x=a y=b
pie (up to 6 categories)
legend=True False
color=[]

plt.
xlabel
ylabel
suptitle


stacked true or false

'''