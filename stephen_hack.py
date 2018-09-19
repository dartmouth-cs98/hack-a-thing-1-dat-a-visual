import pandas as pd
import matplotlib

df = pd.read_csv('./datasets/parks.csv', index_col=['Park Code'])

print(df.head(3))
print(df.iloc[2])
print(df.loc['BADL'])
print(df.loc[['BADL', 'ARCH', 'ACAD']])
print(df[:3])
print(df[3:6])
df.columns = [col.replace(' ', '_').lower() for col in df.columns]
print(df.columns)
print(df.state.head(3))
print(df.state == 'UT')

df.state.plot.bar()