import random
import math


def gcd_game():
    nod = random.randint(1, 20)
    num1 = nod * random.randint(10, 30)
    num2 = nod * random.randint(1, 20)
    example = (f'{num1} {num2}')
    corect_ansver = str(math.gcd(num1, num2))
    return example, corect_ansver
