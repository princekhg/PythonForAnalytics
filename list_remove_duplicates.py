lst_new = []
lst = []


def remove_duplicate(lst):
    for i in lst:
        if i not in lst_new:
            lst_new.append(i)
    return lst_new


def remove_duplicate_set(lst):
    return list(set(lst))


n = int(input("Enter the length of the list- "))
print("Enter values")
for i in range(n):
    val = int(input(" "))
    lst.append(val)

print(remove_duplicate(lst))
print(remove_duplicate_set(lst))
