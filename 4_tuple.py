# tuples in python
# tuples are same as list but tuples are immutable whereas list are mutable

# a tuple
a = (1,2,5,6)

print(type(a)) # tuple

a = () # empty tuple

a = (1) # python consider it as an integer enclosed in parenthesis

print(type(a)) #int

# to make a tuple with one element

a = (1,)

print(type(a)) #tuple

a = (12, 4.23, 54, False, "Yash", "hello")

print(a)

# a[0] = 45 # not allowed because we can't change in tuple

# print(a)

a = (1,0,1,1,0,0,1)

# methods in tuple

# count() returns the count of all the occurences of an element in the tuple and if not present returns 0

print(a.count(1))
print(a.count(2))

# list and tuple both can have distinct type of elements

# tuple is immutable 
# and list is a mutable type of tuple

# index() returns the index of the first occurence of the given input and if not present then it gives ValueError that 

print(a.index(0))
print(a.index(2)) # ValueError


