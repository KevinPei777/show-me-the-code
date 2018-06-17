import re


def html_lines(readlines):
    content_list = []
    for line in readlines:
        pattern = re.compile(r'(<p.*?>)(.*)(</p>+)')
        pattern1 = re.compile('\<.*?\>')

        # matching all <p></p>
        if pattern.match(line):
            text = pattern1.sub('', line)
            text = text.replace('\n', '')
            if text:
                content_list.append(text)
    return content_list


with open('KevinPei777_show-me-the-code.html', 'r', encoding='utf-8') as html:
    content = html.readlines()
    results = html_lines(content)
    print(results)
