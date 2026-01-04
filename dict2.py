names={
    2:"Raman",
    3:"Lala"
}

x = names.setdefault(1, "Modiji")
print(x)
print(names)

names.update({4:"rahul"})
print(names)