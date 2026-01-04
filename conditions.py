age=10
if age>18:
    print("Eligible for voting")
elif age >17 and age <18:
    print("Almost eligible")
else:
    print("Not at all eligible")



print()
a=10.9
b=10.99
c=9
if a>b:
    if a>c:
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")
else:
    if b>c:
        print(F"{b} is greatest")
    else:
        print(f"{c} is greatest")


name = "Babbu Maan"

if type(name)!=int: print("correct")

print("coorect") if type(name)!=int else print("incorrect")


v1=10
v2=20
bigger= v1 if v1>v2 else v2
print(bigger)

if type(v1)==int and type(name)==int:
    print("Both are int")
else:
    print("Something is diff")

flag= not (False)

print(flag)

age=0
if age <18 and name.__contains__("Babbu") and v1 not in [50,40]:
    print("nhi")
else:
    print("Go ahead")


tagline= "This is a container"
flag=tagline.__contains__("cont")
print(flag)