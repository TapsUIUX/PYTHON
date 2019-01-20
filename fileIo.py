# how to genedate file
myFile =  open("text.txt")

x =myFile.read()


x =myFile.read() #  second time will return blank because the cursor is moved.

myFile.seek(0) # move the cursor to the begining

x =myFile.read()


myFile.seek(0)

x = myFile.readlines() # will convrt each line in to a element in the list

# Best practice to open file

myFile.close() # close the file

# We will be using the below way to rad the file so that we dont have to close

with open('text.txt') as myFile: 
    x =  myFile.read()


# mode r rsad only
# mode w wriote only will over write or create new
# mode a will append , will add if there is no file
# r+ read and wiriting
# w+ writeing and reading. Overwriting exoistiang file or creates a new file.


with open('text.txt',mode="r") as f:  # default mode is r Read
    x = f.read()

with open('text.txt',mode="a") as f:  
    f.write("\ntext file line 4")

with open('text.txt',mode="r") as f:   
    x = f.read()

with open('text_new.txt',mode="w") as f:   
    f.write("this is a new file") # create s new file return the lenght of the file too

print("----------------------")
print(x)
print("----------------------")