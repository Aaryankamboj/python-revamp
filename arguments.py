def arbargs(*args, name):
    print(type(args))
    [print(args[i]) for i in range(len(args))]
    print(f"Tuple tha {name}")

#arbargs(["Punjab", "UP", "Delhi"], "Tuple")


def combine(model="Lenovo", *args):
    print(f"This is the {model} laptop")
    print(args)

combine("Samsung","T13","T14", "T15")



def average(*nums):
    avg=0
    n=0
    for i in nums:
        avg=avg+i
        n+=1
    avg = avg/n
    return avg

avg = average(1,3,8,2,3,5,10,13,89)
print(avg)


def MCA(datatype,**stds):
    print(type(stds))
    print(datatype)
    print(stds["name"])
    print(stds["age"])
    print(stds["lname"])
    print(stds["roll"])
    for i in stds.items():
        print(i)



MCA("Dict" ,name="Aman",age=25,lname="Kumar",roll=19)








# To unpack the data

def unpack(a,b,c, fname, lname):
    print(a,b,c)
    print(fname)
    print(lname)

nums=[1,2,3]
names={"fname":"VK", "lname":"Kohli"}
unpack(*nums, **names)
global x
x=100
(
    print(x)
)