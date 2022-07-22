class person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role


ob1 = person("harry", 54, "instructor")
ob2 = person("larry", 5, "student")
print(ob1.name)
print(ob1.role)
print(ob1.age)
print(ob2.name)
print(ob2.age)
print(ob2.role)


