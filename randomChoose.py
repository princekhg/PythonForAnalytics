import random
random_num = random.randint(1,9)
user_input = int(input("Predict a number 1 - 9 \n"))
if user_input == random_num:
    print("Absolutely Correct -- Great Work")
elif user_input < random_num:
    print("Wrong Choice -- \n You Guessed too Low, the number is  - ", random_num)
elif user_input > random_num:
    print("Wrong choice -- \n You Guessed too high, the number is - ", random_num)
