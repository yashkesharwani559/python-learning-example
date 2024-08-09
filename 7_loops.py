# loops in python

# loops in python

# for loop
# while loop

# printing values 1 to 5 using for loop

# for i in range(1,6):
#     print(i)

# i = 1

# while(i<6):
#     print(i)
#     i += 1



# write a program to print 1 to 50 using while loop

# i = 1

# while(i<51):
#     print(i, end=", ")
#     i += 1



# print content of the list using while loop

# list = [1, "Harry", "bro", 3.45]

# i = 0

# while(i<len(list)):
#     print(list[i])
#     i += 1


# for loops in python

# for i in range(4):
#     print(i)


# range(n) -> generates number from 0 to n-1
# means if we give only one parameter to the range function than it is the range which is exclusive.
# range(start, end, step) -> here start is the starting (inclusive) value and end is the ending (exclusive) value and step is the amount of increment of the value after each iteration

# using for loop you can iterate over list, tuple, string

# printing all the elements of the list using for loop

# list = [1, 45, "Yash", 56.23, 231]
# tuple = (1, 45, 'Yash', 34.123, 156)

# for i in list:
#     print(i, end=", ")
# for i in tuple:
#     print(i, end=", ")


# s = 'hello'

# for i in s:
#     print(i, end=" ")

# we can use else with for loop in python

# list = [1, 23, 56]

# for i in list:
#     print(i)
# else:
#     print("completed")

# else will run just definitely after for loop when the control exits from the loop

# break -> to come out of the loop
# continue -> to skip the below code after the continue statement and move to the next iteration


# for i in range(50):
#     if(i == 20):
#         break
#     print(i)


# for i in range(6):
#     if(i == 2):
#         continue
#     print(i)


# pass -> is a keyword that says python to not to take problem of the no body of the loop, pass is a null statement, it means to do nothing


for i in range(5):
    pass

i = 0
while(i<10):
    print(i)
    i += 1




