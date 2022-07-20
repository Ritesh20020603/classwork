# multiple inheritance
class a:
    def f1(self):
        print("K")


class b():
    def f2(self):
        print("L")


class c(a, b):
    def f3(self):
        print("M")


ob = c()
ob.f1()
ob.f2()
ob.f3()


