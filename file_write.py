file_name = input("Enter the output file name")
file = open(file_name, "w+")
file.writelines("This is added")
file.seek(0)
print(file.read())