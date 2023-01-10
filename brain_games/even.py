import prompt
import random


def even_odd():
    name = prompt.string('May I have yore name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_answer = 0

    while number_answer < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        ansver = prompt.string('Yoyr answer: ')
        if random_number % 2 == 0:
            corect_ansver = 'yes'
        else:
            corect_ansver = 'no'
        if ansver == corect_ansver:
            print('Correct!')
            number_answer += 1
        else:
            print(f"'{ansver}' is wrong abswer ;(. \
Correct answer was '{corect_ansver}'")
            print(f"Let's try again, {name}")
            break
    else:
        print(f'Congatulations, {name}')
