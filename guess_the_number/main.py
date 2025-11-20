import random


def game(play):
    correct_number = random.randint(1, 100)
    guesses = 0
    if play == "y":
        difficulty = input(
            "Do you want to play on \"easy\" or \"hard\" level?\n")
        if difficulty == "easy":
            guesses = 10
        elif difficulty == "hard":
            guesses = 5
        else:
            return print("See you next time!")
    else:
        return print("See you next time!\n")
    while guesses != 0:
        user_guess = int(input("Guess a number\n"))
        print(correct_number)
        if user_guess == correct_number:
            return print("You won!")
        elif user_guess > correct_number:
            print("You're too high")
            guesses -= 1
            print(f"You'r remaining guesses is {guesses}")
        elif user_guess < correct_number:
            print("You're too low")
            guesses -= 1
            print(f"You'r remaining guesses is {guesses}")
    print("You lost!")


gaming = input("Do you want to play? Type \"y\" if yes\n")

while gaming == "y":
    game(gaming)
    gaming = input("Do you want to continue? Type \"y\" if yes\n")
