import random

s = """qwertyuiopasdfghjklzxcvbnm<{}!@#$%^&*ASZDQEWRFZGXCVBNMKLJHGTYUIOP1234567890"""
lst = []
lst_length = [a for a in range(25, 4, -1)]
print(lst_length)
for i in lst_length:
    lst.append("".join(random.sample(s, i)))
choice = int(input("Make a choice -- \n 1. for weak password \n 2. For medium password \n 3. For Strong Password \n "
                   "4. For Super Strong Password "))
lst_weak = [a for a in lst if 4 < len(a) <= 6]
lst_medium = [a for a in lst if 6 < len(a) <= 10]
lst_strong = [a for a in lst if 10 < len(a) <= 15]
lst_extra_strong = [a for a in lst if len(a) > 15]
if choice == 1:
    print("Your new password is - ",random.sample(lst_weak, 1))
elif choice == 2:
    print("Your new password is - ", random.sample(lst_medium, 1))
elif choice == 3:
    print("Your new password is - ", random.sample(lst_strong, 1))
elif choice == 4:
    print("Your new password is - ", random.sample(lst_extra_strong, 1))
else:
    print("Wrong choice! ----- ")



