"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


class Warehouse:
    def __init__(self):
        # товары на складе
        self.gds_in_stock = dict()
        # отправка из склада
        self.gds_out_stock = dict()

    def get_goods(self, equip):
        # добавляем товары на склад
        self.gds_in_stock.setdefault(equip.name, dict())
        # прибавляем количество товаров к уже существующим
        self.gds_in_stock[equip.name][equip.goods()] = \
            self.gds_in_stock[equip.name].get(equip.goods(), 0) + equip.qty

    def send_goods(self, name, gds, num):
        if gds in self.gds_in_stock[name]:
            if num <= self.gds_in_stock[name][gds]:
                # добавляем товар к отправке
                self.gds_out_stock[gds] = self.gds_out_stock.get(gds, 0) + num
                # отнимаем из склада
                self.gds_in_stock[name][gds] = self.gds_in_stock[name].get(gds) - num
            else:
                raise ValueError(f'There are only {self.gds_in_stock[name][gds]} in stock!')
        else:
            raise ValueError(f'Product "{gds}" out of stock!')


class Equipment:
    def __init__(self, name: str, brand: str, model: str, color: str, price: float, qty: int):
        self.name = name
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.qty = qty

    def goods(self):
        # получаем краткую информацию: бренд модель цвет
        return f'{self.brand} {self.model} {self.color}'

    def __str__(self):
        return f'\n{self.name.capitalize()} {self.brand} {self.model} {self.color} {self.price}₽ - {self.qty} pieces'


class Printer(Equipment):
    def __init__(self, name, brand, model, color, price, qty, is_wifi_support, speed):
        super().__init__(name, brand, model, color, price, qty)
        self.is_wifi_support = is_wifi_support
        self.speed = speed


class Scaner(Equipment):
    def __init__(self, name, brand, model, color, price, qty, type_scaner):
        super().__init__(name, brand, model, color, price, qty)
        self.type_scaner = type_scaner


class Xerox(Equipment):
    def __init__(self, name, brand, model, color, price, qty, max_size_paper):
        super().__init__(name, brand, model, color, price, qty)
        self.max_size_paper = max_size_paper


stock = Warehouse()

printer_1 = Printer('printer', 'HP', 'LaserJet Pro M15w', 'white', 8690, 40, False, 10)
printer_2 = Printer('printer', 'Epson', 'L805', 'grey', 22890, 35, True, 25)
scaner_1 = Scaner('scaner', 'Fujitsu', 'S1300i', 'black', 14990, 20, 'tablet')
scaner_2 = Scaner('scaner', 'Plustek', '2610 Plus', 'white', 30990, 13, 'bilateral')
xerox_1 = Xerox('xerox', 'Xerox', 'B215VDNI', 'black', 13990, 26, 'A4')
xerox_2 = Xerox('xerox', 'Xerox', 'Versalink B405', 'grey', 18490, 19, 'A4')
# добавляем товары на склад
stock.get_goods(printer_1)
stock.get_goods(printer_2)
stock.get_goods(scaner_1)
stock.get_goods(scaner_2)
stock.get_goods(xerox_1)
stock.get_goods(xerox_2)
print(printer_1, printer_2, scaner_1, scaner_2, xerox_1, xerox_2, sep='\n')
print()
# содержимое склада
print(stock.gds_in_stock)
print()
# готовим к отправке товар и его количество
stock.send_goods('scaner', 'Fujitsu S1300i black', 9)
stock.send_goods('printer', 'Epson L805 grey', 14)
stock.send_goods('printer', 'Epson L805 grey', 6)
stock.send_goods('xerox', 'Xerox B215VDNI black', 20)
# смотрим содержимое
print(stock.gds_out_stock)
print()
# смотрим остаток на скдладе
print(stock.gds_in_stock)
print()
