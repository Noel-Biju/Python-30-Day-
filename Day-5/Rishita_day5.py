'''
Rishita
Date:13/11/24
Python program to get the multiplication table upto 10 of a user input number.
version 1.1
'''
number=int(input("Enter a number:"))
for i in range (1,11):
    table=number*i
    print(number,"*", i,"\t=",table)