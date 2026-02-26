import pandas as pd

datas = pd.read_csv('data/raw/goodreads.csv')
# datas2 = pd.read_csv('data/raw/falf_datas.csv')

# row_datas = len(datas)
# print(f'number of lines {row_datas}')

# half_data = len( datas ) // 2
# new_data = datas.iloc[:half_data]
# new_data.to_csv('data/raw/falf_datas.csv', index=False)

# data_head = datas.head()
# data_info = datas.info()

# print( datas['Unnamed: 12'] )
# print( datas['Unnamed: 13'] )
# print( datas['Unnamed: 14'] )

# copying column that will be removed
# copy_column = datas[ [ 'Unnamed: 12','Unnamed: 13','Unnamed: 14' ] ].copy()
# copy_column.to_csv('data/raw/columns_remove.csv', index=False)

