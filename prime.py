def prime(val):
    for i in range(2, val // 2 + 1):
        if val % i == 0:
            return False
    return True


num = int(input("Enter number to check for prime"))
if prime(num):
    print(num, "is Prime")
else:
    print(num, "Is not Prime")
