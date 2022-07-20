# single inheritance
class A():
    def func1(self):
        print("a")
class B(A):
        def func2(self):
            print("b")
ob = B()
ob.func1()
ob.func2()
