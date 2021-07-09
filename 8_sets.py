colors = {"red", "white", "blue"}

print(colors)
print(type(colors))

#Set properties
# print(dir(colors))

colors.add("Violet")    #Add at beginning because there are not indexes
print(colors)

#Find
print("red" in colors)

colors.remove("red")
print(colors)

#Clean/Delete
colors.clear()
print(colors)
del colors