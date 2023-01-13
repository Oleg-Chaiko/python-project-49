import random


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return 'yes'
    else:
        return 'no'


def prime_game():
    random_number = random.randint(1, 100)
    corect_ansver = is_prime(random_number)
    return random_number, corect_ansver
