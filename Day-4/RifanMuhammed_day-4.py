'''
Author: Rifan Muhammed
Date: 12-11-2024
Day-4:Program to check whether the given number is prime number or not.
version 3.13.0
'''
num = int(input("Enter a number:"))
for i in range(2, num):
    if num % i == 0:
        print(f" {num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
