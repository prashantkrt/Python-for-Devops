name="Tony Stark"
print(name)
print(name.upper()) #creates the new string
print(name)

print(name.lower())
print(name)

print(name.find('a')) #index value
print(name.find('m'))
print(name.find("Tony"))
print(name.find("ark"))
print(name[0])  #character
print(name[0]=='T')  #true


print(name.replace("Tony","Rony"))
print(name)

print("T" in name)#true

val="Eating  apple apple apple banana"
print(val.count("apple"))