lis=[1,2,3,4,5,6,7,8,9]
largest=0
secondlargest=0
for i in lis:
    if i>largest:
        largest=i
a=lis.remove(largest)
for i in lis:
    if i>secondlargest:
        secondlargest=i
print("the largest numberis:",largest)
print("the second largest number is:",secondlargest)



