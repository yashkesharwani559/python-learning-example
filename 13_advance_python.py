from functools import reduce


# virtual environment
# pip install virtualenv

# pip freeze -> command used to get name and versions of all the modules 

# pip freeze > requirements.txt


# lambda functions are functions that we create using lambda keyword
# lambda means function in the form of expression

# def sq(n):
#     return n*n

# same as
# var = lambda x: x*x

# print(var(6))




# join() method

# a = ["Harry", "Rohan", "Shubham"]

# res = "-".join(a)
# # join only works on list of strings

# print(res)



# format() in python
# a = "{} is a good {}".format("harry", "boy")
# a = "{0} is a good {1}".format("harry", "boy") #default
# a = "{1} is a good {0}".format("harry", "boy") #  boy is a good harry
# print(a)


# map(), filter(), reduce()
# map() applies into all the items of an input list
a = [1,2,3,4,5]

square = lambda x: x*x

l = map(square,a) # returns map object

# print(a)
# print(list(l))


# filter is basically used to filter the records of the list
even = lambda n: n%2==0

l = filter(even, a)

# print(list(l))


# reduce() -> returns only one value
# we have to import reduce() from functtools module

sum = lambda x,y: x+y

l = reduce(sum, a)

print(l)


