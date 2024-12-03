'''
Author: Rishita
Date: 03-12-2024
Python program to find the largest and second largest element in a given list.
version 1.0
'''
list=[1,2,3,4,5,6,7]
largest=0
second_largest=0
for i in list:
    if i>0:
        largest=i
print('The largest element in the list is',largest)
for i in list:
    if i==largest:
        list.remove(i)
for i in list:
    if i>second_largest:
        second_largest=i
print('The second largest number in the list is',second_largest)