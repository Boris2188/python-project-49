import prompt

NUMBER_OF_ROUNDS = 3


def brain_logics(brain_logic):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(brain_logic.DESCRIPTION)
    count = 0
    for _ in range(NUMBER_OF_ROUNDS):
        question, result = brain_logic.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == str(result):
            print("Correct!")
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct "
                f"answer was '{result}'\nLet's try again, {name}!"
            )
            break
    if count == NUMBER_OF_ROUNDS:
        print(f"Congratulations, {name}!")
