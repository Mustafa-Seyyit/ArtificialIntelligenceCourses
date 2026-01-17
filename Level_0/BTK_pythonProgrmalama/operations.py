

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def recursive_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * recursive_factorial(n-1)

def recursive_reverse_list(input_list):
    if len(input_list) <= 1:
        return input_list
    return [input_list[-1]] + recursive_reverse_list(input_list[:-1])

def recursive_sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + recursive_sum_list(numbers[1:])