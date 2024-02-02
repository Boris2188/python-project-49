import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    lst = []
    step = random.randint(1, 10)
    number1 = random.randint(0, 100)
    return progression(number1, step, lst)


def progression(number1, step, lst):
    while len(lst) < 10:
        lst.append(str(number1))
        number1 += step
    index = random.randint(0, 100)
    result: object = lst[index]
    b = '..'
    lst[index] = b
    a = ''
    for i in range(len(lst)):
        a = ' '.join(lst)
        return a, result
