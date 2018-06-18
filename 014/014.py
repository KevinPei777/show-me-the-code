import xlwt
import json


def read_text(text_name):
    with open(text_name) as txt:
        text = txt.read()
        json_text = json.loads(text)
        return json_text


def write_excel(content_dict, excel_name):
    work_book = xlwt.Workbook()
    work_shett = work_book.add_sheet('student', cell_overwrite_ok=True)

    row = 0
    col = 0

    for k, v in content_dict.items():
        work_shett.write(row, col, k)
        for i in v:
            col += 1
            work_shett.write(row, col, i)
        row += 1
        col = 0
    work_book.save(excel_name)


result_dict = read_text('students.txt')
print(result_dict)
write_excel(result_dict, 'students.xls')
