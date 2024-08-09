# list in python

# a list can have different type of values in it
# lists are mutable means its elements can be changed but strings are immutable
# a list can be indexed just like a string
# we can do slicing of list in a same way you are doing with strings
# list allows duplicates

# a list
friends = ["Apple", "Orange", 5, 3.12, False, "akash", "rohan"]

# print(friends[0])

# friends[0] = "Grapes"

# print(friends[0])
# print(friends[6])

# print(friends[1:5])

# # methods of list make the changes in the same list

print(friends)

# append() is a method to add at the end of the list
friends.append(23)
print(friends)

l1 = [12, 56, 98, 1, 1.56, 89]
print(l1)

# sort() sort the list of numbers
# l1.sort()
# print(l1)

# reverse() to reverse the list

# l1.reverse()

# print(l1)


#insert() to insert new element at the specified index but if index is more than or equal to the length of the list len(list) then it will work as append() and adds the element at the end

# print(len(l1))

# l1.insert(9, 14)
# l1.insert(2, 76)

# print(l1)


# pop() method deletes the element present at the given index and returns its value

# print(l1.pop(2))

# print(l1)



# remove() will removes the first occurence of the given element from the list

# l1.remove(1)

# print(l1)


l1.insert(0,1)

print(l1)
l1.remove(1)
print(l1)

