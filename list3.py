list1 = list((10,20,30))
list2=list1.copy()
tmp = list((-1,-2,-3))
#list2.append(tmp)

#for x in tmp:
    #list2.append(x)


#[list2.append(x) for x in tmp]
#print(list2)

[list2.pop() for z in list2 if z<0]
print(list2)


dup_list = list()

[dup_list.append(x+2) for x in list2]
print(dup_list)


