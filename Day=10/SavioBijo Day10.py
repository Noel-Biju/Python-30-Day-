'''Author :Savio Bijo Thomas
   date   :20-11-24
   purpose:To find the number of vowels'''

str=input("enter a  string:")
vowels="aeiouAEIOU"
no_of_vowels=0
for vowel in str:
    if vowel in vowels:
        no_of_vowels+=1
print("number of vowels in",str,":",no_of_vowels)
