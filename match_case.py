'''
num=int(input("Enter the number -> "))

match num:
    case 1 | 5 | 6 |9:
        print("India")
    case 2:
        print("USA")
    case 3:
        print("UK")
    case _:
        print("No other options found")





i=1
while(i<6):
    print(f"Hi for {i} time")
    i+=1
else:
    print(f"Value of {i} is not less than 6 now")
'''

for i in "Narendra bhai":
    print(i, end="")
print()
for i in ["red", "tasty", "big"]:
    for j in ["apple", "banana", "cherry"]:
        print(i, j , end = " ")
    print()