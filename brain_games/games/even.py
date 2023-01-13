import random


def even_game():
    random_number = random.randint(1, 100)
    if random_number % 2 == 0:
        corect_ansver = 'yes'
    else:
        corect_ansver = 'no'
    return random_number, corect_ansver
