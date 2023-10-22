import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('opendata111b141.csv')

# 新增一列資料
new_data = {'statistic_yyy':'151',
           'according':'按發生日期分',
           'district_code':'65000010',
           'site_id':'白色巨塔',
           'sex':'女',
           'father_age':'25～29歲',
           'mother_age':'25～29歲',
           'birth_count':'100' }
# 將新的資料轉換為 DataFrame
new_row = pd.DataFrame(new_data, index=[0])
# 使用 concat() 函數將新的資料添加到現有的 DataFrame 中
df = pd.concat([df, new_row], ignore_index=True)
print(df[df['site_id'] == '白色巨塔'])

# 修改資料
df.loc[df['site_id'] == '白色巨塔', 'birth_count'] = 90
print(df[df['site_id'] == '白色巨塔'])

df.to_csv('opendata111b141.csv', index=False)
