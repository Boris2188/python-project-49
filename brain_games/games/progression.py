import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    list = []
    step = random.randint(1, 10)
    num1 = random.randint(0, 100)
    return progression(num1, step, list)


def progression(num1, step, list):
    while len(list) < 10:
        list.append(str(num1))
        num1 += step
    index = random.randint(0, 9)
    result = list[index]
    b = ".."
    list[index] = b
    a = ''
    for i in range(len(list)):
        a = ' '.join(list)
    return a, result
