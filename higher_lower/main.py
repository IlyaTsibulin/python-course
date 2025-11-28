import random


def higher_lower(play):
    score = 0
    numbers = []
    for i in range(100):
        numbers.append(random.randint(1, 1000))
    if play == "y":
        user_guess = True
        while user_guess == True:
            first_number = numbers[random.randint(0, len(numbers))]
            second_number = numbers[random.randint(0, len(numbers))]
            assumption = input(
                f"What is higher? {first_number} or {second_number}\n Type 1 or 2.\n")
            if int(assumption) == 1 and first_number > second_number:
                score += 1
                print(f"You got it right! Score is {score}")
            elif int(assumption) == 2 and first_number < second_number:
                score += 1
                print(f"You got it right! Score is {score}")
            else:
                return print(f"You lost! Your score was {score}")


gaming = input("Do you want to play? Type \"y\" if yes\n")

while gaming == "y":
    higher_lower(gaming)
    gaming = input("Do you want to continue? Type \"y\" if yes\n")
