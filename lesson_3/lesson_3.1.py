""" 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(x, y):
    if y != 0:
        return x / y
    raise Exception('Аргумент "y" не должен быть равен 0')


x, y = int(input()), int(input())
try:
    print(division(x, y))
except Exception as err:
    print(err)
