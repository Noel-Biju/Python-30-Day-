n=int(input("Enter a number:"))
number=str(n)
if number==number[::-1]:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
