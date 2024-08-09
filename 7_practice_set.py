# wap to print multiplication table of a given number

# n = int(input("Enter the number: "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# using while loop

# i = 1
# while(i<11):
#     print(f"{n} x {i} = {n*i}")
#     i += 1


# wap to greet all the persons whoose name starts with the letter 's' in the list 'l'

# l = ["Harry", "Sachin", "Sohail", "Raghav", "Satyam"]

# for i in l:
#     if(i.lower().startswith('s')):
#         print(f"Hello {i} Bhai,")



# wap to find whether a given number is prime or not

# n = int(input("Enter the number: "))

# flag = True
# for i in range(2, int(n/2)):
#     if(n%i == 0):
#         flag = False
#         break

# if(flag):
#     print(f"{n} is a prime number. ")
# else:
#     print(f"{n} is not a prime number. ")



# find the sum of n natural numbers using while loop

# n = int(input("Enter the number: "))

# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i += 1

# print(sum)


# program to print factorial of a given number using for loop

# n = int(input("Enter the number:"))

# res = 1

# for i in range(1,n+1):
#     res *= i

# print(f"factorial of {n} is {res}")



# program to print star pattern 
#   *
#  ***
# *****
# for n = 3

# n = 3

# for i in range(3):
#     for j in range(3-i-1):
#         print(" ", end="")
    
#     for j in range(2*i+1):
#         print("*", end="")
#     print("")
# or
# n = 3
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i+1))



# *
# **
# ***
# n = 3
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print("")
# or

# n=3
# for i in range(n):
#     print("*"*(i+1))


# * * *
# *   *
# * * *
# n=3
# for i in range(3):
#     for j in range(3):
#         if(i==0 or i==2 or j == 0 or j==2):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print("")

# or

n = 3
for i in range(0,n):
    if(i==0 or i==n-1):
        print("* "*n)
    else:
        print("* ",end="")
        print("  "*(n-2),end="")
        print("* ")


# wap program to print multiplication table in reverse order using for loop

# n = int(input("Enter the number: "))

# for i in range(10,0, -1):
#     print(f"{n} x {i} = {n*i}")



