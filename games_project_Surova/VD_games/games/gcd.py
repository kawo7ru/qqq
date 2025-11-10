import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    result = gcd(a, b)
    question = f"{a} {b}"
    correct_answer = str(result)
    return question, correct_answer

def run():
    from VD_games.engine import play_game
    description = "Find the greatest common divisor of given numbers."
    play_game(description, generate_question)
