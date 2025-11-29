import random
x=int(34.44)
print(x)

#string = int("575")
#print(string)

print("Aaryan")
print("It's very nice")

name = "SALman Singh"
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
print(name.capitalize())
print(name.casefold())
print(name.center(20,'&'))
print(name.count(' '))
print(name.encode())
print(name.endswith('hi'))
txt = "H\te\tl\tl\to"
print(txt.expandtabs(8))
print(name.find('S'))
print(name.format('a'))


txt2 = "My name is {f_name} and I am {age} years old".format(f_name="aaryan", age=23)
txt4 = "My name is {} and I am {:x} years old".format("aaryan", 23)
print(txt4)
print(txt4.upper())
txt4[1].capitalize()
print(txt4.capitalize())

nm = "aryan"
print(nm.upper())
print(nm.capitalize())
print(nm.lower())

nm = "       aaryan Kamboj"
print(nm.strip())
nm="Hello, Programmers!!, What's up"

print(nm.split(','))
a="Sri"
b="Amritsar"
c="sahib"
c = a+ ' ' + b + ' ' +c
print(c)

work_ex=3
desc = "I am a programmer with {} years of ex".format(work_ex)
work_ex2=1
print(f"My {work_ex*3} YOE is \"much\" greater than {name} {work_ex2} YOE")
print(desc)
print(" '\'xhh 7")

print(10>9)