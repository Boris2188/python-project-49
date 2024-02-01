import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return f'{num1} {num2}', gcd(num1, num2)


def gcd(a, b):
    result = 0
    if b == 0:
        result = a
    else:
        result = gcd(b, a % b)

    return result
