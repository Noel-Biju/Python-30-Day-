"""author:Savio Bijo Thomas
   date:30-11-24
   purpose:to count how many times a specific element appears in a list"""

list=[1,1,2,3,4,5,6,7,7]
num=int(input("enter a number:"))
if num in list:
    count=list.count(num)
    print("The number of occurance of",num,"is",count)
