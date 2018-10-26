import pandas as pd
import csv
df = pd.read_csv('fm.csv')
#print(df.head())
df = df.applymap(lambda x: 1 if x == True else x)
df = df.applymap(lambda x: 0 if x == False else x)
#df[df.eq(df.max(1),0)&df.ne(0)].stack()
print(len(df.fmid.unique()))
#print(df.describe())
