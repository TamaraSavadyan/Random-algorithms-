haieren_to_ruseren = {
    'Ա': 'А',
    'Բ': 'Б',
    'Ց': 'Ц',
    'Ք': 'К"',
    'Ո': 'Во',
    'Ե': 'Е',
    'Ռ': 'Р"',
    'Տ': 'Т',
    'Ը': '@',
    'Ի': 'И',
    'Օ': 'Օ',
    'Պ': 'П',
    'Ս': 'С',
    'Դ': 'Д',
    'Ֆ': 'Ф',
    'Գ': 'Г',
    'Հ': 'h',
    'Յ': 'й',
    'Կ': 'К',
    'Լ': 'Л',
    'Ժ': 'Ж',
    'Ճ': 'Тч',
    'Չ': 'Ч',
    'Ր': 'Р',
    'և': 'ев',
    'ՈՒ': 'У',
    'Ւ': 'И',
    'Ջ': 'Дж',
    'Ձ': 'Дз',
    'Փ': 'П"',
    'Թ': 'Т"',
    'է': 'э',
    'Զ': 'З',
    'Ղ': 'Х"',
    'Վ': 'В',
    'Ն': 'Н',
    'Մ': 'М',
    'Խ': 'Х',
    'Ծ': 'Ц"',
    'Շ': 'Ш',
    'ա': 'а',  
    'բ': 'б', 
    'ց': 'ц',  
    'ք': 'к"',
    'ո': 'о',  
    'ե': 'е',  
    'ռ': 'р"',  
    'տ': 'т',
    'ը': '@',  
    'ի': 'и',  
    'օ': 'о',
    'պ': 'п',  
    'ս': 'с',  
    'դ': 'д',  
    'ֆ': 'ф',
    'գ': 'г',  
    'հ': 'հ',  
    'յ': 'й',  
    'կ': 'к',
    'լ': 'л', 
    'ժ': 'ж',  
    'ճ': 'тч',  
    'չ': 'ч',
    'ր': 'р', 
    'և': 'ев', 
    'ու': 'у',   
    'ջ': 'дж',
    'ձ': 'дз',  
    'փ': 'п"',  
    'թ': 'т"', 
    'զ': 'з',  
    'ղ': 'х"',  
    'վ': 'в',  
    'ն': 'н',
    'մ': 'м',
    'խ': 'х', 
    'ծ': 'ц"',   
    'շ': 'ш',
    ' ': ' ',
    ',': ',',
    '.': '.',
}

from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfile
import os


def swap_letters():
    path = askopenfile(title='Select file')

    file_path = path.name
    folder_path = os.path.dirname(file_path)
    output_file_path = os.path.join(folder_path, 'output.txt')


    with open(file_path, 'r', encoding='utf-8') as file:
        with open(output_file_path, 'w', encoding='utf-8') as new_file:
            for line in file:
                swapped_line = ''
                for char in line:
                    swapped_char = haieren_to_ruseren.get(char, char)
                    swapped_line += swapped_char
                new_file.write(swapped_line)


if __name__ == '__main__':
    swap_letters()
