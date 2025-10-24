##question
#Write a program that will convert celsius value to fahrenheit

print("convert: celsius to fahrenheit----")

user_input= float(input("Enter your selcius number: "))

# F = (C * 1.8) + 32 Formula

your_fahrenheit = (user_input * 1.8) + 32

print(f'Your total fahrentheit is the {your_fahrenheit}') #print output


##question
#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
## Question------
# 04. Write a program that will reverse a four-digit number.
#     Also, it checks whether the reverse is true.

print("Let's reverse your four-digit number and verify it---")

# Taking 4-digit input from user
number = input("Enter a four-digit number: ")

# Check if it's exactly four digits
if len(number) == 4 and number.isdigit():
    # Reverse the number
    reversed_number = number[::-1]
    
    # Display both numbers
    print("\n-----------------------------------")
    print(f"Original Number : {number}")
    print(f"Reversed Number : {reversed_number}")
    print("-----------------------------------")

    # Check if reverse is correct
    if reversed_number == number[::-1]:
        print("✅ The reverse is TRUE — successfully reversed the number!")
    else:
        print("❌ The reverse is FALSE — something went wrong.")
else:
    print("⚠️ Please enter a valid four-digit number.")
