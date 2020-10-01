# print("\" this is double backspace\'\\\\'\"")
# today = '17/09/2020\rtoday is a great day, we are happy and glad. thank God for this day'

# print(today)
# day = "it's raining"
# day = '\'it\'s raining\''
# day = "\"it's raining\""

# print(day)
# s = '\"hello\tworld\"'
# s.upper()
# print('hello' in s)
# print(s.upper())

# # METHODS
# print("HellO".lower())
# print(str(59))

# my_age = 87
# print (str(int(my_age) + 1))
# print(float(27))

# PROMPTING

# greeting = input("send a greeting ").upper()
# name = len(input("add a name "))
# thing = int(input())

# print(f"i just wanted to say {greeting} to {name} and {thing}")


# make an promt and convert the value to an int
# first_name = input('fisrst name: ')
# last_name = len(input('last name: '))
# age = int(input('age: ' ))
# print(f"welcome {first_name}{last_name} your new age is {age+1}" )


# print(80 // 6 != 20)

# print(not((80 * 5 == 6) and  (3**6 != 15)))

#Control flow

# my_name = input("What is your name? ")

#if statements
#if-else statements
#else-if statement
# while-loops
#for-loops
#do-while loops
#switch

# #if statements and if-else statments
# if (not(len(my_name) != 10)):
#     print("Thats a long name")
# else:
#     print("Not that long")


# # else-if statments
# if (len(my_name) == 10):
#     print("Thats a long name")
# elif (len(my_name) < 10):
#     print("That's not a long name")
# else:
#     print("That's more than ten letters")


# grading system
# score = float(input('score: '))
# if score >= 70 :
#     print('grade=A')
# elif (score >65 and()<= 69 ):
#     print('grade=B')
# elif score >50  <= 64:
#     print('grade=C')
# elif score >30 and()  <= 49:
#     print('grade=D')
# elif score >20 and() <=29:
#     print('grade=E')
# elif (score <=19 or() ==0):
#     print('carry over')
# else: print('NO RESULT')

# MODULE

#import statments
#arguments
#unpacking arguments
#running modules with arguments

#import argument(argv) method from sys module
from sys  import argv
#unpack the argv method
begin, first = argv

print(f"This is the script: {begin}")
print(f"This is the first arg: {first}")
# print("This is the 2nd arg:", second)
# print("This is the final arg:", third)




