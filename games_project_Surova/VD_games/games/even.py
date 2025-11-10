import random

def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return str(number), correct_answer

def run():
    from VD_games.engine import play_game
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    play_game(description, generate_question)
