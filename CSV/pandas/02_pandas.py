import pandas as pd
# 讀取 CSV 檔案
df = pd.read_csv('opendata111b141.csv')

# 選取單個欄位
site_id = df['site_id']

# 選取多個欄位
parent_age = df[['father_age', 'mother_age']]
# 條件篩選
birth_count = df[df['birth_count'] > 200]
print(birth_count)
