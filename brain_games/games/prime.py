import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    num1 = random.randint(1, 100)
    return num1, prime(num1)


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            result_prime = False
            break
        else:
            result_prime = True

    return result_prime


def prime(num):
    ansver = is_prime(num)
    if num == 1:
        result = "no"
    elif ansver:
        result = "yes"
    else:
        result = "no"
    return result
