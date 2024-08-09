# name = input("Enter your name: ")
# marks = int(input("Enter your marks: "))
# phone = int(input("Enter your phone no.:  "))

# s = "The name of the student is {}, his marks is {} and phone number is {}".format(name,marks,phone)

# print(s)


table = [str(7*i) for i in range(1,11)]

# s = "\n".join(table)

# print(s)


# l = [1, 4, 10, 21, 20, 35]

# divisibleFive = lambda x : x%5==0

# res = list(filter(divisibleFive, l))

# print(res)



# program to find max of a list using reduce()

from functools import reduce

l = [1, 10, 3, 2, 6]

def max(a,b):
    if(a>b):
        return a
    else:
        return b

res = reduce(max, l)

print(res)



