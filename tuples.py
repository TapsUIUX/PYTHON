# similar to lists but are immutable
# once element is assigne to an element we cannot reassign

t = (1,2,3,"a","a","b") #tuples
l = [1,2,3] #list

x = t[0]

x = t.count("a") # How many times a occurs in the tuple
x =  t.index("a") # returns  first index of the a

#t[0] = "new" # you cant assign

print("----------------------")
print(x)
print("----------------------")