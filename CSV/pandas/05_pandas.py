import pandas as pd

# 讀取 CSV 檔案

df = pd.read_csv('opendata111b141.csv')

# 計算每個城市區域嬰兒總出生數
count_by_citySite = df.groupby('birth_count').size()
print(count_by_citySite)
# 計算每個城市區域的平均嬰兒出生數
mean_birth_by_citySite = df.groupby('site_id')['birth_count'].mean()
print(mean_birth_by_citySite)
# 計算嬰兒出生數的統計摘要
birth_count = df['birth_count'].describe()
print(birth_count)

