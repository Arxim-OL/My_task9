# Задание: Декораторы в Python

def is_prime(sum_three):
    def wrapper(a, b, c):
        sum_three(a, b, c)
        if sum_three(a, b, c) % 2:
            print('Простое')
        return sum_three (a, b, c)
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)