class a:
    def f1(self):
        print("A")


class b(a):
    def f2(self):
        print("B")


class c(a):
    def f3(self):
        print("C")


class d(b, c):
    def f4(self):
        print("D")


ob1 = d()
ob1.f1()
ob1.f2()
ob1.f3()
ob1.f4()
