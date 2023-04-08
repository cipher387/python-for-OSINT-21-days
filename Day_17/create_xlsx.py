import xlsxwriter


workbook = xlsxwriter.Workbook('employees.xlsx')
worksheet = workbook.add_worksheet()

employees = (
    ['Name', 'Age'],
    ['John Smith', 33],
    ['Eric Gold',   26],
    ['Simon Silver',  37],
    ['James Conor',    50],
)

row = 0

for name, age in (employees):
    worksheet.write(row, 0, name)
    worksheet.write(row, 1, age)
    row += 1


worksheet.write(row, 0, 'Average age')
worksheet.write(row, 1, '=average(B1:B'+str(row-1)+')')

workbook.close()
