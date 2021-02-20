"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что
машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} started!'

    def stop(self):
        return f'{self.name} stopped!'

    def turn_left(self):
        return f'{self.name} turned left!'

    def turn_right(self):
        return f'{self.name} turned right!'

    def show_speed(self):
        return f'Current speed {self.speed}!'


class TownCar(Car):
    def show_speed(self):
        return 'Overspeed detected!' if self.speed > 60 else f'Current speed {self.speed}!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return 'Overspeed detected!' if self.speed > 40 else f'Current speed {self.speed}'


class PoliceCar(Car):
    pass


hyndai = TownCar(80, 'black', 'Hyndai', False)
print(hyndai.go(), hyndai.stop(), hyndai.turn_left(), hyndai.turn_right())
print(hyndai.show_speed())
bugatti = SportCar(120, 'blue', 'Bugatti', False)
print(bugatti.go(), bugatti.stop(), bugatti.turn_left(), bugatti.turn_right())
print(bugatti.show_speed())
audi = WorkCar(30, 'yellow', 'Audi', False)
print(audi.go(), audi.stop(), audi.turn_left(), audi.turn_right())
print(audi.show_speed())
bmw = PoliceCar(70, 'white', 'BMW', True)
print(bmw.go(), bmw.stop(), bmw.turn_left(), bmw.turn_right())
print(bmw.show_speed())
