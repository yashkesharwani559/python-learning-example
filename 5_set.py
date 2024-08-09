# set in python

# set is a collection of unique (non-repetive) elements

a = {2, 5, 78}

print(a, type(a))

a = {} # will create an empty dictionary
a = set() # to make an empty set

print(a, type(a))


# elements don't repeat in sets
# but we can write it multiple times and they will be discarded

s = {23, 1, 1, 5,1, 1}
print(s) #{1,5,23}

# in set the elements are not ordered 


s = {4, "Harry", 45}
print(s, type(s))

# set allows elements of all types

# infact list,tuple,dictionary,set all allows all type of elements to be present at the same time
# means python always follows hetergeneous type 

# set is mutable


# properties of sets
# set are unordered means there order doesn't matters
# set are not indexed -> cannot access elements by index
# there is no way to change items in set but you can insert and remove the items of set and that's why set is mutable
# set cannot contain duplicate values


# methods of set

# add() to add element in the set
set = set()
set.add(123)

print(set)


# clear() make the set empty

# set.clear()
# print(set)


# copy() returns a shallow copy of the set
set1 = set.copy()

print(set1)


# discard() removes the given element from the set and if the element is not present in the set then it doesn't removes it and discard() can be called on empty set whereas remove() and pop() can't be called on an empty set
# set.discard(123)
# # set.discard(124)
# print(set)

# remove() removes the given element from the set but here if the elment is not present in the set then it gives the error (KeyError) and that's why discard() method is better than remove()
# set.remove(123)
# print(set)

# pop() removes a random element from the set
set.pop()
print(set)

print(len(set)) # to find the length of the set



# union() it is called on one set and takes another set as argument and return a new set containing the elements of both the sets
s1 = {34, 2, 1}
s2 = {56, 8, 23,1}

print(s1.union(s2))


# intersection() this method is also called on one set and takes the second set as input and returns a new set containing the elements that are common in both the sets

s1 = {2, 1, 56, 3}
s2 = {1, 5, 35, 56}
print(s1.intersection(s2))

print(s1-s2) # returns the elements of the s1 that are not common in s1 and s2


