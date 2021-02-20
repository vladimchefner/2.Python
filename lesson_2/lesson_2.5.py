""" 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них."""

# максимально топорный вариант, однако быстрый, т.к. вся операция выполняется за один проход, 
# но используется дополнительная память. Применение метода extend:
lst = [7, 5, 3, 3, 2]
lst_new = []
n = int(input())
i = 0
while i < len(lst) and len(lst_new) < len(lst):
    if n > lst[0]:
        lst_new.append(n)
        lst_new.extend(lst)
    elif n <= lst[len(lst) - 1]:
        lst_new.extend(lst)
        lst_new.append(n)
    elif n <= lst[i]:
        lst_new.append(lst[i])
        i += 1
    elif lst[i - 1] >= n > lst[i]:
        lst_new.append(n)
        i += 1
    elif n > lst[i - 1]:
        lst_new.append(lst[i - 1])
        i += 1
if len(lst) == len(lst_new):
    lst_new.append(lst[-1])
print(*lst_new)

# второй вариант через insert, однако, на сколько я знаю insert сложная и медленная операция, может быть даже
# самая медленная
lst = [7, 5, 3, 3, 2]
n = int(input())
i = len(lst)
while i != 0 and n > lst[i - 1]:
    i -= 1
lst.insert(i, n)
print(*lst)

# я считаю, что вот этот самый быстрый и правильный вариант. добавить в конец и передвинуть в нужное место
lst = [7, 5, 3, 3, 2]
n = int(input())
lst.append(n)
i = len(lst) - 1
while i != 0 and n > lst[i - 1]:
    lst[i], lst[i - 1] = lst[i - 1], lst[i]
    i -= 1
print(*lst)
