myset = {"name", "age" , "marks", "class"}
#print(myset)

# The index of elements in myset is not fixed and changes everytime

#for i in range(len(myset)):
    #print(f"Element at index {i} is {myset}")

#print(myset)
#myset.add('age')
#print(myset)

bools = {True, "False", 0, 1, "true"}
#set does not allow duplicate values
#print(bools)
#print(len(bools))


exam = set(('Maths', ))
#print(type(exam))

for x in bools:
    if type(x) == bool:
        bools.remove(x)
        x=str(x)
        bools.add(x)
#print(bools)

#for x in bools:
    #print(type(x), end = " ")




myset.update(bools)
#print()
#print(myset)


data = {
    1:'Aaryan',
    2:'Raman',
    3:'Virat',
    4:'MS Dhoni'
}

myset.update(data)
#print(myset)

# Remove and discard both are used to remove an element from set
myset.remove('name')
#print(myset)
myset.discard('False')
#print(myset)

myset.pop()
#print(myset)


int_set = set(())

'''
for i in myset:
    if type(i) == int:
        tmp = myset.pop()
        int_set.add(tmp)
print(int_set)
'''

myset.clear()
print(myset)
#del int_set
#print("Deleted successfully")

a={1,2,3,4,2,1}
b={2,3,1,6}
c = a.union(b)
print(c)
c = a.intersection(b)
print(c)

diff = a.difference(b)
print(diff)

sym_diff = a.symmetric_difference(b)
print(sym_diff)

d = {"aman", "Chaman", "raman"}
a=a|d
print(a)



a.update({"Hamza",})
print(a)
a.intersection_update(b)
f=a.intersection(b)
print(a, "This is 'a' set")
print(f, "This is a 'F' set")

f.add("Ajit")
print(f)
cp = f.copy()
print(cp)
