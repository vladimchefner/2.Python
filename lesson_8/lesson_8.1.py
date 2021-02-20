"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить
работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def date_extraction(cls, data):
        return [int(i) for i in data.split('-')]

    @staticmethod
    def valid(*args):
        if 1 <= args[0] <= 31:
            if 1 <= args[1] <= 12:
                if 0 <= args[2] <= 2021:
                    return ' '.join(map(str, args))
                else:
                    raise ValueError('Invalid year')
            else:
                raise ValueError('Invalid month')
        else:
            raise ValueError('Invalid day')


try:
    print(Data.valid(*Data.date_extraction('27-01-2021')))
    print(Data.valid(*Data.date_extraction('27-13-2022')))
except Exception as err:
    print(err)
