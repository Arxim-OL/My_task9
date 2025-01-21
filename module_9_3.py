# Задача
# понять механизм создания генераторных сборок и использования встроенных функций-генераторов

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x[1]) - len(x[0])) for x in zip(first, second) if len(x[1]) != len(x[0]))
second_result = (len(first[i]) == len(second[i]) for i in range (len(first)))

print(list(first_result))
print(list(second_result))



