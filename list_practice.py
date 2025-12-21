'''
# Q1
nums = [1,2,3,5,6]
print(f"First element is {nums[0]} and last element is {nums[-1]}")

# Q2
nums.append(100)
nums.insert(1,"Hello")
nums.remove(3)

colors = list(("red", "green", "blue"))
colors[1] = "yellow"
print(len(colors))

emp_list = list(())
emp_list.append(10)
emp_list.append(20)
emp_list.append(30)

a = [10,20,30]
b = [40,50]
a.extend(b)


numss = [5, 4, 3, 2, 1]
tmp_numss = numss.reverse()
print(tmp_numss)
'''

# Level 2 - Practice questions
nums = [2,4,6,8,10]
for x in nums:
    print(x, end = " ") 

print()

marks = [10, 20, 30, 40]
add = 0
for i in range(len(marks)):
    add=add+marks[i]

print(f"Sum is {add}") 

nums = [5, 1, 5, 2, 5, 3]
count = nums.count(5)
print(count)

vals = [11, 2, 35, 14, 9]
vals.sort(reverse=True)
print(vals[0])

# max elemnt to find manually
max_value=0
for i in vals:
    if i > max_value:
        max_value =i

print(max_value)

names = ["john", "amy", "bob"]
names[0].upper()
names[1].upper()
names[2].upper()
print(names)

names = [n.upper() for n in names]
print(names)

sqaures=[]
for x in range(1,11):
    sq = pow(x,2)
    sqaures.append(sq)
print(sqaures)

sqaures=[pow(x,2) for x in range(1,11)]
print(sqaures)

mixed = [10, "a", 20, "b", 30, "c"]
ans = []
for x in range(len(mixed)):
    if(type(mixed[x]) == int):
        ans.append(mixed[x])
    else:
        pass

print(ans)

ans = [ans.append(mixed[x]) for x in range(len(mixed)) if isinstance(mixed[x],int)]

nums = [1, 2, 2, 3, 3, 3, 4]
unique = []
# this is a wrong logic. some edge cases will fail for sure
for x in range(0, len(nums)):
    if(nums[x]!=nums[x-1]):
        unique.append(nums[x])
print(unique)        

# correct logic
for x in nums:
    for y in unique:
        if(x  not in unique):
            unique.append(x)
        else:
            pass

print(unique)


nums = [1, 2, 3, 4, 5]
[ print(x, end=" ") for x in nums if x%2==0 ]


#Reverse a list using loop

test = [1, 2, 3, 4, 5,6]
n=len(test)
i=0

# This will also cause index out of range error in edge cases
while(i<=n):
    tmp = test[i]
    test[i] = test[n-1]
    test[n-1] = tmp
    i=i+1
    n=n-1
print(test)

# correct method

i=0
j=n
while i< j:
    test[i], test[j] = test[j], test[i]
    i+=1
    j-=1
print(test)