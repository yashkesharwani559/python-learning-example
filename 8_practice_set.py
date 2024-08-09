# write a program to find the greatest using function

# def max_of_three(a, b, c):
#     if(a>b):
#         if(a>c):
#             return a
#         else:
#             return c
#     else:
#         if(b>c):
#             return b
#         else:
#             return c


# print(max_of_three(40, 10, 30))


# program using function to convert celsius to farenheit

# def change_temp(celsius):
#     return celsius*9/5 + 32

# print(change_temp(37))


# we have to give empty string to end attribute of print() method to stop a new line gap


# sum of n natural numbers using recursion

# def sum(n):
#     if(n == 1):
#         return 1
    
#     return n + sum(n-1)


# print(sum(10))


# write a program to print first n lines of the pattern

# ***
# **
# *
# n = 3

# n = 3

# def pattern(n):
    
#     if(n==1):
#         print("*")
#         return
    
#     print("*"*n)
#     pattern(n-1)

# pattern(n)



# function that converts inches to cm

# def change_cm(inch):
#     return inch*2.54

# print(change_cm(5))


# write a function to remove an element from the list and then strip it again at the same time


# def remove_word(list, word):
#     res = []

#     for item in list:
#         if item != word:
#             res.append(item.strip(word))

#     return res

# list = ["Harry", "Rohan", "Mohan", "an"]

# print(remove_word(list, "an"))



# program to print multiplication table of a given number

def multiplicatiion_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


multiplicatiion_table(5)

