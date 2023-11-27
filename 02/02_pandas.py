import pandas as pd

# 6. DataFrame
# Dataframes are : bidimensional, indexed, heterogeneous (each column can have a different type)
# data = {'Name': ['Ana', 'Bogdan', 'Cristina'],
#         'Age': [25, 30, 22],
#         'Salary': [50000, 60000, 45000]}

# df = pd.DataFrame(data)

# 6.1. Accessing data
# print(df)
# print(df['Name'])
# print(df.at[1, 'Salary'])
# df['Experience'] = [2, 5, 1] # add a new column
# print(df)

# 6.2. Indexing and selecting data
# df.set_index('Name', inplace=True) # set the index to be the Name column
# print(df.loc['Bogdan']) # loc accesses data by label
# print(df.iloc[1]) # iloc accesses data by position
# print(df.loc[['Ana', 'Cristina'], ['Age', 'Salary']]) # select rows and columns by label

# 6.3. Filtering data
# filtered = df[(df['Age'] > 25)]
# filtered = df[(df['Age'] >= 22) & (df['Experience'] >= 2)]
# print(filtered)

# 6.4. Sorting data
# df.sort_values(by=['Age'], inplace=True, ascending=False)
# print(df)

# 6.5. Remove duplicates
# data = {'Name': ['Ana', 'Bogdan', 'Ana', 'Cristina', 'David', 'Ana'],
#         'Age': [25, 30, 25, 22, 35, 25],
# 		'Salary': [50000, 60000, 50000, 45000, 70000, 50000]}
# df = pd.DataFrame(data)
# print(df.drop_duplicates())

# 6.6. Missing values
# data = {'Name': ['Ana', 'Bogdan', None, 'Cristina', 'David'],
#         'Age': [25, 30, None, 22, 35],
# 		'Salary': [50000, None, 45000, 70000, 60000]}
# df = pd.DataFrame(data)
# print(df.dropna()) # drop rows with missing values
# print(df.fillna(0)) # replace missing values with 0

# 6.7. Collumn manipulation
# print(df.rename(columns={'Name': 'First Name'}, inplace=True)) # rename a column
# print(df)

# 6.8. Grouping data
# data = {'Name': ['Ana', 'Bogdan', 'Cristina', 'David', 'Elena', 'Florin'],
#         'Age': [25, 30, 22, 35, 28, 40],
#         'Salary': [50000, 60000, 45000, 70000, 55000, 80000],
#         'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR']}
# df = pd.DataFrame(data)
# dep = df.groupby(['Department'])
# for group in dep:
# 	print(group)

# avg = dep['Salary'].mean() # average salary for each department
# print(avg)

# agg = dep.agg({'Age': 'mean', 'Salary': ['sum', 'median'], 'Name': 'count'}) # aggregate functions
# print(agg)

# 6.9. Joining data
# data = {'Date': ['2022-01-01', '2022-02-01', '2022-03-01'],
#         'Sales': [100, 150, 200]}
# df = pd.DataFrame(data)
#
# df['Date'] = pd.to_datetime(df['Date']) # convert to datetime
# df['Day'] = df['Date'].dt.day # extract day
# df['Month'] = df['Date'].dt.month # extract month
# df['Year'] = df['Date'].dt.year # extract year
# print(df)

# Calculations between columns
# df['Difference-day'] = (df['Date'] - pd.to_datetime('2022-01-01')).dt.days # difference in days
# print(df)

# 6.10. Concatenate tables
# df1 = pd.DataFrame({'Name': ['Ana', 'Bogdan'],
#                     'Age': [25, 30],
#                     'ID': [1, 2]})
# df2 = pd.DataFrame({'Name': ['Cristina', 'David'],
#                     'Age': [22, 35],
#                     'ID': [2, 3]})
#
# df = pd.concat([df1, df2], ignore_index=True) # concat rows
# df = pd.concat([df1, df2], axis=1) # concat columns
# print(df)

# 6.11. Merge/Join tables
# print(pd.merge(df1, df2, on='ID', how='outer')) # merge tables; how: inner, outer, left, right
# print(df1.join(df2, how='inner', lsuffix='_left', rsuffix='_right')) # join tables

# 6.12. Export data
# df.to_csv('data.csv')
# df = pd.read_csv('data.csv')
# print(df)