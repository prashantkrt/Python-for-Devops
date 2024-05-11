marks ={23,23,23,5,6,78}
print(marks)

for score in marks:
    print(score)
 
#gives empty set    
set1=set()
print(set1)

set2=set({1,2,3})
print(set2)

set2.add(44)
set2.add(90)
print(set2)

#removes 
set2.pop()
print(set2)

# two ways to remove
print()

print(set2)
set2.remove(44)

print(set2)

set2.discard(2)
print(set2)

 
