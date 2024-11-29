'''
Author: Rishita
Date: 29-11-2024
Python program that adds up the lengths of all the words in a string and prints the average(mean) length.
version 1.0
'''

string=input('Enter a string: ')
words=string.split()
list=[]
for i in words:
    list.append(len(i))
sum=sum(list)
total=len(list)
average=sum/total
print('The average is',average)