import random

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_question():
    number = random.randint(2, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return str(number), correct_answer

def run():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    from VD_games.engine import play_game
    play_game(description, generate_question)
