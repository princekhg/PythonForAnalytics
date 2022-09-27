"""
Randomly generate two lists to test this
Write this in one line of Python
"""
import random

lst_1 = []
lst_2 = []
for i in range(10):
    lst_1.append(random.randint(10, 22))
    lst_2.append(random.randint(10, 22))


def ele_check(lst_1, lst_2):
    lst_3 = set()
    for i in lst_1:
        if i in lst_2:
            lst_3.add(i)
    return list(lst_3)


print("The two lists with random values and the overlapping list ")
print(lst_1)
print(lst_2)
print(ele_check(lst_1, lst_2))
