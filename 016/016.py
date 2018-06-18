import xlwt
import json


def read_text(text_name):
    with open(text_name) as txt:
        text = txt.read()
        json_text = json.loads(text)
        return json_text


def write_excel(content, excel_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('numbers', cell_overwrite_ok=True)

    for row in range(len(content)):
        for col in range(3):
            ws.write(row, col, content[row][col])
    wb.save(excel_name)


result = read_text('numbers.txt')
write_excel(result, 'numbers.xls')
