# 🔹 1. What is a Function?

# A function is a block of reusable code that performs a specific task.

# Syntax:
# def function_name(parameters):
#     # body
#     return value

# 🔹 2. Basic Function Example
def greet():
    print("Hello!")


# Call it:

greet()

# 🔹 3. Function With Parameters

# Parameters are inputs to the function.

def greet(name):
    print(f"Hello, {name}!")


# Call:

greet("Alice")

# 🔹 4. Function With Return Type

# In Python, return types are not declared, but you return a value using return.

def add(a, b):
    return a + b


# Call:

result = add(10, 20)
print(result)  # 30

# ✔ Every function returns something

# If you use return, it returns that value.

# If you don’t, it returns None (i.e., void function).

# 🔹 5. Void Function (No Return Value)

# A void function performs an action but returns None.

def display_message():
    print("This is a message!")   # No return


# Call:

print(display_message())


# Output:

# This is a message!
None

# 🔹 6. Types of Parameters

# Python supports several parameter styles:

# ✔ 1. Positional arguments
def multiply(a, b):
    return a * b

# ✔ 2. Default arguments
def greet(name="User"):
    print("Hello,", name)

# ✔ 3. Keyword arguments
greet(name="Alice")

# ✔ 4. Variable-length arguments (*args)

# Accepts unlimited positional arguments.

def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))  # 10

# ✔ 5. Variable keyword arguments (**kwargs)

# Accepts unlimited key-value arguments.

def show_info(**data):
    print(data)

show_info(name="Alice", age=25)

# 🔹 7. Returning Multiple Values

# Python allows returning multiple values using a tuple.

def stats(a, b):
    return a+b, a*b

s, p = stats(5, 3)
print(s, p)  # 8 15

# 🔹 8. Recursive Function

# A recursive function calls itself.

# Example: factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# Call:

print(factorial(5))  # 120


# ⚠ Must have a base condition to avoid infinite recursion.

# 🔹 9. Higher-Order Functions

# A function is higher-order if it:

# accepts another function as input, or

# returns a function

# Examples:

# ✔ Passing a function as a parameter
def apply_twice(func, x):
    return func(func(x))

def add1(n):
    return n + 1

print(apply_twice(add1, 5))  # 7

# ✔ Returning a function
def power(exponent):
    def inner(n):
        return n ** exponent
    return inner

square = power(2)
print(square(5))  # 25



# Example:

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)  # [1, 4, 9, 16]

# 🔹 10. Lambda Functions (Small Anonymous Functions)
square = lambda x: x*x
print(square(4))  # 16


# Useful with map/filter:

evens = list(filter(lambda x: x % 2 == 0, nums))

# 🧾 Summary
# Concept	Meaning	Example
# Basic function	Simple defined block	def f(): ...
# Return type	Value returned using return	return a+b
# Void function	No return → returns None	print()
# Parameters	Inputs to function	def f(a,b)
# *args	Variable positional args	def f(*args)
# **kwargs	Variable keyword args	def f(**kwargs)
# Recursive function	Calls itself	factorial
# Higher-order function	Takes/returns function	map, filter, or custom


# Problem 1: Function to add two numbers
# Example: add(2, 3) -> Output: 5
def add(a, b):
    return a + b
print("Problem 1 Output:", add(2, 3))

# Problem 2: Function to check if number is prime
# Example: is_prime(7) -> Output: True
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Problem 2 Output:", is_prime(7))

# Problem 3: Function to calculate factorial
# Example: factorial(5) -> Output: 120
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print("Problem 3 Output:", factorial(5))

# Problem 4: Function to check palindrome
# Example: is_palindrome("madam") -> Output: True
def is_palindrome(s):
    return s == s[::-1]
print("Problem 4 Output:", is_palindrome("madam"))

# Problem 5: Function to find sum of list elements
# Example: sum_list([1, 2, 3, 4]) -> Output: 10
def sum_list(lst):
    return sum(lst)
print("Problem 5 Output:", sum_list([1, 2, 3, 4]))
