class Person:
    number_of_people = 0
    GRAVITY = -9.8  # Constant

    def __init__(self, name) -> None:
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people +=1

person1 = Person(name="Tim")
print(person1.number_of_people)
person2 = Person(name="Jill")
print(person2.number_of_people)

#Person.number_of_people=8
#print(person1.number_of_people)
#print(person2.number_of_people)

#ClassMethods defined for internal permissions
print(person1.get_number_of_people())