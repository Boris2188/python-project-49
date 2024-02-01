import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    num = random.randint(1, 100)
    return even(num)


def is_even(num):
    return num % 2 == 0


def even(num):
    result = ""
    res = is_even(num)
    if res:
        result = "yes"
    else:
        result = "no"

    return num, result
