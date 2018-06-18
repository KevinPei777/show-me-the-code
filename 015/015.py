import xlwt
import json


def read_text(text_name):
    with open(text_name) as txt:
        text = txt.read()
        json_text = json.loads(text)
        return json_text


def write_excel(content_dict, excel_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('city', cell_overwrite_ok=True)

    row = 0
    col = 0
    for k, v in content_dict.items():
        ws.write(row, col, k)
        col += 1
        ws.write(row, col, v)
        col = 0
        row += 1
    wb.save(excel_name)


result_dict = read_text('city.txt')
write_excel(result_dict, 'city.xls')
