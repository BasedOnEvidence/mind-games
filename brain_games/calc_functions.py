import datetime
import random


def num_generator(start_num=0, end_num=100):
    random.seed(datetime.datetime.now())
    result = random.randint(start_num, end_num)
    return result


def operation_generator(operations_list):
    random.seed(datetime.datetime.now())
    operation = operations_list[random.randint(0, len(operations_list)-1)]
    return operation


def find_gcd(arg1, arg2):
    while arg1 != 0 and arg2 != 0:
        if arg1 > arg2:
            arg1 = arg1 % arg2
        else:
            arg2 = arg2 % arg1
    return arg1 + arg2


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
