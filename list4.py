list1 = [10,20,30]
list2= ['a ', 'b', 'c', 'd']

# Methods to combine two lists
res = list1 + list2
print(res)

# Method 2: Using extend()
list1.extend(list2)
print(list1)  # list1 is changed after extend
print()
tmp_list = list(("India", "USA", "UK"))

for z in tmp_list:
    list1.append(z) 

print(list1)

tmp_list.clear()
print(tmp_list)
cp = list1.copy()
print(f"{cp} is a copy of list1")
count = list1.count('a')
print(count)

idx = list1.index('India')
print(idx)
elem = list1.pop()
print(f"{elem} is removed from the list")

list1.insert(9, 'UK')
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)