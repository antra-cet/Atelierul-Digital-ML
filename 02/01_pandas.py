import pandas as pd
import numpy as np
import datetime

# 1. Series from list
# list = [10, 20, 30 ,40, 50]
# s = pd.Series(list)
# print(s)

# 2. Series from numpy array
# arr = np.array([10, 20, 30, 40, 50])
# s = pd.Series(arr)
# print(s)

# 3. Series from dictionary
# dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# s = pd.Series(dict)
# print(s)

# 4. Series from list with index
# data = [10, 20, 30, 40, 50]
# tokens = ['a', 'b', 'c', 'd', 'e']
# s = pd.Series(data, index=tokens)
# print(s)
# If the number of tokens is less than the number of data, then will receive error

# s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# print(s['b']) # 20
# print(s[['a', 'c', 'e']]) # 10, 30, 50
# print(s['b':'d']) # 20, 30, 40 , different from slicing in python, in pandas, the last index is included
# print(s[1:4]) # 20, 30, 40 , elements are selected by position, with the last index
# print(s[s > 20]) # 30, 40, 50

# 5. Series using dates
# dates_and_time = [datetime.datetime(2022, 1, 1),
#            datetime.datetime(2022, 1, 2),
# 		   datetime.datetime(2022, 1, 3)]
# s = pd.Series([10, 20, 30], index=dates_and_time)
# print(s['2022-01-02']) # 20
# print(s['2022-01-01':'2022-01-02']) # 10, 20


