'''Author :Savio Bijo Thomas
   date   :13-11-24
   purpose:To print multiplication table'''

num=int(input("enter a number:"))
for i in range(1,11):
    product=num*i
    print(num,"X",i,"\t=" ,product)