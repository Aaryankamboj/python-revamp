a = frozenset({1,2,4,50})
print(type(a))
b=[5,6,7,91]
c=a.copy()
print(c)
a=a.union(b)
a=a.difference(b)
print(a)

flag = a.isdisjoint(c)
print(flag)

z = c.issubset(a)
z = c <=a
z= c.issuperset(a)
print(z)

print(z)