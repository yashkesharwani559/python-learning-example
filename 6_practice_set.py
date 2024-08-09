# # write a program to print greater of 4 numbers

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))


# if(a1>a2):
    
#     if(a2>a3):
    
#         if(a3>a4):
#             print(a1)

#         else:
#             if(a1>a4):
#                 print(a1)
#             else:
#                 print(a4)
    
#     else:
#         if(a1>a3):
#             print(a1)
#         else:
#             print(a3)

# else:
#     print(a2)



# # write a program to print the percentage of three numbers

# marks1 = int(input("Enter the marks of 1st subject: "))
# marks2 = int(input("Enter the marks of 2nd subject: "))
# marks3 = int(input("Enter the marks of 3rd subject: "))

# total_percentage = ((marks1 + marks2 + marks3)/300)*100

# if(total_percentage >= 40 and marks1 >=33 and marks2 >=33 and marks3 >= 33):
#     print("You Passed.")
# else:
#     print("You are fail.")



# spam detection in message having words "Make a lot of money", "buy this", "subscribe this", "click this"

# msg = input("Enter the message: ")

# if("Make a lot of money".lower() in msg.lower() or "buy this".lower() in msg.lower() or "subscribe this".lower() in msg.lower() or "click this".lower() in msg.lower()):
#     print("spam mail")
# else:
#     print("mail is not spam")



# write a program to check that a username contains 10 characters or not

# username = input("Enter your username: ")

# if(len(username) < 10):
#     print("username not have 10 characters.")
# else:
#     print("username is correct.")




# write a program to grade a student from his marks

# marks = int(input("Enter your marks: "))

# if(marks<= 100 and marks >= 90):
#     grade = 'A'
# elif(marks < 90 and marks >= 80):
#     grade = 'B'
# elif(marks < 80 and marks >= 70):
#     grade = 'C'
# elif(marks < 70 and marks >= 60):
#     grade = 'D'
# elif(marks < 60 and marks >= 50):
#     grade = 'E'
# else:
#     grade = 'F'

# print(f"Your grade is: {grade}")



# write a program to check that in the sentence is about "Harry" or not

sentence = input("Enter the sentence: ")

if("Harry".lower() in sentence.lower()):
    print("Sentence is talking about harry.")
else:
    print("Sentence is not talking about harry.")


