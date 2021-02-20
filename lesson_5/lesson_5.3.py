"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

# вариант 1 со списками
with open('input.txt', 'r', encoding='utf-8') as file:
    names, salaries = [], []
    for line in file:
        name, salary = line.split(',')
        salaries.append(int(salary))
        if int(salary) < 20000:
            names.append(name)
    print(f'{", ".join(names)} have a salary of less than 20,000')
    print(f'Average income: {sum(salaries) // len(salaries)}')


# вариант 2 без списков
with open('input.txt', 'r', encoding='utf-8') as file:
    sum_salary, cnt = 0, 0
    for line in file:
        cnt += 1
        name, salary = line.split(',')
        sum_salary += int(salary)
        if int(salary) < 20000:
            print(name, end=' ')  # имена в одну строку
    # средняя з/п с новой строки
    print(f'\nAverage income: {int(sum_salary) // cnt}')
