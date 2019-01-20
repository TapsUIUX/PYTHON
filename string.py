msg = "hello World"
print(msg)
print(len(msg))

#Python Data Types
# int, float,str,list (array) ,dict (dictionaries, object),tup (ordered immutable sequence of object)
#set ( u ordered collection of unique objects ), bool : Logical ture and False.

sum = 10 
print(type(sum))

#string Manipulation

x = msg[0]
x= msg[-1]

#slicing

x=msg[2:] # leave 2  
x=msg[:3] # get 3
x= msg[6:9] #after 6 upto 9
x = msg[::2] # default step size 1 
x=msg[1:6:2]
x=msg[::-1] # it will reverse


# immutabale
x= "Sam"
#concate
x = "p" + x[1:]
x = "p"*10   # will print 10 P s
x = "p"+"20"  # cannot concate string with Numnber Throws error

x = x.upper()
x= x.lower()

x = x.split("2") # same as JS 

#Print Format  
# .format()

x = "hello world {}".format("INSERTED") #{} will be replaced by INSERTED

x = "{} {} {}".format("a","b","c") #will go in order

x = "{2} {2} {1}".format("a","b","c")  # will print accordiong to Index  more the three {} throw tuple error

x = "{a} {c} {b}".format(a="a",b="b",c="c") # more redable with the variable names

#Float formating with the format method.

result = 100/777

x ="The result is {r:1.3f}".format(r=result) # {r:1.3f} before decimal and precision.  more than 1. will add white spaces.

result = 100/7

x ="The result is {r:1.3f}".format(r=result) # {r:1.3f} before decimal and precision.  more than 1. will add white spaces.

# you can use format directly same as in JS

# Ne F string in PYTHON 3 , String Interpolation
x = f"this result is {result}"

print("----------------------")
print(x)
print("----------------------")