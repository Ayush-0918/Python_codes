a = (1,45,342,3424,False, "aayush", "varshita")
print(a)
print(type(a))


#Method of tuples

a = (1,45,342,3424,False, 45, "aayush", "varshita")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))


#len()
#Returns the number of elements in the tuple.

t = (1, 2, 3)
print(len(t)) 


#sum()
#Returns the sum of the elements (only numeric values).

t = (10, 20, 30)
print(sum(t))

#max() and min()
#Returns the largest or smallest value.

t = (5, 1, 9, 3)
print(max(t))  
print(min(t))
