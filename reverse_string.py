str = input("Enter a long string to reverse it")
lst = str.split(" ")
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=" ")
