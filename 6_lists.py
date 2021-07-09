newList = [1, "hello", 1.34, False, [1,2,3]]
numList = list([15,21,14,8,1,9])
numTupla = list([1,2,3,4])

print(newList)
print(type(newList))

print(numList)
print(type(numList))

print(numTupla)
print(type(numTupla))

#Create dynamic lists
list2 = list(range(0, 10))
print(list2)
print(type(list2))

#list properties
#print(dir(newList))

print(len(newList))
print(newList[2])
print(newList[-1])

#Search/Find/replace
print('hello' in newList)
newList[1] = "bye"
print(newList)

newList.append({'saludo': 'hola'})
print(newList)
newList.extend([True, 487])
print(newList)

newList.insert(-2, "bye")
print(newList)

newList.pop()   #Deletes last item
newList.pop(4)   #Deletes index item
newList.remove("bye")   #Deletes first found item
print(newList)

#Order
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)

print(newList.index('bye'))
print(newList.count('bye'))

#newList.clear()
#print(newList)