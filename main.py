import pandas as pd

# task 1
df = pd.read_csv('Elite Sports Cars in Data.csv')

print(df.head(5))
print('---------------------------------------------')
print(df.info())
print('---------------------------------------------')
print(df.describe())

# task 2
df2 = pd.read_csv('dz.csv')
df2['City'].fillna('Санкт-Петербург', inplace=True)
df2['Salary'].fillna(100, inplace=True)

print('---------------------------------------------')
print(df2.sort_values(by='City'))

average_group_salary = df2.groupby('City')['Salary'].mean()
print(average_group_salary)