marks = {
    "ayush" : 100, 
    "Aman"  : 39,
    "vishal" : 89,
}
print(marks, type(marks))
print(marks,["ayush"])

 # It is mutable
 # It is indexed
 # It is unordered
 # cannot contain duplicate keys 

 # Method of Dictionary............


marks = {
    "ayush": 100,
    "imtiyaz": 56,
    "shreya": 23,
    0: "ayush"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"ayush": 99, "varshita": 100})
# print(marks)

print(marks.get("ayush")) # Prints None
print(marks["ayush"]) # Returns an error

# Create an empty dictionary Allow 4 Friend toenter their favourite Code

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})


print(d)
