'''
Author: Rishita
Date: 29-11-2024
Python program to count how many times a specific element appears in a list.
version 1.0
'''
list=[1,2,15,3,22,12,5,1,3,22,2,2,4,3]
num=int(input('Enter a number: '))
if num in list:
    count=list.count(num)
print('The number of times',num,'occurs in the list is',count,'.')