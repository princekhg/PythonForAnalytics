"""Instead of printing the elements one by one,
make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that
      are smaller than that number given by the user."""

lst = []
lst_new = []
n = int(input("Enter the length of the list- "))
print("Enter values")
for i in range(n):
    val = int(input(" "))
    lst.append(val)
ele = int(input("Enter the max limit range value for new list- "))
for i in lst:
    if i < ele:
        lst_new.append(i)

print(lst_new)

