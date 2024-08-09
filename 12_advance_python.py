# (:=)walrus operator in python
# operator that is used to assign with expression at same time

# if (n := len([1,2,4,3,5])) != 3:
#     print(f"It has {n} elements")




# type definition (type hints) in python
# type hints are only suggestions and are not enforced
# 
# we have advance type hints that we get from typing module

from typing import List, Tuple

from typing import Union, Set, Dict

t : tuple = (1, 2, 3)
t : tuple[str, int, float] = (1, 2, 3)


# n = 5
# m : int = 5

# print(n.as_integer_ratio())
# print(m.as_integer_ratio())


# def func(a : int | str, b : float) -> str|int:
#     return f"{a}+{b}"

# print(func(1.45,3))
# print(func(3, 4.5))
# print(func("str", 34))




# match statement in python
# match case is same as switch case in other statement

# n = int(input("Enter the number: "))

# match n:
#     case 2:
#         print("B")
#     case 3:
#         print("C")
#     case 4:
#         print("D")
#     case 1:
#         print("Z")
#     case _: #default case
#         print("A")

# in match statement the default case must be the last statement



# we can merge two or more than two dictionaries, set using the | pipe operator

# dict1 = {2: 4, 6: 10}
# dict2 = {1:3, 20:8}
# dict3 = {4:6, 12:24}
# res_dict = dict1 | dict2 | dict3

# print(res_dict)


# tuple1 = {1,4}
# tuple2 = {2,5}

# print(tuple1 | tuple2)



# with statement can be used to write more than one open statements

# with(
#     open("file.txt") as f1,
#     open("poems.txt") as f2
# ):
#     print(f1.read())
#     print(f2.read())
    


# exception handling in python

# try:
#     a = int(input("Enter the number: "))
#     print(a/0)
# except Exception as t:
#     print(t)
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as z:
#     print(z)


# try:
#     a = int(input("Enter the number: "))
#     if(a == 0):
#         raise ZeroDivisionError ("Here our program can't use 0 as denominator")
#     print(12/a)
# except ZeroDivisionError as e:
#     print(e) 

# try with else in python

# for with else -> in this else will run only when the loop completed its execution normally and no break is encountered in between

# try:
#     a = int(input("Enter the number: "))
#     print(12/a)
# except TypeError as e:
#     print("TypeError")
# else: #else block will run only when the try block runs completely without any error
#     print("hello")



# try:
#     print(12/0)
# finally:
#     print("hello")

    # means if an exception is there then after execution of finally the program execution is aborted



__name__  # returns __main__ if we run it in same file
# but if it runs on another file where it is imported as module into another file then 


# if __name__ == '__main__':
#     print("hello") # this code will run only when this python file is running by itself and not from another file


# global keyword in python
# global keyword is used to change the value of global variables

# a = 5

# def func():
#     global a
#     a = 40
#     print(a)

# print(a)
# func()
# print(a)


# enumerate function in python

# l = [1, 34, 23, 56, 89]

# for index,item in enumerate(l):
#     print(f"The item at index {index} is {item}")




# list comprehensions in python

list = [1,2,3,4,5]

squaredList = [i*i for i in list]
# this will create a new list where there are elements stored as square of the elements of the list
print(squaredList)
