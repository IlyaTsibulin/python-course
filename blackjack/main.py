import random
deck = [6, 7, 8, 9, 10, 11]

user_choice = input("Do you want to play Black Jack? Type y or n.\n")


def random_card():
    random_card = random.choice(deck)
    return random_card


if user_choice == "y":
    play = True
    while play:
        bot_hand = [random_card(), random_card()]
        user_hand = []
        user_hand.append(random_card())
        print(f"Bot\'s hand is {bot_hand[0]}")
        while sum(user_hand) < 21:
            additional_card = input(
                f"Your hand is {user_hand}. Want to take another card? Type y or n.\n")
            if additional_card == "y":
                user_hand.append(random_card())
                print(f"Your current cards are {user_hand}")
            else:
                if sum(user_hand) > sum(bot_hand) or sum(bot_hand) > 21:
                    print(
                        f"Bot had {sum(bot_hand)} and you had {sum(user_hand)}, so you won")
                else:
                    print(
                        f"Bot had {sum(bot_hand)} and you had {sum(user_hand)}, so you've lost")
                break
        break
