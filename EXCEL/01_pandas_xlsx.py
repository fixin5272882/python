import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel('pandas.xlsx', sheet_name='工作表1')

# 計算平均值
average = df['Sales'].mean()
print(average)

# 寫入 Excel 檔案
df.to_excel('pandas_output.xlsx', sheet_name='Sheet1', index=False)

