import re
import os
THRESHOLD = 3


def ass_handler(file_name):
    lines = [line.rstrip() for line in open(file_name, 'r').readlines()]
    lines = ass_strip_meta_data(lines)
    return [ass_line_handler(line) for line in lines if len(line) > 3]


def ass_strip_meta_data(lines):
    try:
        i = lines.index("[Events]")
    except IndexError:
        i = 0
    return lines[i+2:]


def ass_line_handler(line):
    if 'Dialogue' not in line:
        return ""
    line = re.subn("\{.+?\}", "", line)
    line = re.subn("Dialogue(.*?,){9}", "", line)
    line = re.subn("\\N", "", line)
    return line



FOLDER_PATH = ''
for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
    for name in files:
        file_name = os.path.join(root, name)
        if file_name.endswith('.ass'):
            line = ass_handler()

if __name__ == "__main__":
    # lines = [line.rstrip() for line in open('test.ass', 'r').readlines()]
    # lines = ass_handler(lines)
    # print(is_jap('jap.srt'))
    pass
