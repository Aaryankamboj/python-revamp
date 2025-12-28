data =("apple", "atta", 4.5, 94)
print(data)
c = data.count(94)
print(c)

print(len(data))

a=('apple') # not a tuple
print(type(a))

b = ('apple',)
print(type(b))

for i in range(len(data)-1, -1, -1):
    print(data[i], end=" ")
print()
del_data = ("testing", )
data+=del_data
print(data)

print(data)

del del_data
#print(del_data)


fruits = ("apple", "banana", "orange", "cherry", "berry")
(a,*b,c)=fruits
print(a)
print(b)
print(c)

for x in fruits:
    print(x)







print()
nums = (1,2,3)
tmp = nums
print(tmp)

nums=nums*2
print(nums)

tmp = (data, type(data), nums)
print(tmp)

print(nums.count(3.0))
print(nums.index(3))