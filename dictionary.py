#Dictionalr are the unordered mapping for storing objects.
# key value pair OBJECT actually


y = {"a" : "A" , "b":"B" , "c" : {"c1":"C1","c2":"C2"} ,"d":["D1","D2","D3"]}

x = y["a"]

x = y["c"]["c1"].lower()

y["c"]["c3"] = "C3"

x = y

print("----------------------")
print(x)
print("----------------------")