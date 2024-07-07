#dictionary uses key value pairs

marks={ 
    "Srish":100,
    "shaq":100,
    "astha":65
}
print(marks)
print (marks["shaq"])   
#print(marks.keys())
marks.update({"hello":1, "astha":75})  #updates the whole dictionary
print(marks)

print(marks.get("shaq")) #gives you the marks of the specified key


