import os
import re


def is_jap(file):
    # about 20% file
    return len(re.findall('[一-龯ぁ-んァ-ンｧ-ﾝﾞﾟー]', open(file, 'r', encoding='utf-8', errors='ignore').read())) > 2500


FOLDER_PATH = './unarchived'
count = 0
for root, dirs, files in os.walk(FOLDER_PATH, topdown=False):
    for name in files:
        file_name = os.path.join(root, name)
        try:
            if is_jap(file_name):
                os.remove(file_name)
                count = + 1
                print(f'removed {file_name}')
        except Exception as f:
            print(f)
            print(file_name)
print(f'removed {count} files')
