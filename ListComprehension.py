a = []
n = int(input("Enter total number of values in the list"))
for i in range(n):
    a.append(int(input(" ")))
lst_a = [n for n in a if n %2 == 0 ]

print(lst_a)

