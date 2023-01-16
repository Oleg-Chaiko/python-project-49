import prompt
from brain_games.games.even import even_game
from brain_games.games.calc import calc_game
from brain_games.games.gcd import gcd_game
from brain_games.games.progression import progression_game
from brain_games.games.prime import prime_game


def welcome_user():
    global name
    name = prompt.string('May I have yore name? ')
    print(f'Hello, {name}!')
    return name


def brain(game):
    counter = 0
    while counter < 3:
        question, corect_ansver = game()
        print(f'Question: {question}')
        ansver = prompt.string('Yoyr answer: ')
        if ansver == corect_ansver:
            print('Correct!')
            counter += 1
        else:
            print(f"'{ansver}' is wrong abswer ;(. \
Correct answer was '{corect_ansver}'")
            print(f"Let's try again, {name}")
            break
    else:
        print(f'Congratulations, {name}!')


def even():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain(even_game)


def calc():
    welcome_user()
    print('What is the result of the expression?')
    brain(calc_game)


def gcd():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    brain(gcd_game)


def progression():
    welcome_user()
    print('What number is missing in the progression?')
    brain(progression_game)


def prime():
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    brain(prime_game)
