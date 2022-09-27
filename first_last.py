import random
# list comprehension involved


def first_last(lst):
    a = lst[::len(lst) - 1]
    return a


lst = []
for i in range(10):
    lst.append(random.randint(10, 50))

print("The randomised list is  -- ", lst)
print(first_last(lst))
