'''Author :Savio Bijo Thomas
   date   :20-11-24
   purpose:To add lengths of all the words in a string and print the average length'''

str=input("Enter a string:")
list1=str.split()
list2=[]
for i in list1:
    list2.append(len(i))
sum=sum(list2)
length=len(list2)
avg=sum/length
print("The average is:",avg)