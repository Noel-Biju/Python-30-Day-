lis=[1,2,3,3,3,3,4,5,5,5,5,6,6,6,6,7,7,7,8,8]
userin=int(input("enter the no:"))
if userin in lis:
    print("no of occurance of",userin,"is:",lis.count(userin))
else:
    ("no not found")