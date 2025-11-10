def play_game(description, generate_question):
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
