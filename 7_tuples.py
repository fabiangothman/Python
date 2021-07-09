#Data which doesn't change (Inmutabes)
newTupleLiteral = (1, 2, 3)
newTuple = tuple((4, 5, 6, 7, 8, 9))
print(type(newTupleLiteral))
print(type(newTuple))

#Just one date
# x = tuple((1))
# x = (1)
aloneTuple = tuple((1, ))
print(aloneTuple)

#Tupla properties
#print(dir(newTuple))

print(newTuple[2])

#You can't re-assign a tuple data
# newTupleLiteral[2] = 10
# print(newTupleLiteral)

#Delete
del newTupleLiteral