import pandas as pd

datas = pd.read_csv('data/raw/goodreads.csv')
# datas2 = pd.read_csv('data/raw/falf_datas.csv')

# row_datas = len(datas)
# print(f'number of lines {row_datas}')

# half_data = len( datas ) // 2
# new_data = datas.iloc[:half_data]
# new_data.to_csv('data/raw/falf_datas.csv', index=False)

data_head = datas.head()
data_info = datas.info()

print( data_head)
print( data_info)