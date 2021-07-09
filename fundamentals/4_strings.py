myStr = "hello_all_world"

#Properties of an object: command "dir"
#print(dir(myStr))
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello", "bye").upper())    #Method chaining (Métodos encadenados)

print(myStr.count("l"))
print(type(myStr.count("l")))

print(myStr.startswith("he"))
print(type(myStr.startswith("he")))

print(myStr.endswith("world"))
print(type(myStr.endswith("world")))

print(myStr.split("_"))
print(type(myStr.split("_")))

print(myStr.find("l"))
print(type(myStr.find("l")))

print(myStr.index("l"))
print(type(myStr.index("l")))

print(myStr[4])
print(myStr[-3])

#Length
print(f"The text length is: {len(myStr)}")
print("The text length is: " + len(myStr).__str__())
print("The text length is: {0}".format(len(myStr)))
