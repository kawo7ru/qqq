import random

def generate_question():
    start = random.randint(1, 10)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)

    progression = []
    for i in range(length):
        value = start + i * step
        if i == hidden_index:
            progression.append("..")
            correct_answer = str(value)
        else:
            progression.append(str(value))

    question = " ".join(progression)
    return question, correct_answer

def run():
    description = "What number is missing in the progression?"
    from VD_games.engine import play_game
    play_game(description, generate_question)
