'''
Author: Rishita
Date: 29-11-2024
Python program to remove duplicates from a list while preserving the original order of elements.
version 1.0
'''
list3=input('Enter a list:')
list1=list(list3)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("The list after removing the duplicate elements is: ",list2)