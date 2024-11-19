str=input("Enter a string:")
list_1=str.split()
list_2=[]
for i in list_1:
    list_2.append(len(i))
s=sum(list_2)
l=len(list_2)
avg=s/l
print(f"The average is:{avg}")