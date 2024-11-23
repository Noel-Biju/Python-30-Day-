list=[1,2,3,2,1,1,5,6,3]
num=int(input("Enter a number: "))
if num in list:
    count=list.count(num)
print(f"The number of occrences of {num} is {count}")
