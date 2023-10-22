import pandas as pd
# 读取 Excel 文件
df = pd.read_excel('pandas.xlsx')
# 创建数据透视表
pivot_table = pd.pivot_table(df, 
                             values='Sales', 
                             index='Region',
                             columns='Year', 
                             aggfunc='sum')

print(pivot_table)

