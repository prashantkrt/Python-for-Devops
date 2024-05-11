marks=(95,97,92,90,90,98,97,97,97,95,95)
print(marks[0:4])
#marks[0]=99 error since tuple we won't be able to edit
print(marks.count(97))
print(marks.index(97))

i=(1,"Hello",True,[1,2,3])
print(type(i))
print(i)

i=(1,2,3,False,(1,2,True))
print(i[4][2])

#tuples are immutable we cannot change any values in tuple
i=(1,2,3)
j=(4,)
print(i+j)
print(i)
print(j)

#converting tuple into the list
list = list(i)
print(list)
list.append(4)
print(list)


tuple = (1,2,3,4,4,4,4,2,2,2,1,1,1,2,3,3,3,3)
count = tuple.count(4)
print(count)
print(len(tuple))