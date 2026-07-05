

list1 = [1, 2, 3, 4, 5,1,2]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print("List without duplicates:", list2)