import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round() -> tuple:
    start_number = random.randint(1, 100)
    step = random.randint(2, 9)

    progression_length = 10
    progression_end = start_number + (step * progression_length)
    progression = list(range(
        start_number,
        progression_end,
        step)
    )

    answer = progression[step]
    progression[step] = '..'
    question = " ".join(map(str, progression))

    return question, str(answer)
