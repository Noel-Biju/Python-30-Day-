string=input("enter the string:")
vowel=0
for i in string:
    if i in "aeiouAEIOU":
        vowel=vowel+1
print("no of vowels in",string,"is :",vowel)