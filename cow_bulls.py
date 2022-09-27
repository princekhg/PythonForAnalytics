import random


def compare_numbers(number, user_guess):
    cowbull = [0, 0]  # cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


if __name__ == "__main__":
    playing = True  # gotta play the game
    number = str(random.randint(0, 9999))  # random 4 digit number
    guesses = 0

    print("This game is cows and bulls \n A 4 digit number is generated and you will \n require to suggest 1 digit of "
          "number at once, if you choose the right digit you receive 1 cow else 1 bull. Game ends when the correct "
          "number is suggested")

    while playing:
        user_guess = input("Guess a digit")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number, user_guess)
        guesses += 1

        print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1] == 4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was " + str(number))
            break  # redundant exit
        else:
            print("Your guess isn't quite right, try again.")
