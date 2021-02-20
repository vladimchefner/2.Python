"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    __colors = {'red': 7, 'green': 5, 'yellow': 2}

    def __init__(self):
        self.__true_colors = ['red', 'yellow', 'green']
        self.__i = 0

    def running(self):
        for color, time in TrafficLight.__colors.items():
            if color == self.__true_colors[self.__i]:
                print(color)
                sleep(time)
                self.__i += 1
            else:
                raise ValueError(
                    f'Wrong color! Should be now {self.__true_colors[self.__i]}')


a = TrafficLight()
try:
    a.running()
except Exception as err:
    print(err)
