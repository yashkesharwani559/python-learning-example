# create a dictionary of hindi words as key and english words as value and user can look up on the dictionary

# words = {
#     "madad": 'help',
#     "kursi": "chair",
#     "billi":"cat"
# }

# word = input("Enter the word whose meaning you want: ")

# print(words.get(word))



# write a program to take 8 numbers from the user and display all unique numbers atleast once
# set = set()
# for i in range(0,8):
#     a = int(input("Enter the number: "))
#     set.add(a)

# print(set)



# can we have a set with values 18 and '18'
# Yes
# set = {18,'18'}
# print(set)



# find the length of the set
# set = set()
# set.add(20)
# set.add(20.0)
# set.add('20')
# print(len(set)) # 2
# because 1 == 1.0 in python
# print(1 == 1.0)


# find the type
# s = {}
# print(type(s)) # dictionary dict



# create an empty dictionary and let your 4 friends add their name as key and their favourite language as value in the dictionary and here name of friends are unique

# set = {}

# for i in range(0,4):
#     name = input("Enter your name: ")
#     lang = input("Enter your language: ")
#     set[name] = lang

# print(set)


# here in above question if two friends have same names the value is overridden and the last value would be there


# here in above question if two friends have same language as value then there would be no problem



# can you change the elements of a list that are contained in a set

# set = {1, 23, [45, 2, 12], "Harry"}
# this will give an error because you can't put list inside a set
# this is because elements of sets are immutable and hashable whereas elements of lists are non hashable and mutable

# so it is not possible to put a list inside a set
# but we can put a set inside a list


list = [23, {1,24}]
