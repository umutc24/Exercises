# Ask the user for a string and print out whether this string is a palindrome or not.

x = input("Please insert a string: ")
x.split()
if x[0:] == x[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")