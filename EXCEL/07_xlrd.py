import xlrd
workbook = xlrd.open_workbook('example.xls',formatting_info=True)

# 獲取所有工作表的名稱
sheet_names = workbook.sheet_names()
print(f"工作表名稱：{sheet_names}")

# 獲取第一个工作表
sheet = workbook.sheet_by_index(0)

# 獲取工作表的行數和欄數
num_rows = sheet.nrows
num_cols = sheet.ncols
print(f"行数：{num_rows}，欄数：{num_cols}")

# 获取合并单元格的数量
merged_cells = sheet.merged_cells
num_merged_cells = len(merged_cells)
print(merged_cells)
print(f"合併儲存格数量：{num_merged_cells}")

# 讀取單元格數據
cell_value = sheet.cell_value(0, 1)
print(f"第一行第二欄的儲存格值：{cell_value}")