""" 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

# 1-й вариант по заданию
n = int(input('Введите целое положительное число: '))
the_biggest_figure = 0
while n != 0:
    figure = n % 10
    n //= 10
    if figure > the_biggest_figure:
        the_biggest_figure = figure
print(f'Самая большая цифра: {the_biggest_figure}')

# 2-й вариант через список
n = input()
print(max(list(n)))

# какой быстрее?
