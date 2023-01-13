import random


def calc_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        example = (f'{num1} + {num2}')
        corect_ansver = str(num1 + num2)
    elif operator == '-':
        example = (f'{num1} - {num2}')
        corect_ansver = str(num1 - num2)
    else:
        example = (f'{num1} * {num2}')
        corect_ansver = str(num1 * num2)
    return example, corect_ansver
