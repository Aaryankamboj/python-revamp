# a,b=10,20
# # a,b=b,a
# name = "Shahrukh"

# def test_func():
#     a=19
#     print(a,b)
#     c=90
# # print(a,b)

# test_func()
# # print(c)
# # try(c):
# #     print(c)
# # finally:
# #     print("Not existed")

# x,y,z = "aman", "raman", "daman"
# print(x,"is a friend of", y, z)
# print(f"{x} is a friend of {y}")

# print(f"{a} + {b} is {(a+b)*2}")

glob_vari = "I am a global var"

def func_test():
    global global_vari 
    glob_vari= "badal gya mai"
    print(glob_vari)

func_test()

print(type(glob_vari))