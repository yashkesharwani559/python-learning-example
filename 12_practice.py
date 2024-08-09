# open three files and except the error if file doesn't exist

# try:
#     with(
#         open("a.txt") as a,
#         open("b.txt") as b,
#         open("c.txt") as c
#     ):
#         print(a, b, c)

# except Exception  as e:
#     print(e)


# print third, fifth and seventh element of the list using enumerate function 

# list = [1,2,3,4,5,6,7,8]

# for i,item in enumerate(list):
#     if(i%2 == 0 and i != 0):
#         print(item)


# write a program to store the multiplication table of a user entered number in a list using list comprehension

# n = int(input("Enter the number: "))

# mulList = [f"{n} x {i} = {n*i}" for i in range(1,11)]

# print(mulList)


# write a program for a/b

# try:
#     a = int(input("Enter the number a: "))
#     b = int(input("Enter the number b: "))

#     if(b == 0):
#         raise ZeroDivisionError("The result is infinite")
    
#     print(f"The result is {a/b}")

# except ZeroDivisionError as e:
#     print(e)

# print("Thank you.. Visit again")


# store multiplication table in Tables.txt

n = int(input("Enter the number: "))

with (
    open("Tables.txt", 'a') as f
):
    for i in range(1,11):
        f.write(f"{n} x {i} = {n*i} \n")




