name = "ayush"

nameshort = name[0:3] 
print(nameshort)
character1 = name[1]
print(character1)

name = "ayush"

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

#string_function

name = "ayush"

print(len(name))
print(name.endswith("sh"))
print(name.startswith("ay"))
print(name.capitalize())
