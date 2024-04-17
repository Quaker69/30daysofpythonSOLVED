# Lets filter only even nubers
from functools import reduce
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))     # [2, 4]


