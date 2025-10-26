##question
#Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

#solve

# print("---Create a Traingle---")
# site_01 = int(input("Enter your x angle number: "))
# site_02 = int(input("Enter your y angel number: "))
# site_03 = int(input("Enter your z angle number: "))

# angle = (site_01 + site_02 + site_03)

# print("Total point number", angle)

# the_traingle = 180

# if angle == the_traingle and site_01 > 0 and site_02 > 0 and site_03 > 0:
#     print("Create a traingle")
# else:
#     print("not create a traingle")


##question
#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

#solve


# print("---User Profit---")

# cost_price = int(input("Enter you costing price: "))
# selling_price = int(input("Enter you selling price: "))

# if selling_price > cost_price:
#     profit = selling_price - cost_price
#     print(f" You profit {profit}")
# elif selling_price < cost_price:
#     loss = selling_price - cost_price
#     print(f"you loss {loss}")
# else:
#     print("NO loss, No profit") 


##question
#Write a program to find the simple interest when the value of principle, rate of interest and time period is given.

#solve

print('--- Simple Interest Calculator ---')

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100


print("Simple Interest =", simple_interest)





 
