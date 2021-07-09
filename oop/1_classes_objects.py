class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        #pass

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking ...")
    
    def walk(self, location="home"):
        return f"{self.name} is walking in {location}..."

dog1 = Dog(name="Puppy", age=7)
#print(type(dog))
print(f"The name is {dog1.name}")
print(f"The name is {dog1.getName()}")
print(f"The age is {dog1.getAge()}")
dog1.bark()
print(dog1.walk(location="park"))
dog1.setAge(9)
print(f"The new age is {dog1.getAge()}")

dog2 = Dog(name="Tim", age=8)
print(f"The name is {dog2.getName()}")
print(f"The age is {dog2.getAge()}")