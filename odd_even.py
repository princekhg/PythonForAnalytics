""" This program will  check odd or even at the same time check for
a number is multiple og 4 or not, plus take two number as input and check if they're
divisible or not"""

num = int(input("Enter number to check for even or odd"))
num_check = int(input("Enter number to divide by check"))
if num % 2 == 0:
    print(num, "is even number ")
    if num % 4 == 0:
        print(num, "is even and multiple of 4")
else:
    print(num, " is odd Number")
if num % num_check == 0:
    print(num, "is divisible by:- ", num_check)
else:
    print(num, "is not divisible by:- ", num_check)
