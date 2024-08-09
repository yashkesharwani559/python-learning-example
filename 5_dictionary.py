# dictionary in python

# collection of key-value pairs
# dictionary takes O(1) to get a value associated with the index
# it is like map of java but here the type of key or value is not fixed

# properties of dictionaries
# it is unordered
# it is mutable
# it is indexed
# it doesnot allow duplicate keys

# dictionary can be changed
# dictionary cannot have duplicate keys
# it is indexed that's why to get value we require O(1) time
# dictionary is unordered means its elements are not ordered
# means elements can be there in any order

marks = {
    "Harry": 100,
    "Shubham": 85,
    "Rohan": 34,
    50: "Yash",
    "Rohan": 23,
    "Aab": 67
}

print(len(marks)) # to find the length of the dictionary

print(marks, type(marks)) #type -> dict class

dict = {} # this will create an empty dictionary
print(dict)

# print(marks[0]) # not allowed

# print(marks["Harry"]) #100

# print(marks[50])


# methods of dictionary

# items() is a method that returns a list of key value pairs where the key value pairs are arranged in the tuple and these tuples are placed in the list
# items basically gives an object of dict_items on which we can iterate using the for loop

# print(marks.items())


# keys() returns the tuple of all the keys of the dictionary in the form of dict_items object
# print(marks.keys())


# values() returns the tuple of all the values of the dictionary in the form of dict_items object
# print(marks.values())



# update() method takes a dictionary as input and updates the dictionary on which it is called
# update() method can be used to add new key-value pairs in the dictionary
# we can update multiple key-value pairs at once

# marks.update({"Harry": 98, "Yash": 91})

# print(marks)


# get() method takes the key as input and returns the value associated with that key and if any key-value not exists with the given key then it will return None

print(marks.get("Harry"))
print(marks.get(91)) # None


# what is the difference between accessing the value using [] square brackets and using the get method (marks["Harry"] and marks.get("Harry"))
# if any key is not present in the dictionary then [] square bracket technique would give an error (KeyError) but the get() method would return None


# clear() method that make the dictionary empty
dict = {"hello": "hii"}
# print(dict)
# dict.clear()
# print(dict)


# copy() returns a shallow copy of the dictionary
dict2 = dict.copy()

# print(dict)
# print(dict2)
# dict.update({"Hello":"Bye"})
# print(dict)
# print(dict2)


# pop(key, defaultValue) remove the specified key-value pair and returns the value but if key doesn't exist then it returns the defaultValue but if defaultValue is not given then it raise KeyError
# print(dict.pop("hello")) # hii
# # print(dict.pop("Hello")) #KeyError
# print(dict.pop("Hello", 12)) # 12




