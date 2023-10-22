import xlwt
import xlsxwriter

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Sheet1')
worksheet.write(0,0, 'Hello, world!_xlwt')
workbook.save('output1.xls')

workbook = xlsxwriter.Workbook('output1.xlsx')
worksheet = workbook.add_worksheet('Sheet1')
worksheet.write('A1', 'Hello, world!_xlsxwriter')
workbook.close()

