import xlwt

# 创建一个新的 Excel 文件
workbook = xlwt.Workbook()

# 创建一个工作表
worksheet = workbook.add_sheet('Sheet1')

# 设置单元格的样式
style = xlwt.XFStyle()

# 创建字体对象
font = xlwt.Font()
font.bold = True
font.colour_index = xlwt.Style.colour_map['red']
style.font = font

# 设置边框
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
style.borders = borders

# 创建一个对齐对象
alignment = xlwt.Alignment()
# 设置水平对齐方式为居中对齐
alignment.horz = xlwt.Alignment.HORZ_CENTER
# 设置垂直对齐方式为居中对齐
alignment.vert = xlwt.Alignment.VERT_CENTER
# 将对齐对象应用于样式对象
style.alignment = alignment

# 写入数据到单元格
worksheet.write(0, 0, 'Hello', style)
worksheet.write(0, 1, 'WORF')

# 合并空白单元格、起始行索引、结束行索引、起始列索引、结束列索引
worksheet.write_merge(1,1, 0,2, 'Merged Cells', style)

# 保存 Excel 文件
workbook.save('example.xls')

