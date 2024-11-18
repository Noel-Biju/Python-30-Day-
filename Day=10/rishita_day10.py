'''
Author: Rishita
Date: 18-11-2024
Python program that counts the number of vowels (a, e, i, o, u) in a given string, regardless of case.
version 1.1
'''
string=input("Enter a string:")
vowels="aeiouAEIOU"
vowels_count=0
for char in string:
    if char in vowels:
        vowels_count+=1
print(f"The number of vowels in {string} = {vowels_count}")