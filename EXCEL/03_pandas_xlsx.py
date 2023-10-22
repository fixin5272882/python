import pandas as pd

# 读取两个 Excel 文件
df1 = pd.read_excel('pandas1.xlsx')
df2 = pd.read_excel('pandas2.xlsx')

# 合并两个数据框
merged_df = pd.merge(df1, df2, on='ID', how='inner')

print(merged_df)

