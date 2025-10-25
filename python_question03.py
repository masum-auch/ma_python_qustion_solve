##question
#Write a program that will tell whether the number entered by the user is odd or even.

#solve

# print('---User print the Even or Odd number----')

# user_input = int(input("Enter your random number: "))

# user = user_input

# if user % 2 == 0:
#     print("The Even Number")
# else:
#     print("Odd Number")



##question
#Write a program that will tell whether the given year is a leap year or not.
#solve

# print("---The calculate by leap year.")

# user_input_year = int(input("Enter the year: "))

# if user_input_year % 400 == 0 and user_input_year % 100 == 0:
#     print(f'{user_input_year} is a leap year')
# elif user_input_year % 4 == 0 and user_input_year % 100 !=0 :
#     print(f'{user_input_year} is a the leap year.')
# else:
#     print(f'The input not a {user_input_year} leap year') 


##question
#Write a program to find the euclidean distance between two coordinates.

#solve

import math

user_x1 = int(input("Enter your X1 number: "))
user_y1 = int(input("Enter your Y1 number: "))
user_x2 = int(input("Enter your X2 number: "))
user_y2 = int(input("Enter your Y2 number: "))

# distance=(x2−x1)2+(y2−y1)2

distance = math.sqrt((user_x2 - user_x1)**2 + (user_y2 - user_y1)**2)

print(f'Euclidean distance between two coordinates {distance}') 