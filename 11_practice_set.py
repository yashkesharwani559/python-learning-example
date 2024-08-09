# problem 1
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __len__(self):
        return 2


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __len__(self):
        return 3

obj = ThreeDVector(1,2,3)
print(obj.i,obj.j,obj.k)

print(obj)
print(len(obj))





# create Animal->Pets->Dog(bark())

# class Animal:
#     pass

# class Pet(Animal):
#     pass

# class Dog(Pet):
        # @staticmethod
#     def bark():
#         print("barking...")


# class Employee:
#     salary = 20000
#     increment = 10

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*(1+self.increment/100)
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((salary/self.salary)-1)*100

# emp = Employee()
# # print(emp.salary)
# # emp.salary = 20
# # print(emp.salary)

# print(emp.salaryAfterIncrement)
# emp.salaryAfterIncrement = 25000
# print(emp.salaryAfterIncrement)



# class Complex:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def __add__(self, self2):
#         return Complex(self.i+self2.i,self.j+self2.j)
    
#     def __mul__(self, self2):
#         return Complex(self.i*self2.i, self.j*self2.j)
    
#     def __str__(self):
#         return f"{self.i}i + {self.j}j"


# c1 = Complex(2,3)
# c2 = Complex(6,8)

# c3 = c1 + c2
# c4 = c1 * c2

# print(c1,c2,c3,c4,sep="\n")








