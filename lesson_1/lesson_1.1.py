""" 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран."""

a = 4
a1 = 3.4
print(a, a1)

b = 'Hello world!'
print(b)

c = input('Как вас зовут? ')
print('Здравствуйте, ', c, '!', sep='')
print(f'Здравствуйте, {c}!')

d = int(input('Введите любимое целое число: '))
print(f'Ваше число: {d}')

e = float(input('Введите число с плавающей точкой: '))
print(f'Ваше число: {e}')
