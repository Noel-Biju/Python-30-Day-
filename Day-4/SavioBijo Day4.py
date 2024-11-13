'''Author :Savio Bijo Thomas
   date   :12-11-24
   purpose:Check whether a given number is prime or not'''

num=int(input("enter a number:"))
for i in range(2,num):
    if num%i==0 :
        print(num,"is not a prime number.")
        break
else:
    print(num,"is a prime number.")