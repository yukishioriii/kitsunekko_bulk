import re
import os
THRESHOLD = 3


def ass_handler(lines):
    lines = [ass_line_handler(line) for line in lines]
    return [line for line in lines if len(line) > THRESHOLD]


def get_event_line(lines):
    try:
        i = lines.index("[Events]")
    except ValueError:
        i = 0
    return i


def ass_line_handler(line):
    if 'Dialogue' not in line:
        return ""
    if "-->" in line or len(line) < 4:
        return ""
    line = re.sub("\{.+?\}", "", line)
    line = re.sub("Dialogue(.*?,){9}", "", line)
    line = re.sub(r"\\N", "", line)
    line = re.sub(r"m -?\d.*", "", line)
    return line


def srt_line_handler(line):
    if "-->" in line or len(line) < 4:
        return ""
    return line


def srt_handler(lines):
    lines = [srt_line_handler(line) for line in lines]
    return [line for line in lines if line]


# FOLDER_PATH = ''
# for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
#     for name in files:
#         file_name = os.path.join(root, name)
#         if file_name.endswith('.ass'):
#             line = ass_handler()

line_for_writting = []


def handle_file(input_path):
    file_name = input_path
    file_name_split = file_name.split('.')
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        index = get_event_line(lines)
        if index:
            lines = ass_handler(lines[index:])
        else:
            lines = srt_handler(lines)
        if lines:
            line_for_writting.extend(lines)


FOLDER_PATH = './unarchived'
if __name__ == "__main__":
    for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
        for name in files:
            file_name = os.path.join(root, name)
            try:
                # print(file_name)
                handle_file(file_name)
            except Exception as f:
                print(f)
                print(file_name)
    nl = []
    with open('data.txt', 'w+') as f:
        for i, line in enumerate(line_for_writting):
            if i:
                if line != line_for_writting[i-1]:
                    nl.append(line)
            else:
                nl.append(line)
        f.write("\n".join(nl))
            # handle_file('test.srt', 'test2.txt', newline=False)
