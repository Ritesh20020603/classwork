class person:
    no_of_leaves = 6
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
ob1 = person("harry", 54, "instructor")
ob2 = person("larry", 5, "student")
ob1.change_leaves(76)  # changing class variables
print(ob1.no_of_leaves)
