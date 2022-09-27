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
final_list = [a for a in lst_1 if a in lst_2]

print("The two lists with random values and the overlapping list ")
print(lst_1)
print(lst_2)
print("The final list with same value")
print(final_list)
