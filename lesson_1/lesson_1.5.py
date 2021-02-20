""" 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника."""

proceeds = int(input('Значение выручки: '))
cost = int(input('Значение издержки: '))
if proceeds > cost:
    print('Фирма работает в прибыль!')
    profit = proceeds - cost
    profitability = profit / proceeds * 100
    print(f'Прибыль: {profit}',
          f'Рентабельность: {"{:.2f}".format(profitability)} %', sep='\n')
    stuff = int(input('Количество сострудников: '))
    profit_per_employee = profit / stuff
    print(
        f'Прибыль в расчете на одного сотрудника: {"{:.2f}".format(profit_per_employee)}')
elif proceeds < cost:
    print('Фирма работает в убыток!')
    print(f'Убыток: {cost - proceeds}')
else:
    print('Фирма работает в 0!')