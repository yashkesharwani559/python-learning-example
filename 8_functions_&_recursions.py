# a function is a group of statements used to perform a specific task.

# function to print average of three number
# def avg(a, b, c):
#     return (a+b+c)//3

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))

# print(f"Average of {a}, {b}, {c} is {avg(a,b,c)}")


# program to greet a person given its name
# def greet(name):
#     print(f"Hello {name}, Bhai... ")

# name = input("Enter your name: ")

# greet(name)


# swapping of two values in python
# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))

# def swap(a, b):
#     c = a
#     a = b
#     b = c

# print(f"{num1}  {num2}")
# swap(num1,num2)#pass by value occurs
# print(f"{num1}  {num2}")


# def greet(name, ending="Thank you"):#default argument
#     print(f"{name}, {ending}")


# greet("Yash")
# greet("Rahul", "bye bye")


# factorial using recursion
def fact(n):
    if(n == 1):
        return 1
    
    return n * fact(n-1)


print(fact(5))