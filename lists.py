# Lists ordered sequence that can hold a varity of object type
# nothing but an array
myList = [1,2,3]
x = len(myList) #length of the array
x =  myList[1:]

myList.append(4) # push in Java script, will change the origional array
x = myList.pop() # same as in JS changes the original array // by defaulr index is -1 // the last element
x = myList.pop(0) # with pop the first element

aList = ["a","c","b","d"]
mList = [1,4,3,5,6,2]

aList.sort()
mList.sort()
mList.reverse()  # chaining No workin  :( 

print("------------------------")
print("output : ", x,myList,aList,mList)
print("------------------------")

