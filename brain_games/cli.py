import prompt


def welcome_user():
    name = prompt.string('May I have yore name?')
    print(f'Hello, {name}!')
    return name
