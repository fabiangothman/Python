product = {
    "name": "book",
    "amount": 3,
    "price": 4.99
}
person = {
    "firstname": "Juan",
    "lastname": "Perez"
}

print(type(product))
print(type(person))

#Dictionary properties
# print(dir(colors))

print(product.keys())
print(product.items())

#Clean/Delete
person.clear()
print(person)
del person