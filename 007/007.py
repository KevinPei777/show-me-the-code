import sys
import os
import re


def get_files(path):
    all_files = os.listdir(path)
    index = all_files.index('code_repositories')
    code_path = path + '/' + all_files[index]
    code_files = os.listdir(code_path)

    return code_files, code_path


def lines_count(line_list):
    code = 0
    space = 0
    note = 0
    multiline_count_sign = 0

    # for count multiline_count
    loop_count = 0
    start_index = 0

    for line in line_list:
        # Single-Line Comments
        pattern = re.compile(r'(\s*)#')

        # multiline comment
        pattern1 = re.compile(r'(\s*)"""')
        multiline_count = 0
        loop_count += 1

        if line == '\n':
            space += 1
        elif pattern.match(line):
            note += 1
        elif pattern1.match(line):
            multiline_count_sign += 1
            multiline_count += 1
            if multiline_count_sign == 1:
                start_index = loop_count
            if multiline_count_sign == 2:
                multiline_count += loop_count - start_index
                multiline_count_sign = 0
                note += multiline_count
                code += (2-multiline_count)
        else:
            code += 1

    return space, note, code


root_path = sys.path[0]
files, code_path = get_files(root_path)

code_line = 0
space_line = 0
note_line = 0

file_count = 0
for file in files:
    with open(code_path + '/' + file, 'r') as code_file:
        file_count += 1
        lines = code_file.readlines()
        result = lines_count(lines)
        code_line += result[2]
        space_line += result[0]
        note_line += result[1]


"""
    according to PEP8 standard, a blank line should be added at 
    the end of file 
"""
space_line += file_count

print('the num of code_lien is: {}'.format(code_line))
print('the num of space_lien is: {}'.format(space_line))
print('the num of note_lien is: {}'.format(note_line))
