import pandas as pd
df = pd.read_excel('pandas3.xlsx')

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['day'] = df['Date'].dt.day

print(df['Year'])
print(df['day'])

