""" 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""


def person(**kwargs):
    return ' '.join(p[i] for i in p)


p = {
    'name': 'Том',
    'surname': 'Харди',
    'birthday': '1982',
    'home_town': 'Лондон',
    'email': 'venom@gmail.com',
    'tel': '+44-20-2568-6984'
}
print(person(**p))
