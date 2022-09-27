

user_name_1 = input("Enter your name")
user_name_2 = input("Enter your name")
print("Choose any one option from below choice \n 1.rock \n 2.paper \n 3.scissor")
choice = True


# function to perform user choice for game continuation
def choose():
    select = input("Do you want to start the game again - y to continue or n to cancel")
    if select.lower() == 'y':
        return True
    else:
        print("GAME ENDS")
        return False


while choice:
    user_choice_1 = input("Enter player1 your choice ")
    user_choice_2 = input("Enter player2 your choice ")
    if user_choice_1 == user_choice_2:
        print("it's a tie")
    elif user_choice_1 == '1' or user_choice_1.lower() == 'rock':
        if user_choice_2 == '3' or user_choice_2.lower() == 'scissor':
            print("Player 1 - ", user_name_1, " wins")
            choice = choose()
        else:
            print("Player 2 - ", user_name_2, " wins")
            choice = choose()
    elif user_choice_1 == '3' or user_choice_1.lower() == 'scissor':
        if user_choice_2 == '2' or user_choice_2.lower() == 'paper':
            print("Player 1 - ", user_name_1, " wins")
            choice = choose()
        else:
            print("Player 2 - ", user_name_2, " wins")
            choice = choose()
    elif user_choice_1 == '2' or user_choice_1.lower() == 'paper':
        if user_choice_2 == '1' or user_choice_2.lower() == 'rock':
            print("Player 1 - ", user_name_1, " wins")
            choice = choose()
        else:
            print("Player 2 - ", user_name_2, " wins")
            choice = choose()
    else:
        print("Wrong Choice !!!! \n Do you want to continue \n y - yes or n - no")
        choice = choose()
