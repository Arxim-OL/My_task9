# Задача
# более глубоко понять особенности работы с функциями генераторами и оператором yield в Python

from itertools import combinations

def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in combinations(text, i):
            yield ''.join(j)

a = all_variants("abc")
for i in a:
    print(i)


