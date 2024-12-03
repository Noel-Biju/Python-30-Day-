list1=[1,2,3,1,2,4,5]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(f"The list after removing the duplicate elements is {list2}")
