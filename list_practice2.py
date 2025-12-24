'''nums = [2,3,6,7,9,12]

sq_list =list(())

for i in range(0, len(nums)):
    if((nums[i]%3) == 0):
        sq = pow(nums[i], 2)
        sq_list.append(sq)

print(sq_list)


#####################
nums = [2, 3, 2, 5, 3, 7, 5, 9]
tmp = []
for i in range(0, len(nums)):
    for j in range(1, len(nums)):
        if(nums[i]!=nums[j] and nums[i] not in tmp):
            tmp.append(nums[i])

print(tmp)


for i in nums:
    if(i not in tmp):
        tmp.append(i)
print(tmp)


i=0
j=1
n=len(nums)
while(i<n and j<=n):
    if(nums[i]!=nums[j] and nums[i] not in tmp):
        tmp.append(nums[i])
        i+=1
        j+=1
print(tmp)
'''

#Q Find all pairs in a list that sum to a given number
'''nums = [2, 4, 3, 5, 7, 8, 1]
nums.sort()

i=0
j=len(nums)-1
pairs = list()
target = int(input("Enter the target -> "))

while(i<j):
    if(nums[i]+nums[j] == target):
        pairs.append((nums[i], nums[j]))        
        i=i+1
        j=j-1
    
    elif(nums[i]+nums[j] > target):
        j=j-1
    else:
        i=i+1

print(pairs)


'''
 
#Q2 - Flatten the list
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[0][1])
print(type(nested))



#q3 - 2nd larget number in the list
nums = [10, 20, 19, 45, 99, 99, 45]
#45,20,4,45,99,99,90

i=0
j=len(nums)-1

for i in range(0, len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            nums[i],nums[j]=nums[j],nums[i]

print(nums)

for j in range(len(nums)-1, 0, -1):
    if(nums[j-1]!=nums[j]):
        print(f"Second largest element is {nums[j-1]}")
        break
print("Finish")