class A:
    a = 5

class B(A):
    a = 10

class C(A):
    a = 45

class D(B,C):
    a = 89

    @staticmethod
    def show(a):
        print(a)

    @classmethod
    def cls_show(class_var):
        print(class_var.a)

    

    def func(self):
        print(self.a)


d = D()

# d.func()

# D.show(19)

# D.cls_show()

D.func(D)
D.func(d)
# d.func(D) not allowed
d.a = 45
D.func(D)
D.func(d)

# d.cls_show()
# D.cls_show()
# D.a = 45
# d.cls_show()
# D.cls_show()
# d.a = 39
# d.cls_show()
# D.cls_show()
