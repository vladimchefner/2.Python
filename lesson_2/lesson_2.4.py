""" 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово
с новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове."""

s = input().split()
i = 1
for word in s:
    print(i, word[:10])
    i += 1
