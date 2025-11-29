print("Hey Guys 😊..welcome to string classes")
print(10<90)
print(bool("string"))
print(bool(10))
print(bool()) #False
print(bool('')) #False
print(bool(0)) #False
print(bool([]))
print(bool({}))

class testing():
    def __len__(self):
        return 0
    
    def returnSum(self, a, b):
        return a+b
    
myObj = testing()
ans = myObj.returnSum(10,3)
print(ans)


def bool_func():
    return True

if bool_func():
    print("Yes! you are innocent")
else:
    print("No! you are also good")

print(isinstance(myObj, testing)) 

