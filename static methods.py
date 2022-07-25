class person:
    no_of_leaves = 6

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    @staticmethod
    def print_details(string):  # if we didnot want to take self and cls as initial value in function then we use static method
        print("this boy is "+string)


ob1 = person("harry", 54, "instructor")
ob2 = person("larry", 5, "student")
ob1.print_details("harry")  # we can use it by using instance or a class
person.print_details("larry")

