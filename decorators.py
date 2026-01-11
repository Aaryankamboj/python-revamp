def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def tellSize(func):
    def size():
        return type(func())
    return size

@changecase
def myfunc():
    return "Lissa Healy"

print(myfunc())

@tellSize
def func2():
    nums=[1,2,5,4]
    return
print(func2())