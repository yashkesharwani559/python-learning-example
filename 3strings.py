# string is a sequence of characters enclosed in quotes
# single quoted string
# double quoted string
# triple quoted string 

# strings are immutable in python
# means if we do operations on it then it will create a new string

a = "hello"
b = 'hello'
c = '''hello'''
d = """hello"""


# slicing of string

name = "harry"

nameShort = name[2:5]
print(nameShort)
nameShort = name[2:5:3]
print(nameShort)

# to slice a string
# string_name[start_index, end_index, skip_value]

# here start_index is inclusive and end_index is exclusive
# skip_value is optional and it has value 1 by default

# negative index in string starts from -1 which starts assigning from the end of the string

print(name[-5:-1]) #harr
# name[-5:-1] same as name[0:4]
print(name[0:4])

print(name[-1:-5]) # prints nothing except a blank line

print(name[:4]) # same as name[0:4]

print(name[2:]) # same as name[2,5]



print(len(name))

print(name.endswith("rry")) # True
print(name.endswith("rrya")) # False

print(name.startswith("ha")) # True
print(name.startswith("hi")) # False

name = "harry are"

# name[0] = "h" # not allowed give problem

print(name.capitalize()) # capitalize() is a method in python that makes the first letter of the first word uppercase
# Harry are

a = """
    hello how are you
    """

print(a)


