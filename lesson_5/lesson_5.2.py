"""
2. Создать текстовый файл (не программно), сохранить в нем несколько
строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('input.txt', 'r', encoding='utf-8') as file:
    cnt = 0
    for line in file:
        cnt += 1
        print(f'{cnt}st line: {len(line.split())} words')
    print(f'Total lines: {cnt}')
