marks = [98,97,96,93]
print(marks)
print(marks[1])
print(marks[0:4])

marks2=[98,"maths",80,"English",90,"Chemistry"]
print(marks2)

print(marks[1:3])
print(marks2[1:3])


marks.append(100)
marks.insert(0,101)
marks.remove(100)
marks.sort()
print(marks)

print(99 in marks)
length = len(marks)
print(length)

print()
for i in marks:
    print(i)
  
print()    
for i in range(len(marks)):
    print(marks[i])
    

print()    
i=0
while i<len(marks):
    print(marks[i])
    i+=1
    
marks.clear()
print(marks)    

    
         