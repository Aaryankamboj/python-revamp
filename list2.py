'''
num = int(input("Enter the number of elements"))

digits=list(())
for i in range(num):
    tmp = int(input(f"Enter {i+1} number "))
    digits.append(tmp)

print(digits)

avg = 0
sum = 0
for i in range(num):
    sum = sum+digits[i]

avg = sum//num
print(f"The average of list is {avg}")
'''


brands = ["nike", "rebook", "puma"]

dup_list = brands
tmp = brands[0] 
brands[0] = brands[2]
brands[2] = tmp

print(dup_list)

dup_list.insert(3, "Duke")
print(dup_list.index('Duke'))

tmp_list = list((1,2,3,4))
dup_list.extend(tmp_list)
print(dup_list)

marks = {
    "Aaryan" : 900,
    "Pratham" : 899,
    "Ritik" : 898,
    "Manik": 897
}


print(len(marks))
print(marks.keys())
print(marks.values())
print(type(marks.keys))

print(dup_list)
# removes specified value
dup_list.remove("Duke")
print(dup_list)

#remove value at specified index
dup_list.pop(1)
print(dup_list)

dup_list.pop() #by default removes last item
print(dup_list)

del dup_list[2] # del also removes the element 
print(dup_list)

#del tmp_list #del can delete an entire list too
print(tmp_list)
tmp_list.clear()
print(tmp_list)

for x in dup_list:
    print(x, end=" ")
print()
n=len(dup_list)
i=0
while(i<n):
    print(f"Item at index {i+1} is {dup_list[i]}")
    i = i+1

print()

[print(x, end=" ") for x in dup_list]

print()

fruits=["apple", "Banana", "orange", "kiwi"]
[print(x) for x in fruits if 'a' in x] #list comprehension

# or 
'''
for z in fruits:
    if 'a' in z:
        print(z)
'''

nums = [x for x in range(10) if x%2==0]
print(nums)

# We can manupulate an expression also
nums = [x+3 for x in range(10) if x%2==0]
print(nums)

[print(x) for x in nums if x%3==0]


fruits.sort()
print(fruits)

nums.sort(reverse=True)
print(nums)

def myfunc(n):
    return n-2

nums.sort(key=myfunc)
print(nums)

#by default, the sort is case sensitive

# to make the sort case insensitive
fruits.sort(key=str.lower)
print(fruits)

fruits.reverse()
print(fruits)


'''
So important list functions -
sort()
sort(reverse=True)
sort(key=custom_func)
sort(key=str.lower)
reverse()
'''