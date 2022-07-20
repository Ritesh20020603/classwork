# multilevel inheritance
class a:
    def f1(self):
        print("A")


class b(a):
    def f2(self):
        print("B")


class c(b):
    def f3(self):
        print("C")


ob = c()
ob.f1()
ob.f2()
ob.f3()


