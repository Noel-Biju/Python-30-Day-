list=[1,2,3,4,5,6,7]
largest=0
second_largest=0
for i in list:
    if i>largest:
        largest=i
print(f"The largest element in the list is {largest}")
for i in list:
    if i==largest:
        list.remove(i)
for i in list:
    if i>second_largest:
        second_largest=i
print(f"The second largest element in the list is {second_largest}")
