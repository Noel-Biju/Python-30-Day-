List_1=[1,2,3,4]
List_2=[1,2,6,7]
common_list=[]
for i in List_1:
       if i in List_2:
            common_list.append(i)
print(f"The common elements include {common_list}")
