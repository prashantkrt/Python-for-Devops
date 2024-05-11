str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

print()

text = "Python is awesome"
words = text.split()
print("Words:", words)

print()

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

print()

text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

print()

text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

print()

text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
    
text="prashant"
print(text.capitalize())
print(text) 

print(text.isupper())
print(text.islower())


text="     pr     "
print(text.rstrip())
print(text.lstrip())
print(text.strip())

i="Parrot,Peacock"
list=i.split(",")
print(list)
print(list[0])

print()
for i in range(len(list)):
    print(list[i])
    
print()

for i in list:
    print(i)
    

  