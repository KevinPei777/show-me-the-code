from xml.etree import ElementTree as ET
import json
import xlrd


def read_execl(excel_name):
    excel = xlrd.open_workbook(excel_name)
    excel_sheet = excel.sheet_by_name('student')
    data = {}
    for i in range(excel_sheet.nrows):
        data[(excel_sheet.row_values(i))[0]] = excel_sheet.row_values(i)[1:]

    return json.dumps(data, ensure_ascii=False)


def write_xml(data, xml_name):
    root = ET.Element('root')
    students = ET.SubElement(root, 'students')
    students.text = data
    students.append(ET.Comment(u"""学生信息表"id": [名字,数学,语文,英文]"""))

    students_xml = ET.ElementTree(root)
    students_xml.write(xml_name, xml_declaration=True, encoding='utf-8')


content = read_execl('students.xls')
write_xml(content, 'students.xml')
