#list in py is array in java

friends=["hello", "hi", "bye", "you", "me" ,"together"]

print(friends[1])

friends[0]="garpes"

print(friends)

 #print(friends[1:5])
friends.sort() #sorts teh list alphabetically   
friends.reverse()  # prints teh reverse string starting from behind
friends.append("hey") # adds hey at the end of the string
friends.insert(4, "why")  #inserts why at index 4
friends.pop(3)  #will pop out the word at index 3
friends.remove("bye") #will remove hi from the list
print(friends)



#tuple is similar as a list but the difference is that list is mutable, you can cahneg the original list and tuple is immutable like strings, means that it cannot be changes, can only be made into a  new string
#tuple can be defined by putting round brackets
a=(1,2,3,4,5,6,7,8,9)
print(type(a))

#if there is only one element ina  tuple, then put a comma after taht one element otherwise python will consider taht one elemnet as an integer or string
