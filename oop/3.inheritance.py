class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old!")
    
    def speak(self):
        print("Uhh?")

class Cat(Pet):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"Meow")

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}!")

class Dog(Pet):
    def speak(self):
        print("Rawf")

class Fish(Pet):
    pass

pet1 = Pet(name="Tim", age=9)
pet1.show()
pet1.speak()

cat1 = Cat("Bill", 15, "Red")
cat1.show()
cat1.speak()

dog1 = Dog("Jill", 12)
dog1.show()
dog1.speak()

dog1 = Fish("Nemo", 2)
dog1.show()
dog1.speak()