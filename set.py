
e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 


print(s)


# Method of sets 


s = {1, 5, 32, 54,5, 5, 5, "ayush"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))
