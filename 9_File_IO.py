# a = "a very long string with emails."

# reading from a file
# establishing connection with the file named file.txt

# # open() is a function in python that is used to open a file
# # it takes two arguments first is file path and second is mode of opening the file
# # but second argument is optional and by default it opens the file in the read in text mode

# modes are :-
# 'r' - reading
# 'w' - writing
# 'a' - appending
# '+' - for updating
# 'rb' - read in binary mode
# 'rt' - read in text mode default mode

# file = open("file.txt")
# content = file.readline()
# content = file.readlines()

# print(content, type(content))

# file.close()

# readline() -> reads one line at a time
# readlines() -> returns the list of all the lines of the file

# write on a file
# file = open("file.txt",'w')
# # write mode will remove the old written text and write this new text on the file

# file.write("Yash is a boss")


# file.close()



# f = open("file.txt")
# print(f.read())
# f.close()

# above three lines work can be done with 'with' statement as:

with open("file.txt") as f:
    print(f.read())

# here in with statement you don't have to explicitly close the file but it implicitly does it


