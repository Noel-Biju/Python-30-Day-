'''
Author: Rishita
Date: 12-11-2024
Python program to check whether the given number is a prime number or not.
version 1.1
'''
num=int(input("Enter a number: "))
for i in range (2,num):
    if(num%i==0):
        print(f"{num} is not a prime number.")
        break
    else:
        print(f"{num} is a prime number.")