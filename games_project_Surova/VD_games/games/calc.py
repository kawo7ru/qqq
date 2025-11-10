import random

def generate_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(['+', '-', '*'])

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:  # '*'
        result = a * b

    question = f"{a} {op} {b}"
    correct_answer = str(result)
    return question, correct_answer

def run():
    from VD_games.engine import play_game
    description = "What is the result of the expression?"
    play_game(description, generate_question)
