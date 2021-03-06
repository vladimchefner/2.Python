""" 6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый
цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count, cycle


def iter_count(s, f):
    for x in count(s):
        if x > f:
            break
        yield x


def iter_cycle(lst, num):
    for x in cycle(lst):
        if num == 0:
            break
        num -= 1
        yield x


for j in iter_count(3, 10):
    print(j)
for j in iter_cycle([3, 2, 1], 10):
    print(j)
