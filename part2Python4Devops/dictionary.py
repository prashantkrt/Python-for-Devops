dic={"key1":1,"key2":2}
marks ={"english":89,"maths":97,"science":91}
info={"Fruit1":"Apple","Fruit2":"Guava"}

print(marks["english"])
print(dic["key1"])
print(info["Fruit1"])

print(info)

myDictionary={1:"Prashant",2:True,3:24}
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())# list of tuples for key : val

for i in myDictionary.keys():
    print(myDictionary[i])
 

#Adding into the dictionary 
myDictionary["key4"]="Key4Val"
print(myDictionary) 


studnet_Dictionary ={'name':'Rahul','age':21,'city':'Mumbai'}
marks_Dictionary={'English':70,'Maths':80,'Science':80}

studnet_Dictionary.update(marks_Dictionary)
print(studnet_Dictionary)   

#remove 
print(studnet_Dictionary.pop('city'))
print(studnet_Dictionary)

print(marks_Dictionary.popitem())# removes the last element
print(marks_Dictionary)

#delete the dictionary
#del marks_Dictionary

del marks_Dictionary['Maths']
print(marks_Dictionary)

marks_Dictionary.clear()
print(marks_Dictionary)


