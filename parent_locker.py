import xlsxwriter

workbook = xlsxwriter.Workbook('parent_locker.xlsx')
worksheet = workbook.add_worksheet()

row = 0
while True:
    col = 0
    sections = ['Student Last Name', 'Student First Name', 'Grade', 'Gender', 'Date of Birth', 'Parent 1 First Name',
                'Parent 1 Last Name', 'Parent 1 Cell #', 'Parent 1 Email', 'Parent 2 First Name',
                'Parent 2 Last Name', 'Parent 2 Cell #', 'Parent 2 Email', 'Address (Street)', 'City', 'State', 'Zip Code',
                'Home Phone #']
    for item in sections:
        if col in [3, 6, 7, 12, 13]:
            worksheet.write(row, col, '')
            col += 1
        if col in [3, 6, 7, 12, 13]:
            worksheet.write(row, col, '')
            col += 1
        worksheet.write(row, col, input(item + ' : '))
        col += 1
    if input('Continue (y,n)') == 'n':
        break
    row += 1

workbook.close()