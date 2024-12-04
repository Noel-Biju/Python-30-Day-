list=[1,2,3,2,1,4,5,7,6,5]
unique_list=[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(f"The List after removing duplicate elements is: {unique_list}")
