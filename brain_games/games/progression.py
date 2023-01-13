import random


def progression_game():
    step = random.randint(1, 20)
    num1 = random.randint(1, 30)
    num2 = num1 + step * random.randint(5, 9)
    progres = list(range(num1, num2, step))
    index_ = random.randint(0, len(progres) - 1)
    corect_ansver = str(progres[index_])
    progres[index_] = '..'
    example = (" ".join(map(str, progres)))
    return example, corect_ansver
