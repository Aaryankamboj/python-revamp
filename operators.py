x=['apple', 'banana']
y=['apple', 'banana']

print(x is y) # because both are diff objects pointing to diff memory locations
print(x is not y)
z=x
print(z is y)

if('apple' in x):
    print("Apple is present")
else:
    print("Out of stock")

name = "Donald Trump"
print('Don' in name)

# 5 = 10100
# 3 = 011
# & = 001 [1]
# | = 111 [7]
# ^ = 110 [6] - Only one of the 2 bits should be 1
# << = 5<<2 = 20
# >> = 5>>2 = 101 = 001 = [1]
# ~ = ~(101) = 010 = 2
a,b=5,3
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(a>>2)
print(~a)
print((5+2)-(3-2))  #7-1
print(~4)
