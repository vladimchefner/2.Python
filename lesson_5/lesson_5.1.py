"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open('output.txt', 'w', encoding='utf-8') as file:
    s = input()
    while s != '':
        print(s, file=file)
        s = input()
