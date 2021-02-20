"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from json import dump

with open('output.json', 'w', encoding='utf-8') as file_out:
    with open('input.txt', 'r', encoding='utf-8') as file_in:
        firms, avg_pr, cnt = dict(), dict(), 0
        for line in file_in:
            firm, type_f, proceeds, cost = line.split()
            profit = int(proceeds) - int(cost)
            firms.setdefault(firm, profit)
            if profit > 0:
                avg_pr['average_profit'] = avg_pr.get('average_profit', 0) + profit
                cnt += 1
        avg_pr['average_profit'] = avg_pr['average_profit'] // cnt
    dump([firms, avg_pr], file_out)
