import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('opendata111b141.csv')

# 刪除單個欄位
df = df.drop('according', axis=1)

# 刪除多個欄位
# df = df.drop(['according','district_code'], axis=1)

# 刪除符合條件的資料
df = df.drop(df[df['birth_count'] < 230].index)
print(df.tail())