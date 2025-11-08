print(type('hello'))
print(("He'llo"))


txt = """this is a 
mulitple line 
string 
"""
#
'''print(txt[5:0:-1])
for x in txt:
    print(x, end="")


print(len(txt))

print("string" in txt)

if "line" in txt:
    print("YES!, It's present 😊")

if "is" not in txt:
    print("Not Present")'''

print(txt[1:7])
print(txt[:5])
print()
print(txt[2:])

txt="Jibhaisaab"
print(txt[-1:-8:-1])

print(txt.upper())
print(txt.lower())
a = "he llo  j i "
#The strip() method removes any whitespace from the beginning or the end:
print(a.strip())

print(a.replace('h', 'y'))
print(a)

print(a.split(' '))

Fname = "Aaryan"
Lname =  "Kamboj"

name = Fname + " " + Lname
print(name)

age = 24
# Not valid and will give an error
#intro = "My name is AK and I'm " + age
intro = F"My name is Ak and I am {age} years old"
print(intro)

def func(a,b):
    ab2 = f"a^2 + b^2 = a*a + b*b + 2*{a}*{b})"
    return ab2

print(func(5,2))


intro = f"My name is {name} and I am {age:.2f} years old"
print(intro)

dollars = 99
rs = f"The price of Rs is {dollars * 86}"
print(rs)

adj = "highest"
txt = f"We're at the edge of world's most {adj} point which is the \"Mount Everest\" "
print(txt)