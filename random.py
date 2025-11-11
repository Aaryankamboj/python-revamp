import random
x=int(34.44)
print(x)

#string = int("575")
#print(string)

print("Aaryan")
print("It's very nice")

name = "Salman Singh"
for x in name:
    print(x.upper(), end="")
print()
print("###################")

f_name = name[0:6]
print(f_name)
print(name[::5])

name = f_name + " " + name[7:]
print(name)

num=45
print(f'The price is {num:.3f}')