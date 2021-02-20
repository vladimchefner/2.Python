"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('output.txt', 'w', encoding='utf-8') as file_out:
    file_out.write(input())
with open('output.txt', 'r', encoding='utf-8') as file_in:
    print(sum([int(num) for num in file_in.readline().split()]))
