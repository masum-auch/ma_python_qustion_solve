##question
#User will input (2numbers).Write a program to swap the numbers


print("Create the swap number---")

frist_user_input = input("Enter your frist number: ")
second_user_input = input("Enter your second number: ")

print(f'\n Before Swapping:\nFrist = {frist_user_input}, Second = {second_user_input}')

frist_user_input, second_user_input = second_user_input, frist_user_input


print(f'After Swapping:\nFrist = {frist_user_input}, Second = {second_user_input}')
print(f"\n This is a swapping number")