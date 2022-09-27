string = input("Enter string to check for palindrome")
if string == string[::-1]:
    print("String is Palindrome")
else:
    print("String is not palindrome")