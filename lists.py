players = ["Virat", "Rohit", "Dhoni"]
print(players)
print(players[2])
print(len(players))
n = len(players)
for i in range(0, n):
    print(f"{players[i]} comes at {i+1} wicket down")

variety = [20, 5.6, "Virat", True, " "]
print(variety)
print(type(variety[0]))
print(type(variety[2]))
print(type(variety[3]))
v_len = len(variety)
for i in range(v_len):
    print(f"{variety[i]} is of {type(variety[i])}")

sample = list(("name", "age", 7.9, "", True))
print(type(sample[0]))
print(type(sample[3]))
sample[3] = "Empty"  # List are mutable
print(sample)

# There are 4 types of Array collections in python
"""
1. List
2. Tuple
3. Set
4. Dictionary
"""

size = len(sample)
for i in range(size-1,0,-1):
    print(f"Item at index {i} is {sample[i]}")

sample[0]=109
sample[0:2] = list(("name", "umar"))
print(sample)
sample[0:2] = ["details"]
print(sample)
sample.insert(4, "False") # To insert an element at specific position
print(sample)

name = input("Enter your name ")
sample.insert(5, f"{name}")
print(sample)