import os
import shutil
import sys
from ocr import convert_image_to_csv
import pdf2jpg


def log(s):
    # В будущем возможно добавим логи
    print(s)


ispdf = False
show_output = False

# Эта штука ответственная за удаление цели после обработки
delete_file = False

filepath = input()
original_filepath = filepath

if filepath[len(filepath) - 3:] == 'pdf':
    ispdf = True
    pdf2jpg.convert_pdf2jpg('..\\' + filepath, '..\\' + filepath[:len(filepath) - 4], dpi=300, pages="0")
    filepath = filepath[:len(filepath) - 4] + '\\' + filepath[:len(filepath) - 4] + '.pdf_dir\\0_' + filepath[:len(
        filepath) - 4] + '.pdf.jpg'

csv_output = convert_image_to_csv(filepath)

if show_output:
    print("\n---------------------------\n")
    print(csv_output)
    print("\n---------------------------\n")

f = open('done.csv', 'w')
f.write(csv_output)
f.close()

if delete_file:
    os.remove(original_filepath)
shutil.rmtree(f'{filepath[:len(filepath) - 4]}')
if ispdf:
    shutil.rmtree(f'{original_filepath[:len(original_filepath) - 4]}')
