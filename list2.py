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