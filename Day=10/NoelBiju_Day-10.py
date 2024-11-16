string=input("Enter a string:")
vowels="aeiouAEIOU"
no_of_vowels=0
for vowel in string:
    if vowel in vowels:
        no_of_vowels+=1
print("The number of vowels in the string is:",no_of_vowels)
