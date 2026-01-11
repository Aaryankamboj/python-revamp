def get_ready(org="TCS"):
    #return 1
    #print("Dhurandhar")
    print(f"I am in {org} company")

def details(name, age):
    print(f"I am {name} and I'm {age} years old")
    print(f"{name} is not a good person")
get_ready("Amazon")
get_ready("Google")
get_ready() # to test default param value



def args_test(name, age, gen):
    print(f"{name} with {age} and gender is {gen}")


details(name="Andrew", age="78") #keyword args
details(78, "andrew") #positional args


args_test("Narendra", age=90, gen="F")
args_test("Raman", gen="F", age=23)
args_test("Sachin","M", gen=63)


def myfunc(person, a,b):
    v1= person["id"]
    v2 = person["name"]
    #return v1, v2
    return a+b

person={
    "id":10,
    "name":"Trump"
}

#v1 = myfunc(person)
#print(v1)
add = myfunc(person, 5,6)
print(add)



# Syntax for function have positional args
def print_name(id,name, /):
    print(f"Hello {name} {id}")
#print_name(id=333, name="moosewala")

# Syntax for function having keyword args
def kwy_args(*, name="Diljit",id):
    print(f"Sat Sri Akal {name} paaji")

kwy_args(name="DJ",3)