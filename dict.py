brand={
    'name':'Apple',
    'id':17,
    'price':99999,
    "sales":[100,200,300]
}

print(brand)
print(brand["name"])
print(len(brand))
print(brand['sales'][0:2])

reason  = str("Payment UPI link")
link = f"This is the reason for {reason}"
print(link)


# Dict constructor
devices = dict(name="laptop", price=100, model="India" )

print(devices)

dev=devices.get("name")
print(dev)
print(devices.keys())
print(devices.values())
print()
print(devices.items())

if "name" in devices:
    print("Available")


brand['id'] =90
print(brand)

brand.__delitem__('sales')
print(brand)

brand.update({"year":2025})
print(brand)

brand["type"]="Ipad"
print(brand)

brand.pop("type")
print(brand)
brand.popitem()
print(brand)




#del brand

for x in brand:
    print(brand[x])

print()
for i in brand.values():
    print(i)

for j in brand.keys():
    print(j)

print()
for key,val in brand.items():
    print(key, "->", val)


dups = brand.copy()
print(dups)

prods=dict(dups)

print(prods)

my_exp={
    "company1":{
        "name":"DXC",
        "tenure":2.5
    },
    "company2":{
        "name":"LimeChat",
        "tenure":0.11
    },
    "total":{
        "exp" : 3.5,
        "no_of_companies": 2
    }
}


print(my_exp["company1"]["name"])
print(my_exp["company1"]["tenure"])



for i in my_exp:
    print(i)


pat1={
    "name":"SRK", "age":60
}


pat2={
    "name":"Amir", "age":60
}


pat3={
    "name":"Salman", "age":60
}


pat_list={
    "p1":pat1,
    "p2":pat2,
   "p3":pat3
}

print(pat_list["p1"])



for x, obj in pat_list.items():
    print(x, obj)

print()

pat1.clear()
print(pat1)

p_copy =  pat2.copy()
print(p_copy)

keys = [1,2,3]
values = False,True
p_keys= dict.fromkeys(keys,values)
print(p_keys)