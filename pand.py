
import pandas as pd 
data={
    'age': [14,15,16,17],
    'heights':[5.5,5.6,5.7,6]
}

df=pd.DataFrame(data, index=['James','Bob','Amy','Dave'])
#print(df)
#print(df.loc['Bob'])

'''
df[column]

At certain index
df.iloc[index]

Conditions
df[(df[column]>20) & (df[column]<40)]

Reading
head()
tail()
info()
set_index(col, inplace=True)
drop(row, axis,inplace=true)
axis 1 drops col and axis 0 drops row
describe()
value_counts()
groupby()[]
sum()
'''
# a=pd.read_csv('the-heart-failure-prediction-pakistan.csv')
b=pd.read_csv('Sample-Spreadsheet-100-rows.csv')
#a['month'] = pd.to_datetime(a['Period'], format='mixed').dt.month_name()

#df.drop('state', axis=1, inplace=True)

a.set_index('Age', inplace=True)
#print(a.head(10))
print(b.head(10))