class a:
    def f1(self):
        print("A")


class b(a):
    def f2(self):
         print("B")


class c(a):
    def f3(self):
        print("C")
        

ob1 = c()
ob2 = b()
ob1.f1()
ob2.f2()
ob1.f3()
