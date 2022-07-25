class A:
    classvar1 = "I am a class variable in class A"  # if other two statements not run then this statement will run

    def __init__(self):
        self.var1 = "I am inside A constructor"
        self.classvar1 = "Instance variable in class A"  # firstly this will run as it look for instance variable


class B(A):
     classvar1 = "I am inside class B"  # if instance variable is not present then this statement will execute


a = A()
b = B()
print(b.classvar1)
