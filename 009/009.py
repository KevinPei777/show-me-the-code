import re


def html_lines(readlines):
    content_list = []

    for line in readlines:
        pattern = re.compile(r'.*https://.+|.*http://.+')
        if pattern.match(line):
            content_list.append(line)
    return content_list


with open('KevinPei777_show-me-the-code.html', 'r', encoding='utf-8') as html:
    content = html.readlines()
    result = html_lines(content)
    print(result)
