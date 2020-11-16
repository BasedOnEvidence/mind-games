import datetime
import random


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def odd_num_generator(start_num=0, end_num=100):
    result = num_generator(start_num, end_num)
    if result % 2 == 0:
        result = result + 1
    return result


def operation_generator(operations_list):
    random.seed(datetime.datetime.now())
    operation = operations_list[random.randint(0, len(operations_list) - 1)]
    return operation


def find_gcd(arg1, arg2):
    while arg1 != 0 and arg2 != 0:
        if arg1 > arg2:
            arg1 = arg1 % arg2
        else:
            arg2 = arg2 % arg1
    return arg1 + arg2


def is_prime(num):
    divider = 2
    while num % divider != 0:
        divider = divider + 1
    return divider == num


def calculate(arg1, arg2, operation):
    result = 0
    if operation == '+':
        result = arg1 + arg2
    if operation == '-':
        result = arg1 - arg2
    if operation == '*':
        result = arg1 * arg2
    return result


def main():
    pass


if __name__ == "__main__":
    main()
