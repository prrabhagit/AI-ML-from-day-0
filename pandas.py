
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'], dtype='int64')
### CREATION OD DATAFRAME (datatype:dictionary)
df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'A'],
    'age': [20, 21, 22, 20],
    'score': [80, 85, 90, 88],
    'city': ['X', 'Y', 'X', 'Z'],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'tags': [['ml', 'ai'], ['ai'], ['ds'], ['ml', 'ds']]
})
#inspection for data for:
df.head() ## first row
df.tail() ##last row 
df.sample() ##random
df.shape ##rows, columns
df.size ##total elements
df.ndim #size of elements
df.columns # column names
df.index  ## index
df.values ##Numpy array
df.info() ##summary about it
df.describe() ##statistics
df.describe(include='all') ##all columns
df.dtypes ## datatypes

df['age']
df[['name', 'score']]
df.loc[0]
df.iloc[0]
df.loc[:, ['name', 'age']]
df.iloc[0:2, 1:3]
df.at[0, 'score']
df.iat[0, 2]

df[df['age'] > 20]
df.query("age > 20 and score > 85")

df['passed'] = df['score'] > 85
df['age'] = df['age'].astype('int32')
df['score_norm'] = (df['score'] - df['score'].mean()) / df['score'].std()
df.assign(rank=lambda x: x['score'].rank())

df.drop('rank', axis=1, errors='ignore')
df.drop([0], axis=0)
df.drop_duplicates()
df.duplicated()

df.isna()
df.notna()
df.fillna(0)
df.fillna(method='ffill')
df.fillna(method='bfill')

df.sort_values('score')
df.sort_values(['city', 'score'], ascending=[True, False])
df.sort_index()

df.groupby('city').mean(numeric_only=True)
df.groupby('city')['score'].agg(['mean', 'max', 'min', 'count'])
df.groupby(['city', 'passed']).size()

df['score'].sum()
df['score'].mean()
df['score'].median()
df['score'].mode()
df['score'].std()
df['score'].var()
df['score'].quantile(0.75)

df['score'].apply(lambda x: x + 5)
df.apply(np.sum, axis=0)
df.apply(np.mean, axis=1)

df['name'].map({'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma'})
df.replace({'city': {'X': 'CityX'}})

df['name'].str.upper()
df['name'].str.lower()
df['name'].str.contains('A')
df['name'].str.len()
df['name'].str.replace('A', 'X')

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.weekday

df.set_index('id')
df.reset_index()
df.rename(columns={'score': 'marks'})
df.rename(index={0: 'row0'})

df['city'].value_counts()
df['city'].unique()
df['city'].nunique()

pd.cut(df['score'], bins=3)
pd.qcut(df['score'], q=3)

df['city'] = df['city'].astype('category')
df['city'].cat.categories
df['city'].cat.codes

df.explode('tags')

df['score'].rolling(2).mean()
df['score'].expanding().mean()
df['score'].ewm(alpha=0.5).mean()

df.corr(numeric_only=True)
df.cov(numeric_only=True)

pd.crosstab(df['city'], df['passed'])

df.eval("score_plus_age = score + age")
df.query("score > 85")

df.pipe(lambda x: x.assign(double_score=x['score'] * 2))

df.memory_usage()
df.astype({'age': 'int64'})

df1 = df[['id', 'score']]
df2 = df[['id', 'age']]
pd.merge(df1, df2, on='id', how='inner')
pd.merge(df1, df2, on='id', how='left')
pd.merge(df1, df2, on='id', how='right')
pd.merge(df1, df2, on='id', how='outer')

df1.join(df2.set_index('id'), on='id'

pd.concat([df1, df2])
pd.concat([df1, df2], axis=1)

df.pivot(index='name', columns='city', values='score')
pd.pivot_table(df, values='score', index='city', aggfunc='mean')

pd.melt(df, id_vars=['id', 'name'])

df.to_csv('out.csv', index=False)
df.to_excel('out.xlsx', index=False)
df.to_json('out.json')

pd.read_csv('out.csv')
pd.read_excel('out.xlsx')
pd.read_json('out.json')

df.copy(deep=True)

df['target'] = [1, 0, 1, 1]
X = df.drop('target', axis=1)
y = df['target']

