# 1. Basic if Statement
x = 10

if x > 5:
    print("x is greater than 5")

# in python same indentation means a statement block

if x > 5 :
    print("x is greater than 5")

# 2. if...else Statement

x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


# 3. if...elif...else Statement

x = 5

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# 4. Nested if Statements

x = 15

if x > 10:
    if x < 20:
        print("x is between 10 and 20")

# Multiple elif statements

x = 7  
if x < 5:
    print("x is less than 5")
elif x < 10:
    print("x is between 5 and 10")
elif x < 15:
    print("x is between 10 and 15")
else:
    print("x is 15 or greater")


# Operators
"""greater than (>)
less than (<)
greater than or equal to (>=)
less than or equal to (<=)
comaprison (==)"""


# problem 1  =  Check if number is positive, negative or zero.

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# problem 2 =  Age eligibility for voting.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  

# problem 3 =  Find the largest of three numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))    


# problem 4 = . Check leap year.

year = int(input("Enter a year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")   
else:
    print(f"{year} is not a leap year.")


# problem 5 = Grade student based on marks.
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# problem 6 = Check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.") 






