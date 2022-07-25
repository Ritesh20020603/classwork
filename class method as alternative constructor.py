class person:
    no_of_leaves = 6

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    @classmethod  # decorator
    def from_dash(cls, string):
        return cls(*string.split("-"))

ob1 = person.from_dash("harry-54-instructor")  # passing string instead of values
ob2 = person("larry", 5, "student")  # passing values
ob3 = person.from_dash("karan-42-professor")  # class method as alternative constructor
print(ob3.role)
print(ob1.role)
