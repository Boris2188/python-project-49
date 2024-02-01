import random

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    operand = ['+', '-', '*']
    oper = random.choice(operand)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return calculator(oper, num1, num2)


def calculator(oper, num1, num2):
    operator = f'{num1} {oper} {num2}'
    result = 0
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    return operator, str(result)
