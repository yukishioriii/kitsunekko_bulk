import os
import re


def is_jap(file):
    return len(re.findall('[一-龯ぁ-んァ-ンｧ-ﾝﾞﾟー]', open(file, 'r').read())) > 1000 # about 20% file


FOLDER_PATH = ''
for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
    for name in files:
        file_name = os.path.join(root, name)
        if is_jap(file_name):
            os.remove(file_name)
